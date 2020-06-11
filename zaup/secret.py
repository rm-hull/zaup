#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017-2020 Richard Hull and contributors
# See LICENSE.md for details.

import onetimepass as otp
from base64 import b32encode


def get_token(secret):
    encoded_secret = b32encode(secret.secret)
    return '{0:06d}'.format(otp.get_totp(encoded_secret))
