# README

## Build and run a release

Note that this will not reload if changes are made in for example `main.py`.
Adapted from the [FastAPI tutorial](https://fastapi.tiangolo.com/deployment/docker/).

```sh
docker container rm irc-link-history-container  # Not needed the first time.
docker build -t irc-link-history-image .
docker run -d --name irc-link-history-container -p 8000:8000 irc-link-history-image
firefox localhost:8000
docker stop irc-link-history-container
docker container rm irc-link-history-container
```

## Develop

```sh
virualenv env   # Only needed the first time.
docker run -dit --name apache2 -p 80:80 -v $PWD/:/usr/local/apache2/htdocs/ httpd:2.4
source env/bin/activate
pip install -r requirements.txt
cd app
uvicorn main:app --reload
```
