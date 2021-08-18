import datetime
from modules.target import Target
import concurrent.futures
import os
import jinja2


class Scan:
    def __init__(self, filename: str):
        self.filename = filename
        self.date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.targets = []

    def start_scan(self, list_targets: list) -> str:
        """Start the threading
        launch a nmap scan on all the targets

        Args:
            list_targets (list): all the target to scan

        Returns:
            (str): the final recap
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for target in list_targets:
                futures.append(executor.submit(Target.scan_target, target))

            for future in concurrent.futures.as_completed(futures):
                self.add_target(future.result())

        return self.text_final_recap()

    def add_target(self, target):
        """Add target only if target instance of Target

        Args:
            target Target
        """
        if isinstance(target, Target):
            self.targets.append(target)

    def text_final_recap(self) -> str:
        """Return the final recap at the end of the scan

        Returns:
            str: The recap
        """
        text = "\n---------------\n"
        text = f'{text}[*] All the targets have been scans'
        for target in self.targets:
            text = f'{text}{str(target.text_final_recap())}'
        text = f'{text}\n---------------'
        return text

    def create_html_file(self) -> str:
        """Create html file

        Returns:
            str: text to give information
        """
        file = open(f'{self.filename}.html', "w")
        file.write(self.create_html_content())
        file.close()
        return f"[!] File create: {self.filename}.html"

    def create_html_content(self):
        """Create the content of the Html file with the template

        Returns:
            the content
        """
        path = os.path.join(os.path.dirname(__file__), '../templates')

        jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(path))

        jinja_var = {
            "date": self.date,
            "targets": self.targets,
        }

        return jinja_env.get_template('layout.html').render(jinja_var)
