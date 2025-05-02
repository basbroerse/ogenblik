# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:00:29 2025

@author: basbr
"""

import spacy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def getFiles():
    #path = Path('\Code\Corpus_cleaned_21_NL\Corpus')
    path = Path.cwd()
    files = list(path.rglob('*.txt'))
    names = []
    
    for f in files:
        a = str(f)
        b = a.replace(str(path),'')
        c = b.replace('.txt','')
        d = c.replace('\\','')
        names.append(d)
    
    return files, names

def getStats(file):
    #print(file)
    nlp = spacy.load('nl_core_news_sm')
    nlp.max_length = 1100000
    doc = nlp(open(file, errors='backslashreplace').read())
    
    pos = []            # lijstje voor woordsoorten
    
    # lemma's
    lemmas = [token.lemma_ for token in doc]
    
    # woordsoorten
    for token in doc:
        pos.append(token.pos_)
    
    return lemmas, pos

def main():
    files, names = getFiles()
    
    n = len(files)
    
    for i in range(n):    
        file = files[i]
        name = names[i]
        print(name)
                
        # bepaal lemma's en woordsoorten
        lem, pos = getStats(file)
        
        # sla de lijsten op in een txt-bestand
        lem_name = '70_' + name + ' lemmas.txt'     # pas bestandsnaam aan afhankelijk van het corpus
        pos_name = '70_' + name + ' pos.txt'        # pas bestandsnaam aan afhankelijk van het corpus
        
        lem_file = open(lem_name,'w', encoding='UTF-8')
        for l in lem:
            lem_file.write(l + ' ')
        lem_file.close()
        
        pos_file = open(pos_name,'w')
        for p in pos:
            pos_file.write(p + ' ')
        pos_file.close()
        
    print('Klaar! %i boeken verwerkt' %n)
    
if __name__ == "__main__":
    main()