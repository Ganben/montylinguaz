#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben: commonsense port of montylingua 2.1`


class MontyCommonsense:
    dbname = '' #u obviously need a big db or graph or nosql
    
    def __init__(
        self,
        montyLemmatiser_handler = None,
        montyTagger_handler = None):
        # the lemmatiser
        # the tagger

        this.montyLemmatiser_handler = montyLemmatiser_handler or MontyLemmatiser.MontyLemmatiser()
        # 
        this.montyTagger_handler = montyTagger_handler or MontyTagger.MontyTagger()
        #
        
