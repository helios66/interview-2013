__author__ = 'fdamilola'

import base64

#scanning qrcode image resulted in a base64 encoded string

s = """Base 64 string. Redacted for some weird reason by me"""

print base64.decodestring(s)