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
from aiohttp import web

try:
    import zeroseg
except:
    pass
import database
import views


def ask_exit(signame):
    print("got signal %s: exit" % signame)
    loop.stop()


if __name__ == "__main__":

    loop = asyncio.get_event_loop()

    filename = "databases"
    secrets = database.load_secrets(filename)
    if 'zeroseg' in globals():
        zeroseg.init(loop, secrets)

    for signame in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(getattr(signal, signame),
                                functools.partial(ask_exit, signame))

    print("Event loop running forever, press Ctrl+C to interrupt.")
    print("pid %s: send SIGINT or SIGTERM to exit." % os.getpid())

    app = web.Application()
    app.router.add_get('/qr/{id}', views.totp_qrcode(secrets).handler)

    web.run_app(app, port=9000)
