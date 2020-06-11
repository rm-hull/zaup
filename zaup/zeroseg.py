#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.md for details.

"""
Display a TOTP code based on some stored secrets
"""

import time
import RPi.GPIO as GPIO

from luma.core.serial import spi
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219, sevensegment
from secret import get_token


def scroll_message(device, msg, delay=0.2):
    width = device.width
    padding = " " * width
    msg = padding + msg + padding
    n = len(msg)

    virtual = viewport(device, width=n, height=8)
    sevensegment(virtual).text = msg
    for i in reversed(list(range(n - width))):
        virtual.set_position((i, 0))
        time.sleep(delay)


class display(object):

    def __init__(self, loop, secrets):
        self.seg = sevensegment(max7219(spi()))
        self.secrets = secrets
        self.loop = loop
        self.current = 0

    def token(self):
        n = self.current % len(self.secrets)
        self.seg.text = "  %s" % get_token(self.secrets[n])
        last_digit = token % 10
        self.loop.call_later(0.8, self.dot, last_digit)

    def dot(self, last_digit):
        self.seg.text[7:] = str(last_digit) + "."
        self.loop.call_later(0.2, self.token)

    def message(self, next=None):
        n = self.current % len(self.secrets)
        token = get_token(self.secrets[n])
        self.seg.device.clear()
        scroll_message(self.seg.device, self.secrets[n].name)
        self.seg.text = "  %06d" % token

        if next:
            self.loop.call_soon(next)

    def next(self):
        self.current += 1
        self.loop.call_soon(self.message)

    def prev(self):
        self.current -= 1
        self.loop.call_soon(self.message)


def init(loop, secrets):

    dispatch = display(loop, secrets)

    # GPIO buttons
    import const as button
    button.a = 17
    button.b = 26

    def cb(channel):
        method = dispatch.prev if channel == button.a else dispatch.next
        loop.call_soon(method)

    def title(msg):
        dispatch.seg.text = msg

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button.a, GPIO.IN)
    GPIO.setup(button.b, GPIO.IN)
    GPIO.add_event_detect(button.a, GPIO.RISING, callback=cb, bouncetime=200)
    GPIO.add_event_detect(button.b, GPIO.RISING, callback=cb, bouncetime=200)

    loop.call_soon(title, "- ZAUP -")
    loop.call_later(3, dispatch.message, dispatch.token)
