from . import validators
from collections import namedtuple

fields = ['call', 'params', 'validator', 'validator_params']

check_definition = namedtuple(
    'CheckDefinition',
    fields,
    defaults=(None,) * len(fields)
)

CHECK_DEFINITIONS = [
    # transaction_status_api
    check_definition(
        "transaction_status_api.find_transaction",
        {"transaction_id": "b8660cc5464d37aa566e12d70349a30706a243063"},
    ),
    # account_by_key_api
    check_definition(
        "account_by_key_api.get_key_references",
        {},
    ),
    # condenser_api
    check_definition(
        "condenser_api.find_proposals",
        [[0]],  # proposal id: 0, return proposal.
        validators.should_return_at_least_one_element,
    ),
    check_definition(
        "condenser_api.get_account_count",
        [],
    ),
    check_definition(
        "condenser_api.get_account_history",
        ["hiveio", 100, 100],
    ),
    check_definition(
        "condenser_api.get_account_reputations",
        ["emre", 10],
        validators.should_return_at_least_one_element,
    ),
    check_definition(
        "condenser_api.get_accounts",
        [["emrebeyler"]],
        validators.should_return_at_least_one_element,
    ),
    check_definition(
        "condenser_api.get_active_witnesses",
        [],
        lambda resp: len(resp["result"]) == 21
    ),
    check_definition(
        "condenser_api.get_block",
        [8675309],
        lambda resp: resp["result"]["witness"] == "pfunk"
    ),
    check_definition(
        "condenser_api.get_block_header",
        [8675309],
        lambda resp: len(resp["result"].keys()) == 5,
    ),
    check_definition(
        "condenser_api.get_blog",
        ["hiveio", 0, 1],
        lambda resp: len(resp["result"]) == 1
    ),
    check_definition(
        "condenser_api.get_blog_entries",
        ["hiveio", 0, 3],
    ),
    check_definition(
        "condenser_api.get_chain_properties",
        [],
        lambda resp: isinstance(resp.get("result"), dict)
    ),
    check_definition(
        "condenser_api.get_comment_discussions_by_payout",
        [{"tag": "hive", "limit": 1}],
        validators.should_return_at_least_one_element,
    ),
    check_definition(
        "condenser_api.get_config",
        [],
        validators.should_return_a_dictionary,
    ),
    check_definition(
        "condenser_api.get_content",
        ["emrebeyler", "httpx"],
        validators.should_return_a_dictionary,
    ),
    check_definition(
        "tags_api.get_content_replies",
        {"author": "emrebeyler", "permlink": "httpx"},
        validators.should_return_at_least_one_element,
    ),
    check_definition(
        "block_api.get_block",
        {"block_num": 8675309},
        lambda resp: resp.get("result", {}).get("block", {}).get(
            "witness") == 'pfunk'
    ),
    check_definition(
        "block_api.get_block_header",
        {"block_num": 8675309},
        lambda resp: resp.get("result", {}).get("header", {}).get(
            "witness") == 'pfunk'
    ),
    check_definition(
        "database_api.get_current_price_feed",
        {"block_num": 8675309},
        validators.should_return_a_dictionary,
    ),
    check_definition(
        "database_api.get_dynamic_global_properties",
        {},
        validators.should_return_a_dictionary,
    ),

]
