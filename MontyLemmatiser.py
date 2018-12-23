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

    