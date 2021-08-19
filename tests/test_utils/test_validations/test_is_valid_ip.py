from utils.validation import is_valid_ip


def test_type_error():
    assert is_valid_ip({}) is False
    assert type(is_valid_ip('127.0.0.1')) is bool


def test_value_ip():
    assert is_valid_ip('127.0.0.1') is True
    assert is_valid_ip('192.168.1.1/24') is True
    assert is_valid_ip('127.0.0') is False
    assert is_valid_ip('192.168') is False
    assert is_valid_ip('google.com') is False
    assert is_valid_ip("fe80::20d:61ff:fe22:3476") is True
