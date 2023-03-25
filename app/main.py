from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .pathfinder import PathFinder

app = FastAPI()


def reader(note):
    with open(note, "r") as f:
        return f.read()


@app.get("/", response_class=HTMLResponse)
async def root(note: str):
    endpoints = PathFinder().all_paths
    for e in endpoints:
        try:
            e[note]
            return reader(e[note])
        except:
            pass
    return "Note not found :(\n"
