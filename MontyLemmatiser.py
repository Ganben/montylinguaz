#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben: MontyLemmatiser port of montylingua 2.1`

import re

# think about import 

class MontyLemmatiser:
    #
    # original implt read `.mdf` file as db
    # u obviously need a bigger db file
    xtag_morph_zhcn_corpus = '' # add a real source
    exceptions_source = '' # file or db, see LEMMAEXCEPTION.MDF
    regular_any = []
    regular_verb = []
    regular_noun = []
    regular_adj = []
    regular_operators = []  # operator/operands concept
    # regular can be default option
    irregular_re_any = []
    irregular_re_verb = []
    # irregular can be tf model/db
    irregular_nouns += [

    ]
    # additional irregular nouns
    def __init__(self):
        #
        filename_str=[]
        self.regular_any,self.regular_verb,self.regular_noun,self.irregular_re_any,self.irregular_re_verbs,self.irregular_re_nouns=map(lambda the_tokenizers:map(lambda the_tokenizer_str:[re.compile('^'+the_tokenizer_str[0].lower()+'$')]+the_tokenizer_str[1:],the_tokenizers),filename_str)
        return

    def lemmatise_untagged_sentence(self,untagged):
        #

    def lemmatise_tagged_sentence(self,tagged):
        #

    
    def lemmatise_word(self,word,pos=""):

        #

    def verify_lemmatiser(self):
        #
    
    def make_verification_dictionary(self):
        #
        return

    def fix_case(self, word1, word2):
        #
        return

    def _re_match_helper(self, re_kb, word):
        #
        return

    def find_irregular_morph(self,word,pos=""):
        a1=self._re_match_helper
        groupnames1=self.find_irregular_morph
        cron_dictr=a1(self.irregular_re_any,word)

        return
    
    