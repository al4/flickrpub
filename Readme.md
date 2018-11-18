flickrpub
=========

Watches a directory of files and pushes them to a given flickr collection. Sub-directories are created as separate sets.

This is a one-shot project for gathering and uploading family photos from an event. I _may_ update it in future and respond to pull requests, but don't expect to spend a lot of time on this project!

NB: Unfinished at time of writing, documentation is thus hypothetical. May publish to pip if it ends up being polished enough.

Installation
------------

From git checkout:

```bash
python setup.py install
```

Configuration
-------------

First obtain an API key and secret as per the [flickrapi documentation](https://stuvel.eu/flickrapi-doc/3-auth.html). This is required by Flickr to use their API.

Save these credentials in a file named credentials.ini in your current working directory:
```ini
[flickrapi]
api_key = xxx
secret = xxx
```

Usage
-----
Publish a directory tree of files:
```bash
flickrpub <dir>
```
Watch a drectory and publish files as they are added:
```bash
flickrpub -w <dir>
```
(this uses Linux's inotify, and is thus only supported on Linux)
