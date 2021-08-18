import nmap3
from typing import Union
from modules.host import Host
from modules.port import Port


class Target:
    def __init__(self, target: str):
        self.target = target
        self.hosts = []

    @classmethod
    def scan_target(cls, target: str):
        """Start a scan on a target. Launch Nmap - print partial recap -
        return a target instance

        Args:
            target (str): the target

        Returns:
            Target: instance of Target
        """
        print(f'[*] Start nmap on this target : {str(target)}')
        new_target = Target(target)
        new_target.nmap()
        print(new_target.text_partial_recap())
        return new_target

    def nmap(self):
        """Start a nmap scan on one Host"""
        nm = nmap3.Nmap()
        results = nm.nmap_version_detection(str(self.target), args="--script vulners")

        for key in results.keys():
            if self.is_interesting_result(results[key]) and key not in ['stats', 'runtime']:
                new_host = Host.create_host(key, results[key])

                if new_host is not None:
                    for port in results[key]['ports']:
                        new_port = Port.create_port(port)
                        new_host.add_port(new_port)

                self.add_host(new_host)

    def add_host(self, host: Union[Host, None]):
        """add host to the list of hosts

        Args:
            host (Host) or None
        """
        if isinstance(host, Host):
            self.hosts.append(host)

    def is_interesting_result(self, result: dict) -> bool:
        """Check if the dict has host information

        Args:
            result (dict) result from nmap

        Returns:
            [bool]: True correct - False Incorrect
        """
        if "macaddress" in result.keys() and "ports" in result.keys() and \
                "hostname" in result.keys():
            return True
        return False

    def text_partial_recap(self) -> str:
        """Generate text for the partial recap

        Returns:
            str: partial recap
        """
        if not self.hosts:
            return f'[?] No host up on this target {str(self.target)}'
        return f'[!] Target {str(self.target)} : {str(len(self.hosts))} Host(s) up'

    def text_final_recap(self) -> str:
        """Generate text final recap

        Returns:
            str: text final recap
        """
        text = f'\n[*] Target : {str(self.target)}'

        if not self.hosts:
            return f'{text}\n[?] No host up on this target'

        for host in self.hosts:
            if isinstance(host, Host):
                text = f'{text}\n{host.text_recap()}'

        return text
