#!/usr/bin/env python

import setuptools  # type: ignore

info = dict(
    name="{{cookiecutter.name}}",
    version="0.1.0",
    description="TODO: write a description",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="{{cookiecutter.homepage}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    license="{{cookiecutter.license}}",
    packages=["{{cookiecutter.name}}"],
    keywords="sample development package",
    classifiers=["Development Status :: 4 - Beta"],
    entry_points={"console_scripts": ["{{cookiecutter.name}}={{cookiecutter.name}}.__main__:main"]},
    tests_require=["tox"],
    python_requires=">={{cookiecutter.python}}",
    install_requires=[],
)

if __name__ == "__main__":
    setuptools.setup(**info)
