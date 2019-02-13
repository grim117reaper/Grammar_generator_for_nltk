#imports
import os
import nltk

#grammar finding function
def grammar(sentences , phrase):

    No_sen = len(sentences) #findng number of sentences

    #tokenizing
    token = []
    for i in sentences:
        token.append(nltk.word_tokenize(i))

    #tagging
    tagged = []
    for i in token:
        tagged.append(nltk.pos_tag(i))

    #finding different parts of speech
    k = 0
    l = [[] for i in range(No_sen)] #creating a list for tagged elements
    for i in tagged:
        for j in i:
            l[k].append(j[1])
        k = k + 1

    #finding unique parts of speech
    g = []
    for i in l:
        for j in i:
            if j not in g:
                g.append(j)

    #generating grammar parts
    gr = []
    for i in g:
        gr.append("<" + i + ">")

    #creatng the final grammar
    grammar = phrase +" : {("
    for i in gr:
        grammar = grammar + i + "*"
    grammar = grammar + ")*} # " + phrase

    return grammar #returning final grammar
