#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.md for details.

import qrcode
import qrcode.image.svg
import asyncio
import io
from aiohttp import web
import aiohttp_jinja2
import onetimepass as otp
from base64 import b32encode
import json
import time

from database import account

# https://github.com/google/google-authenticator/wiki/Key-Uri-Format
TOTP_URI = "otpauth://totp/{0}?secret={1}&issuer={2}"


class totp(object):

    def __init__(self, secrets):
        self.factory = qrcode.image.svg.SvgPathImage
        self.secrets = secrets

    def _get_secret(self, request):
        n = int(request.match_info.get('id'))
        if 0 <= n < len(self.secrets):
            return self.secrets[n]
            
    def _get_token(self, secret):
        encoded_secret = b32encode(secret.secret)
        return '{0:06d}'.format(otp.get_totp(encoded_secret))

    async def qrcode(self, request):
        secret = self._get_secret(request)
        if secret is None:
            return web.Response(status=404)

        uri = TOTP_URI.format(secret.name,
                              b32encode(secret.secret),
                              secret.issuer)

        output = io.BytesIO()
        img = qrcode.make(uri, image_factory=self.factory)
        img.save(output)
        data = output.getvalue()
        output.close()
        return web.Response(body=data, content_type="image/svg+xml")

    async def tokens(self, request):
        tokens = [self._get_token(secret) for secret in self.secrets]
        time_left = 30 - int(time.time()) % 30
        result = dict(tokens=tokens, timeLeft=time_left)
        return web.Response(body=json.dumps(result), content_type="application/json")
        
    @aiohttp_jinja2.template('index.html')
    async def index(self, request):
        return {'secrets': list(enumerate(self.secrets))}
