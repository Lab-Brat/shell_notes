import os
from rich.console import Console
from rich.markdown import Markdown


class PathFinder:
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.root = os.path.dirname(self.path)
        self.data = self.root + "/data"
        self.all_paths = self.get_paths()

    def get_paths(self):
        all_paths = []
        for root, _, files in os.walk(self.data, topdown=True):
            all_paths.extend(
                [
                    {file[0:-3]: f"{root}/{file}"}
                    for file in files
                    if file.endswith(".md") and file != "README.md"
                ]
            )
        return all_paths


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
