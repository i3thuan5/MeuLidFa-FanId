from argparse import ArgumentParser
import re
import csv
import io
from urllib.request import urlopen

mai_lukdui = re.compile('（.+?）')


def main():
    for hang in ngin():
        for meu, fa in zip(
            hang['例句'].split('\n'), hang['翻譯'].split('\n')
        ):
            meu = meu.strip()
            fa = fa.strip()
            if meu:
                print(mai_lukdui.sub('', meu), fa)


def ngin():
    github_bangtsi = ('https://raw.githubusercontent.com/'
                      'i3thuan5/Elearning-Hakka/main/csv_imtong/')
    jintsing_sului = [
        f'{github_bangtsi}siw.csv',
        f'{github_bangtsi}si3-1.csv',
        f'{github_bangtsi}si3-2.csv',
    ]
    for bangtsi in jintsing_sului:
        with urlopen(bangtsi) as tong:
            with io.StringIO(tong.read().decode('utf-8')) as tsuliau:
                yield from csv.DictReader(tsuliau)


if __name__ == '__main__':
  main()
