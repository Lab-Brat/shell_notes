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

    def read_source(self, data):
        """
        Traverse directory with os.walk and return a list of dicts
        with the name of the file as key and the full path as value.
        """
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
        """
        Clone the github repo and return the path to the data folder.
        """
        link = os.environ.get("SN_GITHUB_LINK")
        rep_name = link.split("/")[-1][0:-4]
        tmp_path = f"/tmp/shell_notes_{rep_name}"
        if not os.path.isdir(tmp_path):
            os.system(f"git clone {link} {tmp_path}")
        else:
            os.system(f"git -C {tmp_path} config pull.ff only")
            os.system(f"git -C {tmp_path} pull")
        return tmp_path

    def get_paths(self):
        """
        Return the paths to the notes based on the source.
        """
        if self.source == "submodule":
            return self.read_source(self.data)
        elif self.source == "github":
            return self.read_source(self.get_github())

    def search_note(self, note):
        """
        Search the note in the list of paths and return the path.
        """
        found = []
        for path in self.all_paths:
            path = list(path.keys())[0]
            if note in path:
                found.append(path)
        return found


class RichTextFormatter:
    def __init__(self, note):
        self.note = self.reader(note)

    def reader(self, note):
        """
        Read the note and return the content.
        """
        with open(note, "r") as f:
            return f.read()

    def format(self):
        """
        Format the Markdown note using rich and return the content.
        """
        console = Console()
        with console.capture() as capture:
            console.print(Markdown(self.note))
        return capture.get()


if __name__ == "__main__":
    print(PathFinder().all_paths)
