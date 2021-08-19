from utils.extract import filter_targets
import pytest

list_targets = [
    "-t", '127.0.0.1',
    "192.168.1.1", "192.168.1.24/24",
    "simple_string", "google.com",
    "fe80::20d:61ff:fe22:3476",
    {}, 1
]


def test_type():
    with pytest.raises(TypeError) as exec_info:
        filter_targets({})
    assert '[!] list targets must be a list' in str(exec_info.value)
    assert type(filter_targets([])) is list


def test_filter_targets():
    assert filter_targets([]) == []
    list_filter_targets = [
        '127.0.0.1', "192.168.1.1",
        "192.168.1.24/24", "google.com",
        "fe80::20d:61ff:fe22:3476"
    ]
    assert filter_targets(list_targets) == list_filter_targets
