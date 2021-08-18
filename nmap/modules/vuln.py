class Vuln:
    def __init__(self, type: str, id: str, cvss: str, is_exploit: bool):
        self.type = type
        self.id = id
        self.cvss = cvss
        self.is_exploit = is_exploit

    @classmethod
    def create_vuln(cls, vuln: dict):
        """Create an instance of Vuln class

        Args:
            script (dict): A dict with vuln information. Come from the Nmap dict result

        Returns:
            (None or Vuln): Return an instance of Vuln class or None if not correct
        """

        if ('id' in list(vuln.keys()) and 'type' in list(vuln.keys())
                and vuln['type'] == "cve" and 'cvss' in list(vuln.keys())
                and 'is_exploit' in list(vuln.keys())):

            is_exploit = False
            if vuln['is_exploit'].lower == "true":
                is_exploit = True

            return Vuln(vuln['type'], vuln['id'], vuln['cvss'], is_exploit)

        return None
