### Introduction
This is an API for accessing my notes using curl from a Linux shell. 

### Installation
Build the docker image:
```bash
docker build -t shell_notes_api .
```

Start the continer:
```bash
docker run --name shell_notes \
           --volume ./data/:/code/data \
           -p 127.0.0.1:8000:8000/tcp \
           -d -t shell_notes_api
```

### How To Use
Test if it's working:
```bash
curl 127.0.0.1:8000
curl 127.0.0.1:8000/?note=git
```
