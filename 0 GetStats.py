# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:37:09 2024

@author: basbr
"""
import spacy
import pandas as pd
from pathlib import Path

def getFiles():
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
    nlp = spacy.load('nl_core_news_sm')
    nlp.max_length = 1100000
    
    doc = nlp(open(file, errors='backslashreplace', encoding='UTF-8').read())
    
    lengtes  = []       # lijst voor zinslengtes
    dep_lens = []       # lijst voor afstanden tussen hoofden en kinderen
    pos = []            # lijst voor woordsoorten
    
    # zinnen
    zinnen = list(doc.sents)

    for zin in zinnen:
        x = len(zin)
        
        if not (zin[0].pos_ == 'SPACE' or zin[0].text == '‘' or zin[0].text == '’'):
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
        
    print('Klaar! %i boeken verwerkt' %n)
    
if __name__ == "__main__":
    main()
