#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.md for details.

import sqlite3

import const as account

# 'Account' table fields/offsets
account._id = 0
account.email = 1
account.secret = 2
account.counter = 3
account.typ = 4
account.provider = 5
account.issuer = 6
account.original_name = 7


def load_secrets(filename):
    print("Loading sqlite3 database from:", filename)
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        return list(cur.execute("SELECT * FROM accounts"))
