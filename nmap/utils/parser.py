import argparse


# Parse args from the command line
def parser(args: list) -> argparse.Namespace:
    """Parse args from the command line

    Args:
        args (list): Command-line without the name of the program

    Returns:
        argparse.Namespace: Arguments
    """
    parser = argparse.ArgumentParser(
        description="A simple CLI script to launch Nmap and visualize result in HTML Report"
    )
    parser.add_argument(
        '-o',
        '--output',
        dest='report_filename',
        type=str,
        default='Report',
        help="Define the name of the report file"
    )
    parser.add_argument(
        '-t',
        '--targets',
        dest='targets',
        type=str,
        nargs='+',
        help="Define the target(s)"
    )
    parser.add_argument(
        '-tf',
        '--targetFile',
        dest='target_file',
        type=str,
        help="Define the target file"
    )
    return parser.parse_args(args)


def check_value_args(args: argparse.Namespace) -> bool:
    """Check if target_file or targets is correctly define
        Need to define target file or/and targets

    Args:
        args (argparse.Namespace): Args from argparse

    Raises:
        ValueError: Need to define target file or targets
        TypeError: target file is None and targets not define
        TypeError: targets not define and target file is not str

    Returns:
        bool: True correct - False incorrect
    """
    if args.target_file is None and args.targets is None:
        raise ValueError("[!] You need to specify targets or a target file")

    if args.target_file is None and type(args.targets) is not list:
        raise TypeError(
            "[!] Invalid type targets: You need to specify targets"
        )

    if args.targets is None and type(args.target_file) is not str:
        raise TypeError(
            "[!] Invalid type target_file: You need to specify the path to the target file"
        )

    return True
