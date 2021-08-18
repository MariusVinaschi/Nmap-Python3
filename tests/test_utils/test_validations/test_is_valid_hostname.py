from nmap.utils.validation import is_valid_hostname


def test_type_error():
    assert is_valid_hostname({}) is False
    assert type(is_valid_hostname('google.com')) is bool


def test_value_hostname():
    assert is_valid_hostname('google.com') is True
    assert is_valid_hostname("http://www.google.com") is False
    assert is_valid_hostname('1888888888888888888888') is False
