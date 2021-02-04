MIN_BLOCKCHAIN_VERSION = 1244  # 1.24.4
CHAIN_ID = 'beeab0de00000000000000000000000000000000000000000000000000000000'


def should_return_at_least_one_element(response, response_key="result", sub_response_key=None):
    results = response.get(response_key)
    if sub_response_key:
        results = results.get(sub_response_key)
    if not isinstance(results, list):
        return False
    if len(results) == 0:
        return False

    return True


def should_return_a_dictionary(response, response_key="result"):
    results = response.get(response_key)
    if not isinstance(results, dict):
        return False

    if not len(results.keys()):
        return False

    return True


def should_return_a_list(response, response_key="result"):
    results = response.get(response_key)
    if not isinstance(results, list):
        return False

    return True


def validate_get_version(response):
    version = response.get("result", {}).get("blockchain_version")
    if not version:
        return False
    if int(version.replace(".", "")) < MIN_BLOCKCHAIN_VERSION:
        return False

    if response.get("result", {}).get("chain_id") < CHAIN_ID:
        return False

    return True
