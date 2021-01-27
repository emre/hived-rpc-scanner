import httpx
import asyncio
import uuid
import time
import traceback

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


async def rpc_request(client, node, call, params, validator):
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
            status = validator(response)
            if not status:
                # log the resp here
                # since the validation is failed
                print(response)

    return status, response


async def runner(nodes):
    results = {}
    total_requests = 0
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
                        definition.params, definition.validator)
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
            results[api_type][definition.call][status].sort(
                key=lambda x: x["time_spent"])

    return results, total_requests


def main(nodes):
    start_time = time.time()
    results, total_requests = asyncio.run(runner(nodes))
    end_time = time.time()

    print(f" > {total_requests} "
          f"requests sent in {round(end_time - start_time, 2)} seconds.")
    return results
