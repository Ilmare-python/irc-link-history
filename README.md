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
cd irc-link-history/public-html
docker run -it --name apache2 -p 80:80 -v $PWD/:/usr/local/apache2/htdocs/ httpd:2.4 # use -dit instead of -it to hide output from the webserver.
cd ..
virualenv env   # Only needed the first time, or when new dependencies are added.
source env/bin/activate
pip install -r requirements.txt # Only needed when new dependencies are added.
cd app
uvicorn main:app --reload
# This is how you stop
docker stop apache2
docker container rm apache2
```

## Bugs

* Correct assignment of the `route` element to a `div`..

## Further Reading

MithrilJs tutorial [part 1](https://gilbert.ghost.io/mithril-js-tutorial-1/),  [part 2](https://gilbert.ghost.io/mithril-js-tutorial-2/) and [source code](https://github.com/gilbert/blog-post-examples/tree/gh-pages/mithril-2).
