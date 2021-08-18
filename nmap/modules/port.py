from modules.vuln import Vuln


class Port:
    def __init__(
        self,
        port_id: str,
        service: str,
        product: str,
        version: str,
        extrainfo: str,
        vulns: list
    ):
        self.port_id = port_id
        self.service = service
        self.product = product
        self.version = version
        self.extrainfo = extrainfo
        self.vulns = vulns

    @classmethod
    def create_port(cls, nmap_port: dict):
        """Create an instance of Port class

        Args:
            nmap_port (dict): A dict with port info. Come from nmap result

        Returns:
            None or an Instance of Port
        """
        port_id = ""
        if 'portid' in nmap_port:
            port_id = nmap_port['portid']

        service = ""
        product = ""
        version = ""
        extrainfo = ""

        if 'service' in nmap_port:

            if "name" in nmap_port['service']:
                service = nmap_port['service']["name"]

            if "product" in nmap_port['service']:
                product = nmap_port['service']["product"]

            if "version" in nmap_port['service']:
                version = nmap_port['service']["version"]

            if "extrainfo" in nmap_port['service']:
                extrainfo = nmap_port['service']["extrainfo"]

        vulns = []
        if "scripts" in nmap_port:
            for script in nmap_port['scripts']:
                if 'name' in script and "data" in script and script['name'] == "vulners":
                    list_keys = list(script['data'].keys())
                    for key in list_keys:
                        if "children" in script['data'][key]:
                            for vuln in script['data'][key]['children']:
                                new_vuln = Vuln.create_vuln(vuln)
                                if isinstance(new_vuln, Vuln):
                                    vulns.append(new_vuln)

        if port_id != '':
            return Port(port_id, service, product, version, extrainfo, vulns)

        return None
