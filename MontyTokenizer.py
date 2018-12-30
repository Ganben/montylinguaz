##!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben: MontyTokenizer port of montylingua 2.1`

class MontyTokenizer:

    def __init__(self):
        pass
    
    @classmethod
    def split_paragraphs(cls, text):
        # original: plain regrex split
        info1 = re.split('[\n]+', text)
        # substitue: TBD
        return
    
    @classmethod
    def split_sentences(cls, text):
        # original: re split by . ! ? etc.
        return
    
    @classmethod
    def tokenize(cls, sentence, expand_contractions_p=0):
        # commonsense = common abbrev and acros
        # a big dictionary and, symbols
        # can be use a external cutter
        return
