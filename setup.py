#!/usr/bin/env python

from distutils.core import setup, Extension

setup(
    name="zaup",
    version="0.2.0",
    author="Richard Hull",
    author_email="richard.hull@destructuring-bind.org",
    description=("TOTP authentication using ZeroSeg"),
    license="MIT",
    keywords=["raspberry pi", "rpi", "led", "max7219", "seven segment", "7 segment", "TOTP", "2 factor auth"],
    url="https://github.com/rm-hull/zaup",
    download_url="https://github.com/rm-hull/zaup/tarball/0.2.0",
    packages=['zaup'],
    install_requires=["RPi.GPIO", "max7219", "onetimepass"]
)
