import os
from rich.console import Console
from rich.markdown import Markdown


class PathFinder:
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.root = os.path.dirname(self.path)
        self.data = self.root + "/data"
        self.source = os.environ.get("SN_SOURCE", "submodule")
        self.all_paths = self.get_paths()

    def get_submodule(self, data):
        all_paths = []
        for root, _, files in os.walk(data, topdown=True):
            all_paths.extend(
                [
                    {file[0:-3]: f"{root}/{file}"}
                    for file in files
                    if file.endswith(".md") and file != "README.md"
                ]
            )
        return all_paths

    def get_github(self):
        link = os.environ.get("SN_GITHUB_LINK")
        rep_name = link.split("/")[-1][0:-4]
        tmp_path = f"/tmp/shell_notes_{rep_name}"
        os.system(f"git clone {link} {tmp_path}")
        return tmp_path

    def get_paths(self):
        if self.source == "submodule":
            return self.get_submodule(self.data)
        elif self.source == "github":
            return self.get_submodule(self.get_github())


class RichTextFormatter:
    def __init__(self, note):
        self.note = self.reader(note)

    def reader(self, note):
        with open(note, "r") as f:
            return f.read()

    def format(self):
        console = Console()
        with console.capture() as capture:
            console.print(Markdown(self.note))
        return capture.get()


if __name__ == "__main__":
    print(PathFinder().all_paths)
