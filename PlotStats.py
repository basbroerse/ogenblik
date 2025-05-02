# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:43:49 2024

@author: basbr
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def scatterPlot(stat1,stat2,title,x,y,label_a='Jaren 70',label_b='Modern'):
    plt.scatter(stat1[0],stat2[0], label=label_a)
    plt.scatter(stat1[1],stat2[1], label=label_b)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend()
    plt.show()

def boxPlot(stat,title,label_a='Jaren 70',label_b='Modern'):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.boxplot((stat[0],stat[1]), labels=[label_a,label_b])
    plt.show()

def histPlot(stat,title,label_a='Aantal woorden',label_b='Aantal zinnen'):
    x, y = np.unique(stat,return_counts=True)
    
    plt.bar(x,y)
    plt.title(title)
    plt.show()
    
def sentDistr():    
    zin70 = '70zinnen.csv'
    zin10 = '10zinnen.csv'
     
    data_z70 = pd.read_csv(zin70,index_col=0)
    data_z10 = pd.read_csv(zin10,index_col=0)
    
    m = len(data_z70)
    n = len(data_z10)
    
    for i in range(m):
        boek = data_z70.iloc[i].dropna()
        histPlot(boek,boek.name)
    
    for j in range(n):
        boek = data_z10.iloc[j].dropna()
        histPlot(boek,boek.name)

def main():
    file_in = 'Results.xlsx'
   
    tables  = pd.read_excel(file_in, sheet_name=None)
    sheets = list(tables.keys())
        
    df70 = tables[sheets[0]]
    df10 = tables[sheets[1]]
    
    # zinslengte: scatterplots van de gemiddelden tegen boeklengte, standaardeviatie en modus, en boxplots van gemiddelde, mediaan, modus en standaarddeviatie 
    scatterPlot((df70.loc[:,'z_mean'],df10.loc[:,'z_mean']),(df70.loc[:,'tokens'],df10.loc[:,'tokens']),'Zinslengte','Gemiddelde zinslengte','Boeklengte in tokens')
    scatterPlot((df70.loc[:,'z_mean'],df10.loc[:,'z_mean']),(df70.loc[:,'z_std'],df10.loc[:,'z_std']),'Zinslengte','Gemiddelde zinslengte','Standaarddeviatie')
    scatterPlot((df70.loc[:,'z_mean'],df10.loc[:,'z_mean']),(df70.loc[:,'z_mode'],df10.loc[:,'z_mode']),'Zinslengte','Gemiddelde zinslengte','Modus')
    boxPlot((df70.loc[:,'z_mean'],df10.loc[:,'z_mean']),'Zinslengte (gemiddelde)')
    boxPlot((df70.loc[:,'z_median'],df10.loc[:,'z_median']),'Zinslengte (mediaan)')
    boxPlot((df70.loc[:,'z_std'],df10.loc[:,'z_std']),'Zinslengte (standaarddeviatie)')
    
    # ttr: scatterplot van ttr tegen scv en boxplots van ttr en scv
    scatterPlot((df70.loc[:,'ttr'],df10.loc[:,'ttr']),(df70.loc[:,'ttr_basic'],df10.loc[:,'ttr_basic']),'Woorddiversiteit en -complexiteit','Type-tokenratio','Aandeel veelvoorkomende woorden')
    boxPlot((df70.loc[:,'ttr'],df10.loc[:,'ttr']),'Type-tokenratio')
    boxPlot((df70.loc[:,'ttr_basic'],df10.loc[:,'ttr_basic']),'Aandeel veelvoorkomende woorden')

    # dependency length: scatterplot van gemiddelde zinslengte en dependency length en boxplot van gemiddelde dependency length
    scatterPlot((df70.loc[:,'z_mean'],df10.loc[:,'z_mean']),(df70.loc[:,'d_mean'],df10.loc[:,'d_mean']),'Zinslengte en dependency length','Gemiddelde zinslengte','Gemiddelde dependency length')    
    scatterPlot((df70.loc[:,'d_mean'],df10.loc[:,'d_mean']),(df70.loc[:,'d_std'],df10.loc[:,'d_std']),'Dependency length','Gemiddelde','Standaarddeviatie')    
    boxPlot((df70.loc[:,'d_mean'],df10.loc[:,'d_mean']),'Dependency length (gemiddelde)')
    
    # woordsoorten: boxplots en scatterplots van nouns, verbs, adjectieven en bijwoorden
    boxPlot((df70.loc[:,'nouns'],df10.loc[:,'nouns']),'Zelfstandig naamwoorden')
    boxPlot((df70.loc[:,'verbs'],df10.loc[:,'verbs']),'Werkwoorden')
    scatterPlot((df70.loc[:,'nouns'],df10.loc[:,'nouns']),(df70.loc[:,'verbs'],df10.loc[:,'verbs']),'Woordsoorten','Aandeel zelfstandig naamwoorden','Aandeel werkwoorden')
    boxPlot((df70.loc[:,'adjs'],df10.loc[:,'adjs']),'Bijvoeglijk naamwoorden')
    boxPlot((df70.loc[:,'advs'],df10.loc[:,'advs']),'Bijwoorden')
    scatterPlot((df70.loc[:,'adjs'],df10.loc[:,'adjs']),(df70.loc[:,'advs'],df10.loc[:,'advs']),'Woordsoorten','Bijvoeglijk naamwoorden','Bijwoorden')
    
    sentDistr()
    
    
if __name__ == "__main__":
    main()