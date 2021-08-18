import pytest
from modules.host import Host
from modules.port import Port


@pytest.fixture
def port():
    return Port("21", "ftp", "vsftpd", "2.3.4", "", [])


@pytest.fixture
def host():
    return Host("127.0.0.1", 'PC-1', '5E:FF:56:A2:AF:15')


def test_init_host(host):
    assert host.host == "127.0.0.1"
    assert host.hostname == "PC-1"
    assert host.mac == "5E:FF:56:A2:AF:15"
    assert host.ports == []


def test_create_host():
    host_1 = {
        "osmatch": {},
        "ports": [],
        "hostname": [
            {
                "name": "PC-1",
                "type": "PTR"
            }
        ],
        "macaddress": "None",
        "state": {
            "state": "up",
            "reason": "syn-ack",
            "reason_ttl": "0"
        }
    }
    instance_host1 = Host.create_host('127.0.0.1', host_1)
    assert isinstance(instance_host1, Host)
    assert instance_host1.host == "127.0.0.1"
    assert instance_host1.hostname == "PC-1"
    assert instance_host1.mac == ""
    assert instance_host1.ports == []
    host_2 = {
        "osmatch": {},
        "ports": [],
        "hostname": [],
        "macaddress": "5E:FF:56:A2:AF:15",
        "state": {
            "state": "up",
            "reason": "syn-ack",
            "reason_ttl": "0"
        }
    }
    instance_host2 = Host.create_host('127.0.0.1', host_2)
    assert isinstance(instance_host2, Host)
    assert instance_host2.host == "127.0.0.1"
    assert instance_host2.hostname == ""
    assert instance_host2.mac == "5E:FF:56:A2:AF:15"
    assert instance_host2.ports == []

    assert Host.create_host('', host_2) is None
    assert Host.create_host({}, host_2) is None


def test_text_recap(host, port):
    assert host.text_recap() == "[+] Host up : 127.0.0.1 - Hostname : PC-1\n"
    host.add_port(Port("21", "ftp", "vsftpd", "2.3.4", "", []))
    assert host.text_recap() == "[+] Host up : 127.0.0.1 - Hostname : PC-1 - Open Ports : 1\n"


def test_extract_hostname():
    correct_hostname = [
        {
            "name": "simple_desktop_name",
            "type": "PTR"
        }
    ]
    two_hostnames = [
        {
            "name": "simple_desktop_name",
            "type": "PTR"
        },
        {
            "name": "second_desktop_name",
            "type": "PTR"
        }
    ]
    invalid_dict_hostname = [
        {
            'incorrect': 'name'
        }
    ]
    assert Host.extract_hostname(correct_hostname) == "simple_desktop_name"
    assert Host.extract_hostname({}) is None
    assert Host.extract_hostname([]) is None
    assert Host.extract_hostname(two_hostnames) == "simple_desktop_name"
    assert Host.extract_hostname(invalid_dict_hostname) is None


def test_extract_mac_address():
    assert Host.extract_mac_address('None') is None
    assert Host.extract_mac_address('') is None
    assert Host.extract_mac_address([]) is None
    assert Host.extract_mac_address("5E:FF:56:A2:AF:15") == '5E:FF:56:A2:AF:15'


def test_add_port(host, port):
    len_ports_list = len(host.ports)
    host.add_port({})
    assert len(host.ports) == len_ports_list
    host.add_port(port)
    assert len(host.ports) > len_ports_list
    assert host.ports[0] == port
