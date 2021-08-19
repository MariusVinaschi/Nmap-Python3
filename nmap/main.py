import sys

from modules.scan import Scan
from utils.cli import cli, check_value_args
from utils.validation import is_valid_filename, is_valid_list_targets
from utils.extract import extract_targets

if __name__ == '__main__':
    args = cli(sys.argv[1:])

    try:
        is_valid_filename(args.report_filename)
        check_value_args(args)
        list_targets = extract_targets(args)
        is_valid_list_targets(list_targets)
    except TypeError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)

    new_scan = Scan(args.report_filename)
    print(new_scan.start_scan(list_targets))

    new_scan.create_html_file()
