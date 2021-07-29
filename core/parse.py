#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from core.attack import __go_for_attacks
from core.alert import info
from core.alert import write
from core.alert import messages
from core.load_modules import load_all_modules
from core.load_modules import load_all_graphs
from core.args_loader import load_all_args
from core.args_loader import check_all_required


def load():
    """
    load all ARGS, Apply rules and go for attacks

    Returns:
        True if success otherwise None
    """
    write("\n\n")
    # load all modules in lib/brute, lib/scan, lib/graph
    module_names = load_all_modules()
    graph_names = load_all_graphs()
    options = check_all_required(load_all_args())
    # Filling Options
    check_ranges = options.check_ranges
    check_subdomains = options.check_subdomains
    targets = options.targets
    targets_list = options.targets_list
    thread_number = options.thread_number + 1
    thread_number_host = options.thread_number_host
    log_in_file = options.log_in_file
    scan_method = options.scan_method
    exclude_method = options.exclude_method
    users = options.users
    users_list = options.users_list
    passwds = options.passwds
    passwds_list = options.passwds_list
    timeout_sec = options.timeout_sec
    ports = options.ports
    time_sleep = options.time_sleep
    language = options.language
    verbose_level = options.verbose_level
    show_version = options.show_version
    check_update = options.check_update
    socks_proxy = options.socks_proxy
    retries = options.retries
    graph_flag = options.graph_flag
    help_menu_flag = options.help_menu_flag
    ping_flag = options.ping_flag
    wizard_mode = options.wizard_mode
    profile = options.profile
    start_api = options.start_api
    api_host = options.api_host
    api_port = options.api_port
    api_debug_mode = options.api_debug_mode
    api_access_key = options.api_access_key
    api_client_white_list = options.api_client_white_list
    api_client_white_list_ips = options.api_client_white_list_ips
    api_access_log = options.api_access_log
    api_access_log_filename = options.api_access_log_filename
    api_cert = options.api_cert
    api_cert_key = options.api_cert_key
    backup_ports = ports


    info(messages(language, "scan_started"))
    info(messages(language, "loaded_modules").format(
        len(load_all_modules()) - 1 + len(load_all_graphs())))
    __go_for_attacks(targets, check_ranges, check_subdomains,
                     log_in_file, time_sleep, language, verbose_level, retries,
                     socks_proxy, users, passwds, timeout_sec,
                     thread_number, ports, ping_flag,
                     backup_ports, scan_method, thread_number_host,
                     graph_flag, profile, False)
    return True
