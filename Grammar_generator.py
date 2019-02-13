#!/usr/bin/env python

#imports
import os
import helper

file_name = input("enter the text file name : ") #getting the input file name

if "." not in file_name: #adding the correct format at the end of the filename
    file_name = file_name + ".txt"
else:
    if ".txt" not in file_name:
        index = file_name.find(".")
        file_name = file_name[0:index]
        file_name = file_name + ".txt"

file = open(file_name , "r+") #reading input file

sentences = file.readlines() #reading lines

phrase = input("name of phrase\n") #getting phrase name

grammar = helper.grammar(sentences , phrase)

print(grammar) #printing grammar
