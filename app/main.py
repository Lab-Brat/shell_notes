from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .utils import PathFinder, RichTextFormatter

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root(note: str):
    endpoints = PathFinder().all_paths
    for e in endpoints:
        try:
            e[note]
            return RichTextFormatter(e[note]).format()
        except:
            pass
    return "Note not found :(\n"
