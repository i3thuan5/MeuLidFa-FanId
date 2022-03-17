import argparse
from http.client import HTTPConnection
from urllib.parse import urlencode
import json


def fanid(fa):
    tsuliau = dataraw(fa)

    lian = HTTPConnection('ai49.gohakka.org', port=80)
    header = {
        "Accept": "*/*",
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Origin': 'http://ai49.gohakka.org',
        'Referer': 'http://ai49.gohakka.org/',
    }
    lian.request("POST", "/py/translate.py", tsuliau, header)
    giedgo = lian.getresponse().read()
    huein = json.loads(giedgo)
    return huein['output']


def dataraw(fa):
    post_fa = []
    for tsua in fa:
        post_fa.append(''.join(tsua.split()))
    return urlencode({
        'page_name': 'hakkadic',
        'input_lang': 'zh-tw',
        'input_txt': '\n'.join(post_fa)
    })


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Jī-bōo tsuán su-siá.')
    parser.add_argument("fa", help="Fa-ngi txt")
    parser.add_argument('meu', help='Meu-lid txt')
    args = parser.parse_args()

    with open(args.fa) as fa_dong:
        with open(args.meu, 'w') as meu_dong:
            print(
                fanid(fa_dong.readlines()),
                file=meu_dong
            )
