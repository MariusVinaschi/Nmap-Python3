from nmap.modules.vuln import Vuln


def test_create_vuln():
    vuln_dict = {
        'type': 'cve',
        'is_exploit': 'false',
        'cvss': '3.5',
        'id': 'CVE-2010-0733'
    }
    new_vuln = Vuln.create_vuln(vuln_dict)
    assert isinstance(new_vuln, Vuln)
    assert new_vuln.is_exploit is False
    assert new_vuln.type == "cve"
    assert new_vuln.cvss == "3.5"
    assert new_vuln.id == 'CVE-2010-0733'

    no_cve_vuln_dict = {
        'id': 'SECURITYVULNS:VULN:10803',
        'cvss': '6.5',
        'type': 'securityvulns',
        'is_exploit': 'false'
    }
    result_cve_vuln_dict = Vuln.create_vuln(no_cve_vuln_dict)
    assert result_cve_vuln_dict is None
    assert Vuln.create_vuln({}) is None
