#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.md for details.

"""
Display a TOTP code based on some stored secrets
"""

import os
import asyncio
import functools
import signal

import zeroseg
import database


def ask_exit(signame):
    print("got signal %s: exit" % signame)
    loop.stop()


if __name__ == "__main__":
    filename = "databases"
    secrets = database.load_secrets(filename)
    loop = asyncio.get_event_loop()
    zeroseg.init(loop, secrets)

    for signame in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(getattr(signal, signame),
                                functools.partial(ask_exit, signame))

    print("Event loop running forever, press Ctrl+C to interrupt.")
    print("pid %s: send SIGINT or SIGTERM to exit." % os.getpid())

    try:
        loop.run_forever()
    finally:
        loop.close()
