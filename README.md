
#1. Overview
This project is intended to demonstrate how to package an application that is accessible via cli. A simple application that prints `hello [name]` based on the cli argument.  

`setuptools` is the de facto standard way to facilitate packaging applications.  It builds on top of the `distutils` library, which comes with Python. 

# 2. Pre-Work
## directory structure
README.md, setup.py, LICENSE can all sit at the top level. src folder typically contains the application code.

## Adding a license
The [website](https://choosealicense.com/) is a good place to start.  If you are looking for something simple, that is permissive but does not keep you liable, use the MIT license.  Just paste it and make a couple of edits for year and name.
 
## README.md file
* [Resource](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) on how to use mark-up
* You can add this to the long_description in setup.py, be sure to also add: `long_description_content_type='text/markdown'`

## Manifest
Needs to be created to include all other files (license, readme, etc) among other functions.  Inside the file explicitly include the files needed.

## setup.py file
See the file itself for the comments, most is straightforward.

## __init__.py
Among other things, the `find_packages()` function of setuptools, searches application for folders for files of this type.

Python package definition is something like: a folder that contains an init.py file.  We also use packages as something that's distributed on PyPi, but that might be better described as a distribution.

You can exclude certain directories (tests directory here) by using keyword `exclude` inside the `find_packages` function.  

## requirements file
`pip freeze --format=freeze` returns the list of packages used in your project.  Add `> requirements.txt` to the end and this will write to a requirements file.  This allows users of the project to simply write `pip install -r requirements.txt`.  It also allows easier reference in the setup.py file.

# 3. Running Setup
## Create a virtual environment and activate
`virtualenv virt`
`source virt/bin/activate`

## Create distribution package
`python setup.py sdist`

## Create distribution package development mode
`python setup.py develop`

## Install the package locally
cd into top level and `pip install .` You can use the flag `pip install -e .` so you can edit the source while
# 4. Resources and videos
* [Video](https://www.youtube.com/watch?v=j8q428a_7Is) by PACKT. Does not cover CLI, but has the other components
* [Video](https://www.youtube.com/watch?v=wCGsLqHOT2I) shows how to package AND distribute.
* [Video](https://www.youtube.com/watch?v=GaWs-LenLYE) gives a good idea on how to launch your program via CLI.