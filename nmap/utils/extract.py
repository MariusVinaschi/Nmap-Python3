from argparse import Namespace
from utils.validation import is_valid_ip, is_valid_hostname
import os


def extract_targets(args: Namespace) -> list:
    """Extract target from targets list and the target file
    Create a list with only valid targets

    Args:
        args (Namespace): args from the cli

    Raises:
        TypeError: Args must be a Namespace

    Returns:
        list: Only valid targets
    """
    if type(args) is not Namespace:
        raise TypeError("[!] Invalid type for args")

    list_targets = []

    if args.target_file:
        try:
            list_targets = list(
                set(list_targets + filter_targets(extract_targets_from_file(args.target_file)))
            )
        except IOError:
            print("[!] An error occurred when the program tries to open the file")
        except Exception as e:
            print(e)

    if args.targets:
        try:
            list_targets = list(set((list_targets + filter_targets(args.targets))))
        except TypeError as e:
            print(e)

    return list_targets


def filter_targets(list_targets: list) -> list:
    """Filter a list to validate each targets (IP / hostname /cidr)

    Args:
        list_targets (list): Targets

    Raises:
        TypeError: list_targets is not a list

    Returns:
        list: Return a list with correct targets
    """
    if type(list_targets) is not list:
        raise TypeError('[!] list targets must be a list')

    list_filter_targets = []

    for target in list_targets:
        if is_valid_hostname(target) or is_valid_ip(target):
            list_filter_targets.append(target)
        else:
            print(f'[!] This target {target} will be skip: invalid format')

    return list_filter_targets


def extract_targets_from_file(filename: str) -> list:
    """Extract targets from target file

    Args:
        filename (str): the path of the file

    Raises:
        TypeError: Filename must be a string
        ValueError: Can't find the file

    Returns:
        list: List of targets
    """
    if type(filename) is not str:
        raise TypeError("[!] filename must be a string")

    if not os.path.isfile(filename):
        raise ValueError("[!] Can't find the target file")

    file = open(filename, mode='r')
    lines = file.readlines()
    file.close()
    return [line.split(maxsplit=1)[0] for line in lines if line.strip()]
