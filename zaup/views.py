#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.md for details.

import qrcode
import qrcode.image.svg
import asyncio
import io
from aiohttp import web


from database import account

# https://github.com/google/google-authenticator/wiki/Key-Uri-Format
TOTP_URI = "otpauth://totp/{0}?secret={1}&issuer={2}"


class totp_qrcode(object):

    def __init__(self, secrets):
        self.secrets = secrets
        self.factory = qrcode.image.svg.SvgPathImage

    @asyncio.coroutine
    def handler(self, request):
        n = int(request.match_info.get('id'))

        uri = TOTP_URI.format(self.secrets[n][account.email],
                              self.secrets[n][account.secret],
                              self.secrets[n][account.issuer])

        output = io.BytesIO()
        img = qrcode.make(uri, image_factory=self.factory)
        img.save(output)
        data = output.getvalue()
        output.close()

        return web.Response(body=data, content_type="image/svg+xml")
