# MIN
* *min*imal manpages
* providing you with the 80/20 of how many unix commands are used, for whenever you've forgotten how to use `find` or `grep` for the 3rd time this week

[![demo](https://asciinema.org/a/XnrGtDVrAqIBQTH9xosKOCamf.png)](https://asciinema.org/a/XnrGtDVrAqIBQTH9xosKOCamf?autoplay=1)

# Installation
* available from pypi via `pip install miniman`

# Usage
* contains minpages for unix commands, as well as more general explainer pages for important topics in the unix workflow (e.g. file, filesystem)

## Unix commands
* run `min` to get a list of all available minpages for bash commands
* run `min command` to get the minpage for bash command `command`
* e.g. `min grep` to get the minpage for `grep`

## Unix Topics
* run `min -t` to get a list of all available minpages for unix topics
* run `min -t topic` to get the minpage for unix topic `topic`
* e.g. `min -t filesystem` to the minpage for `filesystem`

# Contribute
Obviously, this is a work in progress.
Although I use many of these commands in my daily workflow, I am nowhere near understanding all the ins and outs.
So please open up an issue if I've gotten anything wrong. Thanks in advance.

Also there are more things I'd like to do with this project:
* add a search function where you can just search for a string pattern among all minpages, and get returned relevant results (i.e. grepping among all minpages)
* add additional useful commands
* add additional useful topics (e.g. 80/20 regexp, interactive bash [things like <(command), !:n/!^/!$, piping, difference between '' and "", ...], vim, ...)
* unify the sections in the commands/topics so that everyone can always have clear expectations of what to expect from a `min` page
* maybe go for some more advanced markup, to do highlights, bolding, etc.

If you could see yourself contributing to any of that, just open up an issue at [https://github.com/mleue/min/issues](https://github.com/mleue/min/issues). I'd be delighted.
