import pytest
from nmap.utils.validation import is_valid_filename


def test_type_error():
    with pytest.raises(TypeError) as excinfo:
        is_valid_filename({})
    assert "[!] Invalid Type filename: must be a string" in str(excinfo.value)
    assert type(is_valid_filename('filename')) is bool


def test_valid_name():
    with pytest.raises(ValueError) as excinfo:
        is_valid_filename('filename_123')
    assert "[!] Invalid value filename: Only letters and numbers" in str(excinfo.value)
    assert is_valid_filename('validfilename') is True
