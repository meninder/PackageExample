
# 1. Overview
This project is intended to demonstrate how to package an application that is accessible via cli. A simple application that prints `Hello I am [name]` based on the cli argument.  I try to follow best practices around directory structure, although that makes the code overly complex for trying to achieve a simple objective.  I am hoping this will serve as a template for me in future projects. 

`setuptools` is the de facto standard way to facilitate packaging applications.  It builds on top of the `distutils` library, which comes with Python. 

# 2. Using this application
* Clone the project
* cd to the directory
* Create a virtual environment `virtualenv virt` and activate
`source virt/bin/activate`
* pip install .
* run: `package_example -g <NAME>`

# 3. Pre-Work: Top level Directory
## Directory structure
The files at the top level are typical and explained below.

## LICENSE file
This [website](https://choosealicense.com/)is a good place to start. If you are looking for something simple, that is permissive but does not keep you liable, use the MIT license.  Just paste it and make a couple of edits for year and name.
 
## README.md file
* [Resource](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) on how to use mark-up
* You can add this to the long_description in setup.py, be sure to also add: `long_description_content_type='text/markdown'`

## MANIFEST.in file
Needs to be created to include all other files (license, readme, etc) in the package.  Inside the file explicitly include the files needed.

## setup.py file
See the file itself for the comments, most is straightforward.

## requirements file
`pip freeze --format=freeze` returns the list of packages used in your project.  Add `> requirements.txt` to the end and this will write to a requirements file.  This allows users of the project to simply write `pip install -r requirements.txt`.  It also allows easier reference in the setup.py file.

## __init__.py
Not at the top level, but within the folder.  The `find_packages()` function of setuptools, searches application for folders for files of this type.  Python package definition is something like: a folder that contains an init.py file.  We also use packages as something that's distributed on PyPi, but that might be better described as a distribution.

You can exclude certain directories (tests directory here) by using keyword `exclude` inside the `find_packages` function.  


# 4. Package Creation
In addition to the local installation, one can package up the application for distribution through PyPi (not explored here).  There are two functions to help with that:  `python setup.py sdist` to create the distribution and to do in development mode: `python setup.py develop`

# 5. Resources and videos
* [Video](https://www.youtube.com/watch?v=j8q428a_7Is) by PACKT. Does not cover CLI, but has the other components
* [Video](https://www.youtube.com/watch?v=wCGsLqHOT2I) shows how to package AND distribute.
* [Video](https://www.youtube.com/watch?v=GaWs-LenLYE) gives a good idea on how to launch your program via CLI.