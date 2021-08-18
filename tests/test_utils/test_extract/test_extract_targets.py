import pytest
from nmap.utils.extract import extract_targets
from nmap.utils.parser import parser

list_args = [
    "-t", '127.0.0.1',
    "192.168.1.1", "192.168.1.24/24",
    "simple_string", "google.com",
    "fe80::20d:61ff:fe22:3476",
    '-tf', './targets/TargetFile2.txt'
]
list_args_only_targets = [
    "-t", '127.0.0.1',
    "192.168.1.1", "192.168.1.24/24",
    "simple_string", "google.com",
    "fe80::20d:61ff:fe22:3476"
]
list_args_only_tf = ['-tf', './targets/TargetFile2.txt']


def test_types():
    with pytest.raises(TypeError) as excinfo:
        extract_targets([])
    assert "[!] Invalid type for args" in str(excinfo.value)
    args = parser(list_args)
    assert type(extract_targets(args)) is list
    args_tf = parser(list_args_only_tf)
    assert type(extract_targets(args_tf)) is list


def test_extract_targets():
    assert extract_targets(parser([])) == []
    correct_list_only_targets = [
        '127.0.0.1', "192.168.1.1",
        "192.168.1.24/24", "google.com",
        "fe80::20d:61ff:fe22:3476"
    ]
    assert len(extract_targets(parser(list_args_only_targets))) \
        == len(correct_list_only_targets)
    assert not set(extract_targets(parser(list_args_only_targets))) \
        ^ set(correct_list_only_targets)

    correct_list_only_tf = [
        "192.168.1.95", "192.168.1.25",
        "192.168.1.27", "192.168.1.20",
        "192.168.1.254", "google.com",
        "192.168.1.10/12", "fe80::20d:61ff:fe22:3476"
    ]
    assert len(extract_targets(parser(list_args_only_tf))) \
        == len(correct_list_only_tf)
    assert not set(extract_targets(parser(list_args_only_tf))) \
        ^ set(correct_list_only_tf)

    correct_list_both = [
        '127.0.0.1', "192.168.1.1",
        "192.168.1.24/24", "google.com",
        "fe80::20d:61ff:fe22:3476", "192.168.1.95",
        "192.168.1.25", "192.168.1.27",
        "192.168.1.20", "192.168.1.254",
        "192.168.1.10/12"
    ]

    assert len(extract_targets(parser(list_args))) \
        == len(correct_list_both)
    assert not set(extract_targets(parser(list_args))) \
        ^ set(correct_list_both)
