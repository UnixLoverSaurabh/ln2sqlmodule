# -*- coding: utf-8 -*

import sys
import unicodedata
import importlib

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
else:
    # You don't need to encode data that is already encoded in Python 3. When you try to do that, 
    # Python will first try to decode it to Unicode before it can encode it back to UTF-8. 
    importlib.reload(sys)


class Column:
    name = ''
    type = ''
    is_primary = False
    
    def __init__(self, name=None, type=None, is_primary=None):
        if name is None:
            self.name = ''
        else:
            self.name = name
        if type is None:
            self.type = ''
        else:
            self.type = type
        if is_primary is None:
            self.is_primary = False
        else:
            self.is_primary = is_primary

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type

    def is_primary(self):
        return self.is_primary
