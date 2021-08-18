import pytest
from nmap.modules.port import Port


@pytest.fixture
def port():
    return Port("21", "ftp", "vsftpd", "2.3.4", "", [])


def test_port_init(port):
    assert isinstance(port, Port)
    assert port.port_id == "21"
    assert port.service == "ftp"
    assert port.product == "vsftpd"
    assert port.version == "2.3.4"
    assert port.extrainfo == ""
    assert port.vulns == []


def test_create_port():
    port_21 = {
        "protocol": "tcp",
        "portid": "21",
        "state": "open",
        "reason": "syn-ack",
        "reason_ttl": "0",
        "service": {
            "name": "ftp",
            "product": "vsftpd",
            "version": "2.3.4",
            "ostype": "Unix",
            "method": "probed",
            "conf": "10"
        },
        "cpe": [
            {
                "cpe": "cpe:/a:vsftpd:vsftpd:2.3.4"
            }
        ],
        "scripts": []
    }
    port_22 = {
        "protocol": "tcp",
        "portid": "22",
        "state": "open",
        "reason": "syn-ack",
        "reason_ttl": "0",
        "service": {
            "name": "ssh",
            "product": "OpenSSH",
            "version": "4.7p1 Debian 8ubuntu1",
            "extrainfo": "protocol 2.0",
            "ostype": "Linux",
            "method": "probed",
            "conf": "10"
        },
        "cpe": [
            {
                "cpe": "cpe:/o:linux:linux_kernel"
            }
        ],
        "scripts": []
    }
    new_port_21 = Port.create_port(port_21)
    assert isinstance(new_port_21, Port)
    assert new_port_21.port_id == port_21['portid']
    assert new_port_21.service == port_21['service']["name"]
    assert new_port_21.product == port_21['service']['product']
    assert new_port_21.version == port_21['service']['version']
    assert new_port_21.extrainfo == ""
    assert new_port_21.vulns == []

    new_port_22 = Port.create_port(port_22)
    assert isinstance(new_port_22, Port)
    assert new_port_22.port_id == port_22['portid']
    assert new_port_22.service == port_22['service']["name"]
    assert new_port_22.product == port_22['service']['product']
    assert new_port_22.version == port_22['service']['version']
    assert new_port_22.extrainfo == port_22['service']['extrainfo']
    assert new_port_22.vulns == []

    no_port_id = {
        "protocol": "tcp",
        "portid": "",
        "state": "open",
        "reason": "syn-ack",
        "reason_ttl": "0",
        "service": {
            "name": "ssh",
            "product": "OpenSSH",
            "version": "4.7p1 Debian 8ubuntu1",
            "extrainfo": "protocol 2.0",
            "ostype": "Linux",
            "method": "probed",
            "conf": "10"
        },
        "cpe": [
            {
                "cpe": "cpe:/o:linux:linux_kernel"
            }
        ],
        "scripts": []
    }
    assert Port.create_port(no_port_id) is None
