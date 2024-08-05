# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:37:09 2024

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
    
    lengtes  = []       # lijst voor zinslengtes
    dep_lens = []       # lijstje voor afstanden tussen hoofden en kinderen
    pos = []            # lijstje voor woordsoorten
    
    # zinnen
    zinnen = list(doc.sents)

    for zin in zinnen:
        x = len(zin)
        lengtes.append(x)
    
    # tokens en lemma's
    tokens = [token.text for token in doc]
    lemmas = [token.lemma_ for token in doc]
    unique_lems = list(set(lemmas))
    
    # dependency length
    for token in doc:
        for child in token.children:
            dep_lens.append(abs(token.i - child.i))
    
    # woordsoorten
    for token in doc:
        pos.append(token.pos_)
    
    return lengtes, tokens, unique_lems, dep_lens, pos

def main():
    #path = r'C:\\Users\\basbr\\OneDrive\\Documenten\\Studie\\Redacteur-editor\\4 Scriptie\\Code\\Corpus_cleaned_70'
    zinnen_out = 'zinnen.csv'
    tokens_out = 'tokens.csv'
    lemmas_out = 'lemmas.csv'
    dependencies_out = 'dependencies.csv'
    pos_out = 'pos.csv'

    files, names = getFiles()
    
    zinslengtes = []        # lijst om alle zinslengtes op te slaan per boek
    tokens = []
    lemmas = []
    dependencies = []
    wosos = []
    
    n = len(files)
    
    for i in range(n):    
        file = files[i]
        name = names[i]
        print(name)
        
        zin, tok, lem, dep, pos = getStats(file)
        zinslengtes.append(zin)
        tokens.append(tok)
        lemmas.append(lem)
        dependencies.append(dep)
        wosos.append(pos)
    
    # gegevens opslaan 
    dfZ = pd.DataFrame(zinslengtes, index=names)
    dfT = pd.DataFrame(tokens, index=names)
    dfL = pd.DataFrame(lemmas, index=names)
    dfD = pd.DataFrame(dependencies, index=names)
    dfP = pd.DataFrame(wosos, index=names)
    
    dfZ.to_csv(zinnen_out)
    dfT.to_csv(tokens_out)
    dfL.to_csv(lemmas_out)
    dfD.to_csv(dependencies_out)
    dfP.to_csv(pos_out)
    
    '''
    df = pd.DataFrame((zinslengtes,tokens,lemmas,basic_words), index=['zinslengtes','tokens','lemmas','basic_words'],columns=names).transpose()
    
    with pd.ExcelWriter(file_out) as writer:
        df.to_excel(writer)
    '''
        
    print('Klaar! %i boeken verwerkt' %n)
    
if __name__ == "__main__":
    main()