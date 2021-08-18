from modules.port import Port
from typing import Union


class Host:
    def __init__(self, host: str, hostname: str, mac: str):
        self.host = host
        self.hostname = hostname
        self.mac = mac
        self.ports = []

    @classmethod
    def create_host(cls, host: str, nmap_host_result: dict):
        """Create an instance of Host Class

        Args:
            host (str): name of the host
            nmap_host_result (dict): dict result from nmap

        Returns:
            (Host or None) Create an instance of Host
        """
        if type(host) is not str or host == "":
            return None

        hostname = cls.extract_hostname(nmap_host_result['hostname'])
        if not hostname:
            hostname = ""

        mac_address = cls.extract_mac_address(nmap_host_result['macaddress'])
        if not mac_address:
            mac_address = ""

        return Host(host, hostname, mac_address)

    def add_port(self, port: Union[Port, None]):
        """Add port to port list

        Args:
            port (Port) or None
        """
        if isinstance(port, Port):
            self.ports.append(port)

    def text_recap(self) -> str:
        """Return a small text about the host

        Returns:
            str: the recap
        """
        text = f'[+] Host up : {str(self.host)}'
        if self.hostname:
            text = f'{text} - Hostname : {str(self.hostname)}'
        if len(self.ports) != 0:
            text = f'{text} - Open Ports : {str(len(self.ports))}'
        return f'{text}\n'

    @staticmethod
    def extract_hostname(list_hostname: list) -> Union[None, str]:
        """Extract hostname from the Nmap result list

        Args:
            list_hostname (list): The list from the Nmap result

        Returns:
            str or None: None if no hostname, str if hostname exist
        """
        if type(list_hostname) is not list:
            return None

        if list_hostname and 'name' in list_hostname[0]:
            return list_hostname[0]['name']

        return None

    @staticmethod
    def extract_mac_address(mac_address: str) -> Union[str, None]:
        """Extract mac address from the string:
            In the Nmap dict mac address can be "None"

        Args:
            mac_address (str): the mac address string

        Returns:
            [str, None]: None if don't exist or values
        """
        if type(mac_address) is not str:
            return None

        if mac_address == "None" or not mac_address:
            return None

        return mac_address
