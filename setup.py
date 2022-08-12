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
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["fancify_text"],
    install_requires=[],
    scripts=[
        "fancify-circled", "fancify-curly", "fancify-wiry", "fancify-bolditalicserif", "fancify-italicserif",
        "fancify-boxed", "fancify-squared", "fancify-wide", "fancify-parenthesized", "fancify-cursive",
        "fancify-bold", "fancify-reversed", "fancify-upsidedown",
        "fancify-blue", "fancify-boldfraktur", "fancify-bolditalic", "fancify-italic",
        "fancify-smallcaps", "fancify-currency", "fancify-monospaced", "fancify-boldserif",
        "fancify-sansserif", "fancify-cool", "fancify-doublestruck", "fancify-magic", "fancify-heavycircled",
        "fancify-fraktur"
    ],
)
