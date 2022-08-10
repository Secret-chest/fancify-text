#! /usr/bin/env python3

# Packages
from setuptools import setup

setup(
    name="fancify-text",
    version="0.1.2",
    author="Robin Winslow",
    author_email="robin@robinwinslow.co.uk",
    url="https://github.com/nottrobin/fancify-text",
    description=(
        "Convert text to one of 25 fancy unicode representations"
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["fancify_text"],
    install_requires=[],
    scripts=[
        "fancify-bold",
        "fancify-italics",
        "fancify-bolditalics",
        "fancify-monospaced",
        "fancify-typewriter",
        "fancify-serif",
        "fancify-handwriting",
        "fancify-formal",
        "fancify-blue",
        "fancify-squared",
        "fancify-circled",
        "fancify-smallcaps",
        "fancify-handwriting2",
        "fancify-reverse",
        "fancify-upsidedown",
        "fancify-wiry",
        "fancify-script",
        "fancify-outline",
        "fancify-curly",
        "fancify-apothecary",
        "fancify-magic",
        "fancify-magic2",
        "fancify-strange",
        "fancify-parenthesized",
        "fancify-boxed",
    ],
)
