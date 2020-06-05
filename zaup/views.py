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

from database import account

# https://github.com/google/google-authenticator/wiki/Key-Uri-Format
TOTP_URI = "otpauth://totp/{0}?secret={1}&issuer={2}"


class totp(object):

    def __init__(self, secrets):
        self.factory = qrcode.image.svg.SvgPathImage
        # self.secrets = []
        # for s in secrets:
        #     row = list(s)
        #     email = row[account.email]
        #     if ':' in email:
        #         row[account.email] = email.split(':')[1]

        #     self.secrets.append(row)

        self.secrets = secrets #sorted(self.secrets, key=lambda s: s[account.email])


    def _get_secret(self, request):
        n = int(request.match_info.get('id'))
        matches = [s for s in self.secrets if s[account._id] == n]
        if len(matches) == 0:
            return None

        return matches[0]

    async def qrcode(self, request):
        secret = self._get_secret(request)
        if secret is None:
            return web.Response(status=404)

        uri = TOTP_URI.format(secret[account.email],
                              secret[account.secret],
                              secret[account.issuer])

        output = io.BytesIO()
        img = qrcode.make(uri, image_factory=self.factory)
        img.save(output)
        data = output.getvalue()
        output.close()
        return web.Response(body=data, content_type="image/svg+xml")

    async def token(self, request):
        secret = self._get_secret(request)
        if secret is None:
            return web.Response(status=404)

        token = '{0:06d}'.format(otp.get_totp(secret[account.secret]))
        return web.Response(body=token, content_type="text/plain")

    @aiohttp_jinja2.template('index.html')
    async def index(self, request):
        return {'secrets': self.secrets, 'account': account}
