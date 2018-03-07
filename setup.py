#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), "README.md")).read()
version = open(os.path.join(os.path.dirname(__file__), "VERSION.txt")).read().strip()

setup(
    name="zaup",
    version=version,
    author="Richard Hull",
    author_email="richard.hull@destructuring-bind.org",
    description=("TOTP authentication using ZeroSeg"),
    license="MIT",
    keywords=["raspberry pi", "rpi", "led", "max7219", "seven segment", "7 segment", "TOTP", "2 factor auth"],
    url="https://github.com/rm-hull/zaup",
    download_url="https://github.com/rm-hull/zaup/tarball/" + version,
    packages=['zaup'],
    install_requires=[
        "luma.led_matrix",
        "cchardet",
        "aiohttp",
        "aiohttp_jinja2",
        "qrcode",
        "onetimepass"
    ],
    setup_requires=["pytest-runner"],
    tests_require=["mock", "pytest", "pytest-cov", "python-coveralls"],
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: System :: Hardware",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]
)
