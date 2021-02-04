from prettytable import PrettyTable
from colored import fg, bg, attr
from .core import main

import argparse

default_nodes = [
    "https://hived.emre.sh",
    "https://api.hive.blog",
]

ok_color = bg('green') + fg('white')
nok_color = bg('red') + fg('white')
reset = attr('reset')


def runner():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nodes', nargs='+', )
    arguments = parser.parse_args()
    resp, total_requests, overall_time_spent = main(nodes=arguments.nodes or default_nodes)

    for api_type, call in resp.items():
        table = PrettyTable()
        table.field_names = ["#", "Node", "Call", "Status", "Time [ms]",
                             "Error"]
        table.align = "l"
        for sub_call, scan_statuses in call.items():
            for scan_status, scan_results in scan_statuses.items():
                i = 1
                for scan_result in scan_results:
                    table.add_row(
                        [f"[{i}]",
                         scan_result["node"],
                         sub_call,
                         ok_color + "OK" + reset if scan_status else nok_color + "NOK" + reset,
                         int(scan_result["time_spent"] * 1e4),
                         scan_result.get("error", "-")]
                    )
                    i += 1
        print(table.get_string(title=f"{api_type}"))
    print(f" > {total_requests} requests sent in {overall_time_spent} seconds.")
