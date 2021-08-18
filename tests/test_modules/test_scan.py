import pytest
from modules.scan import Scan
from modules.target import Target


@pytest.fixture
def scan():
    return Scan('firstScan')


@pytest.fixture
def target():
    return Target('127.0.0.1')


def test_init_scan(scan):
    assert scan.filename == 'firstScan'
    assert type(scan.date) is str
    assert scan.targets == []


def test_add_target(scan, target):
    len_targets_list = len(scan.targets)
    scan.add_target({})
    assert len(scan.targets) == len_targets_list
    scan.add_target(target)
    assert len(scan.targets) > len_targets_list
    assert scan.targets[0] == target


def test_final_recap(scan):
    assert type(scan.text_final_recap()) is str


def test_create_html_file(scan):
    assert type(scan.create_html_file()) is str
    assert scan.create_html_file() == f"[!] File create: {scan.filename}.html"
