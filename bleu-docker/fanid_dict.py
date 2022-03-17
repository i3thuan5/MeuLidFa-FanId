from http.client import HTTPConnection
from urllib.parse import quote
import json


def fanid(fa):
    '''
    - model_id = 2  # Huâ-tâi huanik boo-hing id
      Khuànn `onmt/tsuki/conf.json`
    '''
    post_fa = []
    for tsua in fa:
        post_fa.append(''.join(tsua.split()))
    from urllib.parse import urlencode
    tsuliau = json.dumps(urlencode({
        'page_name': 'hakkadic',
        'input_lang': 'zh-tw',
        'input_txt': quote('\n'.join(post_fa))
    }))

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


fanid(['多國語言有聲版',' 多國語言有聲版'])