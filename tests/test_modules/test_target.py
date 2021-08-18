import pytest
from modules.target import Target
from modules.host import Host


@pytest.fixture
def host():
    return Host("127.0.0.1", 'PC-1', '5E:FF:56:A2:AF:15')


@pytest.fixture
def target():
    return Target('127.0.0.1')


def test_init_scan(target):
    assert target.target == '127.0.0.1'
    assert target.hosts == []


def test_scan_target_nmap():
    new_target = Target.scan_target('127.0.0.1')
    assert isinstance(new_target, Target)
    assert new_target.target == "127.0.0.1"
    assert len(new_target.hosts) > 0


def test_is_interesting_result(target):
    host = {
       "osmatch": {
       },
       "ports": [
       ],
       "hostname": [
          {
             "name": "simple_desktop_name",
             "type": "PTR"
          }
       ],
       "macaddress": "None",
       "state": {
          "state": "up",
          "reason": "conn-refused",
          "reason_ttl": "0"
       }
    }
    stats = {
        "scanner": "nmap",
        "args": "/usr/bin/nmap -oX - -sV 192.168.1.90 192.168.1.35",
        "start": "1628347310",
        "startstr": "Sat Aug  7 16:41:50 2021",
        "version": "7.80",
        "xmloutputversion": "1.04"
    }
    assert target.is_interesting_result(host) is True
    assert target.is_interesting_result(stats) is False


def test_add_host(target, host):
    len_host_list = len(target.hosts)
    target.add_host({})
    assert len(target.hosts) == len_host_list
    target.add_host(host)
    assert len(target.hosts) > len_host_list
    assert target.hosts[0] == host


def test_text_partial_recap(target, host):
    assert target.text_partial_recap() == "[?] No host up on this target 127.0.0.1"
    target.add_host(host)
    assert target.text_partial_recap() == "[!] Target 127.0.0.1 : 1 Host(s) up"


def test_text_final_recap(target, host):
    final_recap_without_host = "\n[*] Target : 127.0.0.1\n[?] No host up on this target"
    assert target.text_final_recap() == final_recap_without_host
    target.add_host(host)
    recap_host = "[+] Host up : 127.0.0.1 - Hostname : PC-1\n"
    final_recap_one_host = f"\n[*] Target : 127.0.0.1\n{recap_host}"
    assert target.text_final_recap() == final_recap_one_host
