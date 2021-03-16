# README

## Run as a Developer

```sh
cd irc-link-history/public-html
docker run -it --name apache2 -p 80:80 -v $PWD/:/usr/local/apache2/htdocs/ httpd:2.4
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

## Prepare for Production

```sh
cd irc-link-history/public-html
docker run -dit --name apache2 -p 80:80 -v $PWD/:/usr/local/apache2/htdocs/ httpd:2.4
# Make sure const uriToAPI is correct.
docker build --compress -t irc-link-history:0.1 . # Number corresponding to version number in Changelog
docker run --name irc-link-history -p 8000:8000 irc-link-history
# Make sure both localhost:8000 and localhost:8000 is working correctly.
docker save irc-link-history -o irc-link-history.dockerfs
# scp over to the production server
```

## Run on Server

```sh
docker run --rm -dit --name apache2 -p 80:80 -v $PWD/:/usr/local/apache2/htdocs/ httpd:2.4
docker import irc-link-history -i irc-link-history.dockerfs
docker run --rm --name irc-link-history -p 8000:8000 irc-link-history
```

## Bugs

* Correct assignment of the `route` element to a `div`.

## Further Reading

MithrilJs tutorial [part 1](https://gilbert.ghost.io/mithril-js-tutorial-1/),  [part 2](https://gilbert.ghost.io/mithril-js-tutorial-2/) and [source code](https://github.com/gilbert/blog-post-examples/tree/gh-pages/mithril-2).
