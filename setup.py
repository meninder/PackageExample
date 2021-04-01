from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read() #TODO: create readme.md file, add this step into the readme

setup(
    name="package_example",
    version="1.0.0",
    description="Toy example of how you create a deploy a package and leverage using a CLI command",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Meninder Purewal",
    author_email='meninder.purewal@gmail.com',
    url='https://github.com/meninder/',
    license="MIT", #TODO: add license, add step into README
    packages=find_packages(exclude=('tests*', 'cli*', )),
    entry_points= {
        'console_scripts': [
            #'package_example = src.greeting:greet'
            'package_example = src.cli.cli_greeting:main'
        ]
    }

    #install_requires=



)