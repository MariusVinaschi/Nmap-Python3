import pytest
from nmap.utils.parser import parser, check_value_args
from argparse import Namespace

list_empty_args = []
list_args = ['-t', '127.0.0.1', '-tf', 'file_target.txt']
list_args_multiple_t_value = [
                                '-t', '127.0.0.1',
                                '192.168.1.1', '192.168.1.1/24'
                            ]
list_args_with_tf_value = ['-tf', 'file_target.txt']


def test_type():
    empty_args = parser(list_empty_args)
    with pytest.raises(ValueError) as excinfo:
        check_value_args(empty_args)
    assert "[!] You need to specify targets or a target file" in str(
        excinfo.value
    )

    with pytest.raises(TypeError) as excinfo:
        check_value_args(Namespace(
            target_file=None,
            targets=1
        ))
    assert "[!] Invalid type targets: You need to specify targets" in str(
        excinfo.value
    )
    with pytest.raises(TypeError) as excinfo:
        check_value_args(Namespace(
            target_file=1,
            targets=None
        ))
    assert "[!] Invalid type target_file: You need to specify the path to the target file" in str(
        excinfo.value
    )


def test_value_args():
    args = parser(list_args)
    assert check_value_args(args) is True
    args_multiple_t_value = parser(list_args_multiple_t_value)
    assert check_value_args(args_multiple_t_value) is True
    args_with_tf_value = parser(list_args_with_tf_value)
    assert check_value_args(args_with_tf_value) is True
