#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben: MontyTagger port of montylingua 2.1`

import re
import string
import time
import MontyTokenizer
import MontyLexicalRuleParser
import MontyContextualRuleParser
import MontyLexiconFast
import MontyLemmatiser

# think about import normal word cutter and tagger in chinese corpus

class MontyTagger:
    # 
    def __init__(
        self,
        trace_p=0,
        MontyLemmatiser_handler=None
    ):
        self.montyLemmatiser_handler = MontyLemmatiser_handler or MontyLemmatiser.MontyLemmatiser()
        # word cut

        # tokenizer

        # lexicon

        # the lexicon fast

        # LRP lexicon rule parser
    
    def tag(self,text,expand_contractions_p=0,all_pos_p=0,commonsense_p=1):
        #
    
    def tag_tokenized(self,text,all_pos_p=0,commonsense_p=1):
        #
    