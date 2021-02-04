import httpx
import asyncio
import uuid
import time
import traceback
import progressbar
from .checkers import CHECK_DEFINITIONS


def build_request_body(method, params):
    """Build a JSON-RPC request body based on the parameters given."""
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": str(uuid.uuid4())
    }
    return data


async def rpc_request(client, node, call, params, validator, validator_params):
    response = await client.post(
        node,
        json=build_request_body(call, params)
    )
    response = response.json()

    status = True
    if 'error' in response:
        status = False
    else:
        if validator:
            status = validator(response, *validator_params)
            if not status:
                # log the resp here
                # since the validation is failed
                print(response)

    return status, response


async def runner(nodes):
    results = {}
    total_requests = 0
    total_hits = len(nodes) * len(CHECK_DEFINITIONS)
    bar = progressbar.ProgressBar(max_value=total_hits, redirect_stdout=True)
    i = 0
    async with httpx.AsyncClient() as client:
        for definition in CHECK_DEFINITIONS:
            api_type = definition.call.split(".")[0]
            for node in nodes:
                result = {"node": node}
                start_time = time.time()
                status = None
                try:
                    status, response = await rpc_request(
                        client, node, definition.call,
                        definition.params, definition.validator, definition.validator_params or [])
                    if not status:
                        # in case we have a RPC error
                        # update the dict with the response dict
                        # so that we can investigate the error details
                        rpc_error = response.get(
                            "error", {}).get("message")
                        if rpc_error:
                            result["error"] = rpc_error
                except Exception as error:
                    traceback.print_exc()
                    result.update({"error": error.args[0]})
                end_time = time.time()
                result.update({"time_spent": round(end_time - start_time, 4)})
                total_requests += 1

                # boiler plate checks to set the default dict
                if api_type not in results:
                    results[api_type] = {}

                if definition.call not in results[api_type]:
                    results[api_type][definition.call] = {}

                if status not in results[api_type][definition.call]:
                    results[api_type][definition.call][status] = []

                results[api_type][definition.call][status].append(result)

                # update the progress bar
                i += 1
                bar.update(i)
            for _status in [True, False]:
                if _status in results[api_type][definition.call]:
                    results[api_type][definition.call][_status].sort(
                        key=lambda x: x["time_spent"])

    return results, total_requests


def main(nodes):
    start_time = time.time()
    loop = asyncio.get_event_loop()
    results, total_requests = loop.run_until_complete(runner(nodes))
    end_time = time.time()
    return results, total_requests, round(end_time - start_time, 2)
