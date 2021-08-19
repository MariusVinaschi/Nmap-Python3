from utils.cli import cli
from argparse import Namespace

list_args = [
    "-o", 'simple_report',
    '-t', '127.0.0.1',
    '-tf', 'file_target.txt'
]
list_args_multiple_t_value = [
    "-o", "simple_report",
    '-t', '127.0.0.1',
    '192.168.1.1', '192.168.1.1/24'
]
list_args_without_ouput = ['-tf', 'file_target.txt']


def test_cli_type_return():
    assert type(cli([])) is Namespace
    assert type(cli(list_args)) is Namespace


def test_cli_value():
    args = cli(list_args)
    assert args.report_filename == "simple_report"
    assert args.targets == ["127.0.0.1"]
    assert args.target_file == "file_target.txt"


def test_cli_value_several_targets():
    args = cli(list_args_multiple_t_value)
    assert args.report_filename == "simple_report"
    assert args.targets == ['127.0.0.1', '192.168.1.1', '192.168.1.1/24']


def test_cli_value_without_ouput():
    args = cli(list_args_without_ouput)
    assert args.report_filename == "Report"
    assert args.target_file == "file_target.txt"
