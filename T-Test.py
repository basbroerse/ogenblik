# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:55:20 2024

@author: basbr
"""

import pandas as pd
import numpy as np
import scipy.stats as stats

def tTest(data1, data2):
    var1 = np.var(data1)
    var2 = np.var(data2)
    print('Variance: ', var1, var2,(var1/var2))
    print(stats.ttest_ind(a=data1,b=data2,equal_var=True))

def main():
    file_in = 'Results.xlsx'
   
    tables  = pd.read_excel(file_in, sheet_name=None)
    sheets = list(tables.keys())
        
    df70 = tables[sheets[0]]
    df10 = tables[sheets[1]]
    
    print('\nNouns:')
    tTest(df70.loc[:,'nouns'],df10.loc[:,'nouns'])
    print('\nVerbs:')
    tTest(df70.loc[:,'verbs'],df10.loc[:,'verbs'])
    print('\nAdjectives:')
    tTest(df70.loc[:,'adjs'],df10.loc[:,'adjs'])
    print('\nAdverbs:')
    tTest(df70.loc[:,'advs'],df10.loc[:,'advs'])
    
    print('\nTTR:')
    tTest(df70.loc[:,'ttr'],df10.loc[:,'ttr'])
    print('\nSCV:')
    tTest(df70.loc[:,'ttr_basic'],df10.loc[:,'ttr_basic'])
    
    print('\nMean sentence length:')
    tTest(df70.loc[:,'z_mean'],df10.loc[:,'z_mean'])
    print('\nMode of the sentence length:')
    tTest(df70.loc[:,'z_mode'],df10.loc[:,'z_mode'])
    print('\nMedian sentence length:')
    tTest(df70.loc[:,'z_median'],df10.loc[:,'z_median'])
    
    print('\nMean dependency length:')
    tTest(df70.loc[:,'d_mean'],df10.loc[:,'d_mean'])
    
if __name__ == "__main__":
    main()