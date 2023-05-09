### Introduction
This is an API for accessing my notes using curl from a Linux shell. 

### Testing
To run the app locally for testing purposes, 
navigate to the project directory and run:
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip 
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Installation
Build the docker image:
```bash
docker build -t shell_notes_api .
```

Start the continer:
```bash
docker run --name shell_notes \
           --volume ./data/:/code/data \
           -p 127.0.0.1:8000:8000/tcp  \
           -e SN_SOURCE="github" \
           -e SN_GITHUB_LINK="https://github.com/Lab-Brat/cheatsheets.git" \
           -d -t shell_notes_api
```

### How To Use
Test if it's working:
```bash
# test general availability
curl http://127.0.0.1:8000

# get a note
curl http://127.0.0.1:8000/notes/git

# find a note
curl http://127.0.0.1:8000/find/git
```

