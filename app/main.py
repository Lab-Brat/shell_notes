from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .utils import PathFinder, RichTextFormatter

app = FastAPI(root_path="/api")


@app.get("/{note}", response_class=HTMLResponse)
async def root(note):
    """
    Return the note in HTML format.
    """
    endpoints = PathFinder().all_note_paths
    for e in endpoints:
        try:
            e[note]
            return RichTextFormatter(e[note]).format()
        except:
            pass
    return "Note not found :(\n"


@app.get("/find/{note}")
async def find(note):
    """
    Search the note in existing directory tree
    """
    return {"message": PathFinder().search_note(note)}
