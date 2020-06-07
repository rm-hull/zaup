#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.md for details.

import sqlite3
from base64 import b32decode

import const as account
from migration_payload_pb2 import MigrationPayload

# 'Account' table fields/offsets
account._id = 0
account.email = 1
account.secret = 2
account.counter = 3
account.typ = 4
account.provider = 5
account.issuer = 6
account.original_name = 7


def _convert(row):
    secret = MigrationPayload.OtpParameters()
    secret.name = row[account.email]
    secret.issuer = row[account.issuer]
    secret.secret = b32decode(row[account.secret].upper())
    secret.type = MigrationPayload.OtpType.OTP_TYPE_TOTP
    secret.counter = row[account.counter]
    secret.digits = MigrationPayload.DigitCount.DIGIT_COUNT_SIX
    return secret
    

def load_secrets(filename):
    print("Loading sqlite3 database from:", filename)
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        return [_convert(row) for row in cur.execute("SELECT * FROM accounts")]
