import re
import conllu
from functools import reduce


def get_streusle_sentences(conllulex_path):
    with open(conllulex_path, 'r', encoding="utf-8") as f:
        return reduce(lambda x, y: x + re.findall(r'text = (.*)', y.strip()),
                      f.readlines(),
                      [])


def get_streusle_tokenlists(conllulex_path):
    fields = tuple(list(conllu.parser.DEFAULT_FIELDS)
                   + ['smwe', 'lexcat', 'lexlemma', 'ss', 'ss2', 'wmwe', 'wcat', 'wlemma', 'lextag'])

    with open(conllulex_path, 'r', encoding='utf-8') as f:
        return conllu.parse(f.read(), fields=fields)
