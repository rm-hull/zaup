#!/usr/bin/env python3

"""
Display a TOTP code based on some stored secrets
"""
__author__ = 'Richard Hull <rm_hull@yahoo.co.uk>'
__date__ = '11 September 2016'
__version_info__ = (0, 1, 0)
__version__ = '%s.%s.%s' % __version_info__
__license__ = 'MIT'

import asyncio
import functools
import os
import signal

import sqlite3
import time
import onetimepass as otp
import max7219.led as led
import RPi.GPIO as GPIO

import const as account
import const as button

# 'Account' table fields/offsets
account._id = 0
account.email = 1
account.secret = 2
account.counter = 3
account.typ = 4
account.provider = 5
account.issuer = 6
account.original_name = 7

# GPIO buttons
button.a = 17
button.b = 26


def ask_exit(signame, device):
    print("got signal %s: exit" % signame)
    device.clear()
    loop.stop()

def load_secrets(filename):
    print("Loading sqlite3 database from:", filename)
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        return list(cur.execute("SELECT * FROM accounts"))

def display_token(secrets, loop):
    global current
    n = current % len(secrets)
    token = otp.get_totp(secrets[n][account.secret])
    device.write_text(0, "  " + "%06d" % token)
    last_digit = token % 10
    loop.call_later(0.8, display_dot, secrets, last_digit, loop)

def display_dot(secrets, last_digit, loop):
    device.letter(0, led.constants.MAX7219_REG_DIGIT0, last_digit, dot=True)
    loop.call_later(0.2, display_token, secrets, loop)

def display_message(secrets):
    global current
    n = current % len(secrets)
    token = otp.get_totp(secrets[n][account.secret])
    device.clear()
    device.show_message(secrets[n][account.email], delay=0.2)
    device.write_text(0, "  " + "%06d" % token)

def update(secrets, loop, channel):
    global current
    delta = -1 if channel == button.a else +1
    current = current + delta
    loop.call_soon(display_message, secrets)

def init_gpio(callback):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button.a, GPIO.IN)
    GPIO.setup(button.b, GPIO.IN)
    GPIO.add_event_detect(button.a, GPIO.RISING, callback=callback, bouncetime=200)
    GPIO.add_event_detect(button.b, GPIO.RISING, callback=callback, bouncetime=200)

current = 0

path = os.path.dirname(os.path.abspath(__file__))
filename = path + "/databases"

device = led.sevensegment()
secrets = load_secrets(filename)
loop = asyncio.get_event_loop()
init_gpio(functools.partial(update, secrets, loop))

for signame in ('SIGINT', 'SIGTERM'):
    loop.add_signal_handler(getattr(signal, signame),
                            functools.partial(ask_exit, signame, device))

print("Event loop running forever, press Ctrl+C to interrupt.")
print("pid %s: send SIGINT or SIGTERM to exit." % os.getpid())

loop.call_soon(display_message, secrets)
loop.call_soon(display_token, secrets, loop)

try:
    loop.run_forever()
finally:
    loop.close()
