from http.client import HTTPConnection
from urllib.parse import urlencode
from urllib.parse import quote
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
    print('tsuliau',tsuliau)
    print('giedgo', giedgo)
    huein = json.loads(giedgo)
    print('\033[94m', huein)
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
    gied = dataraw(['多國語言有聲版',' 多國語言有聲版'])
    print(gied)
    # fanid(['多國語言有聲版',' 多國語言有聲版'])