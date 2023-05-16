#! /usr/bin/env python3

# Packages
from setuptools import setup

setup(
    name="fancify-text",
    version="0.2.3",
    author="Secret-chest",
    url="https://github.com/Secret-chest/fancify-text",
    description=(
        "Convert text to one of 27 fancy unicode representations"
    ),
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    packages=["fancify_text"],
    install_requires=[],
    entry_points = {
        'console_scripts': [
            'fancify = fancify_text.cli:fancify_cmd'
        ]
    },
)
