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
        self.pms = []
    def polymorh(self, cm, dsc):
        self.pms.append((cm, dsc))

    def add_sub(self, sub):
        self.sub = sub

    def add_obj(self, obj):
        self.obj = obj
    
    def find(self):
        if self.sub is not None and self.obj is not None:
            return self.sub, self.obj

class Preps(WordBase):


class Norms(WordBase):


class Attri(WordBase):


