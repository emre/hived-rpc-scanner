from . import validators
from collections import namedtuple

fields = ['call', 'params', 'validator', 'validator_params']

check_definition = namedtuple(
    'CheckDefinition',
    fields,
)

CHECK_DEFINITIONS = [
    # transaction_status_api
    check_definition(
        "transaction_status_api.find_transaction",
        {"transaction_id": "b8660cc5464d37aa566e12d70349a30706a243063"},
        None,
        None,
    ),
    # account_by_key_api
    check_definition(
        "account_by_key_api.get_key_references",
        {},
        None,
        None,
    ),
    # condenser_api
    check_definition(
        "condenser_api.find_proposals",
        [[0]],  # proposal id: 0, return proposal.
        validators.should_return_at_least_one_element,
        None,
    ),
    check_definition(
        "condenser_api.get_account_count",
        [],
        None,
        None,
    ),
    check_definition(
        "condenser_api.get_account_history",
        ["hiveio", 100, 100],
        None,
        None,
    ),
    check_definition(
        "condenser_api.get_account_reputations",
        ["emre", 10],
        validators.should_return_at_least_one_element,
        None,
    ),
    check_definition(
        "condenser_api.get_accounts",
        [["emrebeyler"]],
        validators.should_return_at_least_one_element,
        None,
    ),
    check_definition(
        "condenser_api.get_active_witnesses",
        [],
        lambda resp: len(resp["result"]) == 21,
        None,
    ),
    check_definition(
        "condenser_api.get_block",
        [8675309],
        lambda resp: resp["result"]["witness"] == "pfunk",
        None,
    ),
    check_definition(
        "condenser_api.get_block_header",
        [8675309],
        lambda resp: len(resp["result"].keys()) == 5,
        None,
    ),
    check_definition(
        "condenser_api.get_blog",
        ["hiveio", 0, 1],
        lambda resp: len(resp["result"]) == 1,
        None,
    ),
    check_definition(
        "condenser_api.get_blog_entries",
        ["hiveio", 0, 3],
        None,
        None,
    ),
    check_definition(
        "condenser_api.get_chain_properties",
        [],
        lambda resp: isinstance(resp.get("result"), dict),
        None,
    ),
    check_definition(
        "condenser_api.get_comment_discussions_by_payout",
        [{"tag": "hive", "limit": 1}],
        validators.should_return_at_least_one_element,
        None,
    ),
    check_definition(
        "condenser_api.get_config",
        [],
        validators.should_return_a_dictionary,
        None,
    ),
    check_definition(
        "condenser_api.get_content",
        ["emrebeyler", "httpx"],
        validators.should_return_a_dictionary,
        None,
    ),
    check_definition(
        "tags_api.get_content_replies",
        {"author": "emrebeyler", "permlink": "httpx"},
        validators.should_return_at_least_one_element,
        None,
    ),
    check_definition(
        "tags_api.get_comment_discussions_by_payout",
        {"tag": "photography", "limit": 1, "truncate_body": 1},
        validators.should_return_at_least_one_element,
        None,
    ),
    check_definition(
        "tags_api.get_discussion",
        {"author": "emrebeyler", "permlink": "httpx"},
        validators.should_return_a_dictionary,
        None,
    ),
    # check_definition(
    #     "tags_api.get_trending_tags",
    #     {"start_tag": "hive", "limit": 1},
    #     validators.should_return_at_least_one_element,
    #     None,
    # ),
    check_definition(
        "block_api.get_block",
        {"block_num": 8675309},
        lambda resp: resp.get("result", {}).get("block", {}).get(
            "witness") == 'pfunk',
        None
    ),
    check_definition(
        "block_api.get_block_header",
        {"block_num": 8675309},
        lambda resp: resp.get("result", {}).get("header", {}).get(
            "witness") == 'pfunk',
        None,
    ),
    check_definition(
        "database_api.get_current_price_feed",
        {"block_num": 8675309},
        validators.should_return_a_dictionary,
        None,
    ),
    check_definition(
        "database_api.get_dynamic_global_properties",
        {},
        validators.should_return_a_dictionary,
        None,
    ),
    check_definition(
        "bridge.account_notifications",
        {"account": "emrebeyler", "limit": 1},
        validators.should_return_a_list,
        None,
    ),
    check_definition(
        "bridge.get_ranked_posts",
        {"sort": "trending", "tag":"hive","observer": "emrebeyler"},
        validators.should_return_at_least_one_element,
        None,
    ),
    check_definition(
        "bridge.list_community_roles",
        {"community": "hive-111111"},
        validators.should_return_at_least_one_element,
        None,
    ),
    check_definition(
        "bridge.list_all_subscriptions",
        {"account": "emrebeyler"},
        validators.should_return_at_least_one_element,
        None,
    ),
    check_definition(
        "bridge.get_community",
        {"name": "hive-111111", "observer": "emrebeyler"},
        validators.should_return_a_dictionary,
        None,
    ),
    check_definition(
        "account_history_api.get_account_history",
        {
          "account": "emrebeyler",
          "start": 0,
          "limit": 1,
        },
        validators.should_return_at_least_one_element,
        ("result", "history"),
    ),
    check_definition(
        "account_history_api.get_ops_in_block",
        {"block_num": 8675309},
        validators.should_return_at_least_one_element,
        ("result", "ops"),
    ),
    check_definition(
        "account_history_api.get_transaction",
        {"id": "2bd270905d3d70baf145b7321b6d55fb923abb2e"},
        lambda x: x.get("result").get("block_num") == 8675309,
        None,
    )
]
