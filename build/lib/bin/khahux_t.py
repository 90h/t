# coding: utf-8

"""khahux_t CLI

Usage:
    khahux_t.py <word>
"""

import json
from distutils.log import warn as printf
try:
    from urllib import urlencode
    from urllib2 import Request, urlopen
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen


KEY = 1132608537
KEYFROM = 'khahux'


def get_translate(word):
    url = 'http://fanyi.youdao.com/openapi.do'
    param = {
        'keyfrom': KEYFROM,
        'key': KEY,
        'type': 'data',
        'doctype': 'json',
        'version': '1.1',
        'q': word
    }
    url += '?' + urlencode(param)
    req = Request(url)
    res = urlopen(req)
    return json.loads(res.read().decode('utf-8'))

def show_json(json_data):
    query = json_data.get('query')
    translation_list = json_data.get('translation')
    printf('[' + query +']' + ': ' + ', '.join(translation_list))

def main():
    from docopt import docopt
    args = docopt(__doc__, version='ktd')
    word = args.get('<word>')
    json_data = get_translate(word)
    show_json(json_data)


if __name__ == '__main__':
    main()

