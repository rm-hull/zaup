# Zaup
TOTP authentication using ZeroSeg

Zaup uses the same sqlite3 database format as [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_GB); 
this means that if you can copy the `/data/data/com.google.android.apps.authenticator/databases/databases`
file from your android device (see references for links on how to do this) onto a Raspberry Pi, then you use
your Pi to display TOTP 2-factor-authentication codes.
 
## Requirements

Zaup is a 21st-century Python app, and as such requires Python3.

## Setup / installation

On your Raspberry Pi:

    $ git clone https://github.com/rm-hull/zaup.git
    $ cd zaup
    $ sudo apt-get install python-pip3
    $ pip3 install -f requirements.txt

Next, assuming you have managed to grab a copy of `/data/data/com.google.android.apps.authenticator/databases/databases` 
from your android device, copy this file to the **zaup** directory. It is generally a good idea to lock down the
file permissions:

    $ chmod og-rwx databases
    
Next, check that the database content is as expected:

    $ sqlite ./databases
    
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

_Obviously, your database records will be different to the made-up ones shown above._

If you want **zaup** to start automatically when the Raspberry Pi is booted, run the following:

    $ sudo -s
    # echo "nohup `pwd`/zaup.py &" >> /etc/rc.local
    # exit
    $


## References

* http://www.howtogeek.com/130755/how-to-move-your-google-authenticator-credentials-to-a-new-android-phone-or-tablet/
* https://dpron.com/3-ways-to-move-google-authenticator/

## License

### MIT License

Copyright (c) 2016 Richard Hull

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
