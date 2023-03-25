from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from rich.console import Console
from rich.markdown import Markdown
from .pathfinder import PathFinder

app = FastAPI()


def reader(note):
    with open(note, "r") as f:
        return f.read()


def capture_console(note_string):
    console = Console()
    with console.capture() as capture:
        console.print(Markdown(note_string))
    return capture.get()


@app.get("/", response_class=HTMLResponse)
async def root(note: str):
    endpoints = PathFinder().all_paths
    for e in endpoints:
        try:
            e[note]
            return capture_console(reader(e[note]))
        except:
            pass
    return "Note not found :(\n"
