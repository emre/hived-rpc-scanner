# hived-rpc-scanner

A CLI tool to check the status of Hive RPC nodes by testing certain endpoints.

<center><img src="https://i.imgur.com/0NWDpWz.png"></center>

# Installation

Requires Python3.6+.

```
$ (sudo) pip install hived_rpc_scanner
```

# Usage

```
$ hived_rpc_scanner --nodes <node_url_1> <node_url_2> <...>
```

# Example
```
$ hived_rpc_scanner --nodes https://api.hive.blog https://hived.emre.sh
(rpc-env) ➜  /tmp hived_rpc_scanner --nodes https://hived.emre.sh https://api.hive.blog
 > 42 requests sent in 4.75 seconds.
+----------------------------------------------------------------------------------------------------+
|                                       transaction_status_api                                       |
+-----+-----------------------+-----------------------------------------+--------+-----------+-------+
| #   | Node                  | Call                                    | Status | Time [ms] | Error |
+-----+-----------------------+-----------------------------------------+--------+-----------+-------+
| [1] | https://hived.emre.sh | transaction_status_api.find_transaction | ✅     | 3321      | -     |
| [2] | https://api.hive.blog | transaction_status_api.find_transaction | ✅     | 4555      | -     |
+-----+-----------------------+-----------------------------------------+--------+-----------+-------+
+--------------------------------------------------------------------------------------------------+
|                                        account_by_key_api                                        |
+-----+-----------------------+---------------------------------------+--------+-----------+-------+
| #   | Node                  | Call                                  | Status | Time [ms] | Error |
+-----+-----------------------+---------------------------------------+--------+-----------+-------+
| [1] | https://hived.emre.sh | account_by_key_api.get_key_references | ✅     | 451       | -     |
| [2] | https://api.hive.blog | account_by_key_api.get_key_references | ✅     | 1039      | -     |
+-----+-----------------------+---------------------------------------+--------+-----------+-------+
+------------------------------------------------------------------------------------------------------------+
|                                               condenser_api                                                |
+-----+-----------------------+-------------------------------------------------+--------+-----------+-------+
| #   | Node                  | Call                                            | Status | Time [ms] | Error |
+-----+-----------------------+-------------------------------------------------+--------+-----------+-------+
| [1] | https://hived.emre.sh | condenser_api.find_proposals                    | ✅     | 455       | -     |
| [2] | https://api.hive.blog | condenser_api.find_proposals                    | ✅     | 1092      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_account_count                 | ✅     | 457       | -     |
| [2] | https://api.hive.blog | condenser_api.get_account_count                 | ✅     | 1028      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_account_history               | ✅     | 581       | -     |
| [2] | https://api.hive.blog | condenser_api.get_account_history               | ✅     | 1986      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_account_reputations           | ✅     | 460       | -     |
| [2] | https://api.hive.blog | condenser_api.get_account_reputations           | ✅     | 1689      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_accounts                      | ✅     | 488       | -     |
| [2] | https://api.hive.blog | condenser_api.get_accounts                      | ✅     | 1370      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_active_witnesses              | ✅     | 480       | -     |
| [2] | https://api.hive.blog | condenser_api.get_active_witnesses              | ✅     | 1050      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_block                         | ✅     | 451       | -     |
| [2] | https://api.hive.blog | condenser_api.get_block                         | ✅     | 1115      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_block_header                  | ✅     | 467       | -     |
| [2] | https://api.hive.blog | condenser_api.get_block_header                  | ✅     | 1318      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_blog                          | ✅     | 1184      | -     |
| [2] | https://api.hive.blog | condenser_api.get_blog                          | ✅     | 1199      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_blog_entries                  | ✅     | 511       | -     |
| [2] | https://api.hive.blog | condenser_api.get_blog_entries                  | ✅     | 1125      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_chain_properties              | ✅     | 460       | -     |
| [2] | https://api.hive.blog | condenser_api.get_chain_properties              | ✅     | 1356      | -     |
| [1] | https://api.hive.blog | condenser_api.get_comment_discussions_by_payout | ✅     | 1724      | -     |
| [2] | https://hived.emre.sh | condenser_api.get_comment_discussions_by_payout | ✅     | 2377      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_config                        | ✅     | 492       | -     |
| [2] | https://api.hive.blog | condenser_api.get_config                        | ✅     | 1026      | -     |
| [1] | https://hived.emre.sh | condenser_api.get_content                       | ✅     | 597       | -     |
| [2] | https://api.hive.blog | condenser_api.get_content                       | ✅     | 2018      | -     |
+-----+-----------------------+-------------------------------------------------+--------+-----------+-------+
+-----------------------------------------------------------------------------------------+
|                                         tags_api                                        |
+-----+-----------------------+------------------------------+--------+-----------+-------+
| #   | Node                  | Call                         | Status | Time [ms] | Error |
+-----+-----------------------+------------------------------+--------+-----------+-------+
| [1] | https://hived.emre.sh | tags_api.get_content_replies | ✅     | 1149      | -     |
| [2] | https://api.hive.blog | tags_api.get_content_replies | ✅     | 1727      | -     |
+-----+-----------------------+------------------------------+--------+-----------+-------+
+---------------------------------------------------------------------------------------+
|                                       block_api                                       |
+-----+-----------------------+----------------------------+--------+-----------+-------+
| #   | Node                  | Call                       | Status | Time [ms] | Error |
+-----+-----------------------+----------------------------+--------+-----------+-------+
| [1] | https://hived.emre.sh | block_api.get_block        | ✅     | 548       | -     |
| [2] | https://api.hive.blog | block_api.get_block        | ✅     | 1092      | -     |
| [1] | https://hived.emre.sh | block_api.get_block_header | ✅     | 514       | -     |
| [2] | https://api.hive.blog | block_api.get_block_header | ✅     | 1325      | -     |
+-----+-----------------------+----------------------------+--------+-----------+-------+
+-------------------------------------------------------------------------------------------------------+
|                                              database_api                                             |
+-----+-----------------------+--------------------------------------------+--------+-----------+-------+
| #   | Node                  | Call                                       | Status | Time [ms] | Error |
+-----+-----------------------+--------------------------------------------+--------+-----------+-------+
| [1] | https://hived.emre.sh | database_api.get_current_price_feed        | ✅     | 449       | -     |
| [2] | https://api.hive.blog | database_api.get_current_price_feed        | ✅     | 1067      | -     |
| [1] | https://hived.emre.sh | database_api.get_dynamic_global_properties | ✅     | 477       | -     |
| [2] | https://api.hive.blog | database_api.get_dynamic_global_properties | ✅     | 1009      | -     |
+-----+-----------------------+--------------------------------------------+--------+-----------+-------+
```

