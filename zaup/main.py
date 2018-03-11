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
from aiohttp_basicauth_middleware import basic_auth_middleware
import aiohttp_jinja2
import jinja2
import hashlib
import sys

try:
    import zeroseg
except ImportError:
    pass

try:
    import config
except ImportError:
    print("No configuration found, run: zaup/add-user.py")
    sys.exit(-1)

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

    view = views.totp(secrets)
    app = web.Application()
    app.router.add_get('/', view.index)
    app.router.add_get('/token/{id}', view.token)
    app.router.add_get('/qr-code/{id}', view.qrcode)
    app.router.add_static('/assets/', path='zaup/public')
    app.middlewares.append(basic_auth_middleware(
        ['/'], config.users,
        lambda x: hashlib.md5(bytes(x, encoding='utf-8')).hexdigest()))

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('zaup/templates'))
    web.run_app(app, port=9000)
