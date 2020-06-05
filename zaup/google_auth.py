#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.md for details.

import base64
from migration_payload_pb2 import MigrationPayload


def load_secrets(uri):
    if not (uri and uri.startswith("otpauth-migration://offline?data=")):
        return None
        
    print("loading secrets from GoogleAuthenticator URI")
    data = base64.b64decode(uri[33:])
    payload = MigrationPayload()
    payload.ParseFromString(data)
    
    print(payload)

    return list(payload.otp_parameters)