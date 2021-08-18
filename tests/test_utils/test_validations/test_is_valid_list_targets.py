import pytest
from nmap.utils.validation import is_valid_list_targets


def test_type():
    with pytest.raises(TypeError) as excinfo:
        is_valid_list_targets({})
    assert "[!] Invalid Type list_targets: must be a list" in str(excinfo.value)
    with pytest.raises(ValueError) as excinfo:
        is_valid_list_targets([])
    assert "[!] Invalid Value list_targets: no targets to scan" in str(excinfo.value)
    assert is_valid_list_targets(["127.0.0.1"]) is True
