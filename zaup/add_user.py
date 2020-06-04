#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull and contributors
# See LICENSE.md for details.

"""
Adds user/password to zaup/config.py
"""

import getpass
import hashlib
import json
import sys
from time import gmtime, strftime

try:
    import config
except ImportError:
    pass


def write_config(users, google_auth):
    with open("zaup/config.py", "w") as fp:
        fp.write("""# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull and contributors
# See LICENSE.md for details.
#
# This file should NEVER be committed into git!
# Auto-generated on: {0}

users = {1}

google_auth = {2}""".format(
    strftime("%Y-%m-%d %H:%M:%S", gmtime()),
    json.dumps(users, indent=2, sort_keys=True),
    google_auth))


if __name__ == "__main__":
    print("""
This script will add a username/password combination to 'zaup/config.py', for
use with basic authentication on the web user interface
""")
    username = input('  Enter a username: ')
    password = getpass.getpass(prompt='  Type a password: ')
    check = getpass.getpass(prompt='  Re-enter password: ')

    if password != check:
        print("\nPasswords dont match!")
        sys.exit(-1)

    if 'config' in globals():
        existing_users = config.users
        google_auth = '"{0}"'.format(config.google_auth) if hasattr(config, 'google_auth') and config.google_auth else None
    else:
        existing_users = {}
        google_auth = None
        
    existing_users[username] = hashlib.md5(bytes(password, encoding='utf-8')).hexdigest()

    write_config(existing_users, google_auth)
    print("\nzaup/config.py updated")
