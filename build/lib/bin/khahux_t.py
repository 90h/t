# coding: utf-8

import json
from distutils.log import warn as printf
import sys
try:
    from urllib import urlencode
    from urllib2 import Request, urlopen
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen


URL = 'http://fanyi.youdao.com/openapi.do'
KEY = 1132608537
KEYFROM = 'khahux'

CODE_MSG_MAP = {
    20: '要翻译的文本过长',
    30: '无法进行有效的翻译',
    40: '不支持的语言类型',
    50: '无效的key',
    60: '无词典结果，仅在获取词典结果生效'
}


def get_translate(q):
    url = URL
    param = {
        'keyfrom': KEYFROM,
        'key': KEY,
        'type': 'data',
        'doctype': 'json',
        'version': '1.1',
        'q': q
    }
    url += '?' + urlencode(param)
    req = Request(url)
    res = urlopen(req)
    return json.loads(res.read().decode('utf-8'))


def show_json(json_data):
    error_code = json_data.get('errorCode')
    if error_code != 0:
        return printf("""
    [{}]{}
        """.format(error_code, CODE_MSG_MAP.get(error_code)))

    query = json_data.get('query')
    translations = json_data.get('translation')
    printf('\n[{}]: {}'.format(query, ', '.join(translations)))

    basic = json_data.get('basic')
    if basic and isinstance(basic, dict):
        phonetic = basic.get('phonetic', None)
        uk = basic.get('uk-phonetic', None)
        us = basic.get('us-phonetic', None)
        explains = basic.get('explains', [])
        printf('[phonetic] {}, [us] {}, [uk] {}'.format(phonetic, uk, us))
        printf('\n')
        printf(', '.join(explains))

    web = json_data.get('web')
    if web and isinstance(web, list):
        for item in web:
            printf('{0}: {1}'.format(item['key'], ','.join(item['value'])))

    printf('\n')


def main():
    if not len(sys.argv) > 1:
        return printf("""
    Usage:
    khahux_t <word>
        """)

    q = ' '.join(sys.argv[1:])
    json_data = get_translate(q)
    show_json(json_data)


if __name__ == '__main__':
    main()
