#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben: commonsense port of montylingua 2.1`


class MontyCommonsense:
    dbname = '' #u obviously need a big db or graph or nosql
    # cssdb.mdf = 
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
        
        return

    def cs_verify_tagged(self, tagged):
        #verify with hostnames_dict, 
        # in ['VBD', 'VBG'] tags etc.
        
        info1=' '.join(map(lambda tagged_cleaned:tagged_cleaned[0]+'/'+tagged_cleaned[1],map(lambda tmps:tmps.split('/'),cmp1)))
        
        return info1

    def unpp(self,pp):
        cmp1 = pp.strip(' ()\n').split()

        return

    def build_cs_selection_db(self):

        return
    
    def setitem(self,dict,key,value):
        # seems useles?
        dict[key] = value