# Backend Python API
Contributors: Andrew Heckman, Jon Brooks

# Setup Development Environment
Python uses Virtual Environments to help make
development easier and to better manage
dependency conflicts. It's kind of like
node_modules in Nodejs projects, but
needs a little more setup across systems
### On windows:
```
> python3 -m venv .venv
> .\.venv\Scripts\activate
> python3 -m pip install -r requirements.txt
```
### On Linux/MacOS:
```
$ python3 -m venv .venv
$ source .venv/bin/activate # zsh, csh, fish also supported
$ python3 -m pip install -r requirements.txt
```
### check to see if it works:
`python3 -m flask --app api run`
or
`python3 ./api.py`
or
`./api.py`
after you're done, and don't want to be in the virtual env anymore
use the command "deactivate"

# Folder Structure
- ./documents: project documentation and meeting notes
- ./tests: unit tests
- ./src: python source code
- ./db: database file and schema file location
- ./README.md: you are here
- ./requirements.txt: dependencies for python
- ./api.py: main file
