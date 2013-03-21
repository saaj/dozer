try:
    string_types = (str, unicode)
except NameError:
    # Python 3.x
    string_types = str


def asbool(obj):
    # Copied from paste.util.converters
    # (c) 2005 Ian Bicking and contributors; written for Paste
    # (http://pythonpaste.org).  Licensed under the MIT license:
    # http://www.opensource.org/licenses/mit-license.php
    if isinstance(obj, string_types):
        obj = obj.strip().lower()
        if obj in ['true', 'yes', 'on', 'y', 't', '1']:
            return True
        elif obj in ['false', 'no', 'off', 'n', 'f', '0']:
            return False
        else:
            raise ValueError("String is not true/false: %r" % obj)
    return bool(obj)
