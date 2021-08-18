import re
import ipaddress
import socket


def is_valid_ip(ip: str) -> bool:
    """Check if an IP is valid

    Args:
        ip (str): IP address to check

    Returns:
        bool: True correct - False Incorrect type or value
    """
    if type(ip) is not str:
        return False

    try:
        ipaddress.ip_network(ip, strict=False)
        return True
    except ValueError:
        return False


def is_valid_hostname(hostname: str) -> bool:
    """Valid a hostname

    Args:
        hostname (str): Hostname to check

    Returns:
        bool: True correct - False Incorrect type or value
    """
    if type(hostname) is not str:
        return False

    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False


def is_valid_filename(filename: str) -> bool:
    """Valid if filename is correct

    Args:
        filename (str): the filename to check

    Raises:
        TypeError: Filename is not a string
        ValueError: Doesn't respect the regex

    Returns:
        bool: True correct - False incorrect
    """
    if type(filename) is not str:
        raise TypeError("[!] Invalid Type filename: must be a string")

    regex_filename = r'^[A-Za-z0-9]{2,60}$'

    if not re.match(regex_filename, filename):
        raise ValueError("[!] Invalid value filename: Only letters and numbers")

    return True


def is_valid_list_targets(list_targets: list) -> bool:
    """ Valid the list after the filtering of inputs
        check if the list is not empty
        check the type

    Args:
        list_targets (list): list_targets only valid targets

    Raises:
        TypeError: Not a list
        ValueError: Empty list

    Returns:
        bool: True
    """
    if type(list_targets) is not list:
        raise TypeError("[!] Invalid Type list_targets: must be a list")

    if not list_targets:
        raise ValueError("[!] Invalid Value list_targets: no targets to scan")

    return True
