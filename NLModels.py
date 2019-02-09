#!/usr/bin/python3
# -*- coding:utf-8 -*-

import json

class WordBase:
    # serilizaer
    # id
    # category name
    def __init__(self, id, cat_name, c):
        self.id = id
        self.cat = cat_name
        self.c = c
    
    @property
    def json(self):
        return json.dumps(
            { 'id': self.id,
            'cat': self.cat,
            'c': c
            })

class Verbs(WordBase):
    # 
    def __init__(self, id, cat, c):
        super.__init__(self, id, cat, c)
        self.polys = []
        self.ad = []
    def polymorh(self, cm, dsc):
        self.polys.append((cm, dsc))
    
    def add_ad(self, ads):
        for el in ads:
            self.ad.append(el)
        return
    
    def add_sub(self, sub):
        self.sub = sub
        return

    def add_obj(self, obj):
        self.obj = obj
    
    @property
    def graph(self):
        # add a graph obj
        if self.sub is not None and self.obj is not None:
            return self.sub, self.obj

    def execute(self, env_dict):
        # execute the verb to env vars

        # 1. query verb's operator and script

        # 2. running script(where? in a VM or ? data object?)

        # 3. update env



class Preps(WordBase):


class Norms(WordBase):


class Attri(WordBase):


