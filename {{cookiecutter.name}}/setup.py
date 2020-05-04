#!/usr/bin/env python3

"""Setup file of the project."""

import setuptools  # type: ignore


META = dict(
    name="{{cookiecutter.name}}",
    version="0.1.0",
    description="TODO: Write a description",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://{{cookiecutter.control}}/{{cookiecutter.user}}/{{cookiecutter.name}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    license="{{cookiecutter.license}}",
    packages=["{{cookiecutter.name}}"],
    keywords="example package keywords",
    classifiers=["Development Status :: 4 - Beta"],
    entry_points={"console_scripts": ["{{cookiecutter.name}}={{cookiecutter.name}}.__main__:main"]},
    python_requires=">={{cookiecutter.python}}",
    install_requires=[],
)

if __name__ == "__main__":
    setuptools.setup(**META)
