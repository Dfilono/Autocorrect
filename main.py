# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import textdistance
import re
from collections import Counter

# Vocabulary
words = []
with open('book.txt', 'r', encoding="utf8") as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words = re.findall('\w+',file_name_data)
    
V = set(words)

# Frequency of words    
word_freq_dict = {}
word_freq_dict = Counter(words)

#Probability of words
probs = {}
Total = sum(word_freq_dict.values())
for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k]/Total

def my_autocorrect(input_word):
    input_word = input_word.lower()
    if input_word in V:
        return("Your word seems to be correct")
    else:
        similar = [1-(textdistance.Jaccard(qval=2).distance(v,input_word)) for v in word_freq_dict.keys()]
        df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
        df = df.rename(columns={'index':'Word', 0:'Prob'})
        df['Similarity'] = similar
        output = df.sort_values(['Similarity', 'Prob'], ascending=False).head()
        return(output)
    
d = my_autocorrect("neverthelest")