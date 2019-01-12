# -*- coding: utf-8 -*
import importlib
import sys
import unicodedata

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
else:
    # You don't need to encode data that is already encoded in Python 3. When you try to do that,
    # Python will first try to decode it to Unicode before it can encode it back to UTF-8.
    importlib.reload(sys)

class ParsingException(Exception):
    reason = ''
    
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return 'Error: ' + self.reason
