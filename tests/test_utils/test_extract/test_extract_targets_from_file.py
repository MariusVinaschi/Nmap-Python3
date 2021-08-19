import pytest
from utils.extract import extract_targets_from_file


def test_exception_extract_targets_from_file():
    with pytest.raises(TypeError) as exec_info:
        extract_targets_from_file({})
    assert "[!] filename must be a string" in str(exec_info.value)
    with pytest.raises(ValueError) as exec_info:
        extract_targets_from_file("invalid_name")
    assert "[!] Can't find the target file" in str(exec_info.value)


def test_extract_targets_from_file():
    list_valid_targets_targetfile = [
        "192.168.1.95", "192.168.1.25",
        "192.168.1.27", "192.168.1.20",
        "192.168.1.254", "192.168.1.10",
        "fe80::20d:6161:fe22:3876"
    ]
    list_valid_targets_targetfile2 = [
        "192.168.1.95", "192.168.1.25",
        "192.168.1.27", "192.168.1.20",
        "192.168.1.254", "google.com",
        "1888888888888888888888", "192.168.1.10/12",
        "fe80::20d:6161:fe22:3876", "somte_text"
    ]
    assert len(extract_targets_from_file('./targets/TargetFile.txt')) \
        == len(list_valid_targets_targetfile)
    assert len(extract_targets_from_file('./targets/TargetFile2.txt')) \
        == len(list_valid_targets_targetfile2)
    assert not set(extract_targets_from_file('./targets/TargetFile.txt')) \
        ^ set(list_valid_targets_targetfile)
    assert not set(extract_targets_from_file('./targets/TargetFile2.txt')) \
        ^ set(list_valid_targets_targetfile2)
