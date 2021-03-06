# Zaup
[![Maintenance](https://img.shields.io/maintenance/yes/2020.svg?maxAge=2592000)]()

TOTP authentication using [ZeroSeg](https://thepihut.com/products/zeroseg) and Web.

Zaup uses the same sqlite3 database format as [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_GB);
this means that if you can copy the database file from your android device (see
references for links on how to do this) onto a Raspberry Pi, then you can use
your Pi (or a web browser) to display your existing TOTP 2-factor-authentication codes.

## Requirements

Zaup is a 21st-century Python app, and as such requires Python3.

TOTP authentication requires an accurate time source to operate correctly: The
Raspberry Pi must either be connected to the internet to sync against an NTP
server or should employ the use of a RTC add-on board.

```diff
- Always keep your Raspberry Pi secure: change the default password, especially
- as the authenticator database has TOTP secrets that could be used to compromise
- your online accounts.
```

## Setup / installation

On your Raspberry Pi:

    $ git clone https://github.com/rm-hull/zaup.git
    $ cd zaup
    $ sudo apt-get install python3-pip
    $ sudo pip3 install -r requirements.txt

Next, assuming you have managed to grab a copy of
`/data/data/com.google.android.apps.authenticator2/databases/databases` from
your android device, copy this file to the **zaup** directory. It is generally
a good idea to lock down the file permissions:

    $ chmod og-rwx databases

Next, check that the database content is as expected:

    $ sqlite3 ./databases

    sqlite> pragma table_info(accounts);
    0|_id|INTEGER|0||1
    1|email|TEXT|1||0
    2|secret|TEXT|1||0
    3|counter|INTEGER|0|0|0
    4|type|INTEGER|0||0
    5|provider|INTEGER|0|0|0
    6|issuer|TEXT|0|NULL|0
    7|original_name|TEXT|0|NULL|0

    sqlite> select * from accounts;
    1|Google:fred@example.com|sdfsdfsdfsdfsfsdfsfsfsdfsfs|0|0|0|Google|Google:fred@example.com
    2|Google:jim@example.com|weqeqwewqeqeqweqwewqeqeqewq|0|0|0|Google|Google:jim@example.com
    3|github.com/alice|hfhfghfhfhfghf|0|0|0|GitHub|github.com/alice

    sqlite> ^D
    $

_Obviously, your database records will be different to the made-up ones shown
above._

## Running ZAUP

If you want **zaup** to start automatically when the Raspberry Pi is booted,
add the following to the `/etc/rc.local` file _before_ the `exit 0` line
(obviously pick the correct directory, based on where you cloned the repo):

    /home/pi/zaup/zaup/main.py &

else, to just run it on the command-line, enter the following in the _zaup_
directory:

    $ ./zaup/main.py

Cycle through the list of different authenticator codes using the PREV and NEXT
buttons on the ZeroSeg. Observe the flashing dot which indicates the program
is continuously running.

## Starting a Web Server

If you want to use **Zaup** through it's web interface, you must first run a script
to add one or more user/password combinations - the app is protected by a basic
authentication scheme. From the _zaup_ directory, enter the following:


    $ ./zaup/add_user.py

    This script will add a username/password combination to 'zaup/config.py', for
    use with basic authentication on the web user interface

      Enter a username: jeff
      Type a password: ******
      Re-enter password: ******

    zaup/config.py updated

The `add_user.py` script can be run multiple times to add more users.

Start the web server as follows:

    $ ./zaup/main.py
    Loading sqlite3 database from: databases
    Event loop running forever, press Ctrl+C to interrupt.
    pid 98617: send SIGINT or SIGTERM to exit.
    ======== Running on http://0.0.0.0:9000 ========
    (Press CTRL+C to quit)

The server runs on port 9000, and can be terminated by pressing _Ctrl-C_. Any users
attempting to connect will be challenged with an authentication request.

## TODO

* Config settings for systemd startup
* ability to add secrets
* Demo video
* Improve error handling when no database file / no records
* Add countdown timer for web-view

## References

* https://thepihut.com/products/zeroseg
* http://www.howtogeek.com/130755/how-to-move-your-google-authenticator-credentials-to-a-new-android-phone-or-tablet/
* https://dpron.com/3-ways-to-move-google-authenticator/

## License

### MIT License

Copyright (c) 2017-18 Richard Hull and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
