#!/usr/bin/env python3

"""Setup file of the project."""

import setuptools  # type: ignore


META = dict(
   name="{{cookiecutter.name}}",
   version="{{cookiecutter.version}}",
   description="{{cookiecutter.description}}",
   long_description=open("README.md", "r").read(),
   long_description_content_type="text/markdown",
   url="{{cookiecutter.url}}",
   author="{{cookiecutter.author}}",
   author_email="{{cookiecutter.email}}",
   license="{{cookiecutter.license}}",
   packages=["{{cookiecutter.name}}"],
   keywords="{{cookiecutter.keywords}}",
   classifiers=["Development Status :: {{cookiecutter.status}}"],
   entry_points={"console_scripts": ["{{cookiecutter.name}}={{cookiecutter.name}}.__main__:main"]},
   python_requires=">={{cookiecutter.python}}",
   install_requires=[],
)

if __name__ == "__main__":
    setuptools.setup(**META)
