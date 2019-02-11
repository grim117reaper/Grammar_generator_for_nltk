#!/usr/bin/env python
import os
import nltk

sentences = ["loss of hair","bad mayocardial infractions"]

token = []
for i in sentences:
    token.append(nltk.word_tokenize(i))

tagged = []
for i in token:
    tagged.append(nltk.pos_tag(i))

k = 0
l = [[],[],[],[],[],[]]
for i in tagged:
    for j in i:
        l[k].append(j[1])
    k = k + 1

g = []

for i in l:
    for j in i:
        if j not in g:
            g.append(j)

gr = []
for i in g:
    gr.append("<" + i + ">")

grammar = "NP: {("
for i in gr:
    grammar = grammar + i + "*"
grammar = grammar + ")*} # NP "
