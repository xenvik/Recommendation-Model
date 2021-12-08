# MIT License
# 
# Copyright (c) 2018 Stichting SingularityNET
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import re
import operator

import numpy
import pandas as pd
import numpy as np
from collections import Counter
df = pd.read_csv('D:/Thesis/crypto_twitter_reddit.csv', index_col=0)
df = df[df.type == 'twitter']  # only twitter data

# finding mentions in data by feed owners

def feedomen(feedo):
    flist = []
    df = pd.read_csv('D:/Thesis/crypto_twitter_reddit.csv', index_col=0)
    df = df[df.type == 'twitter']
    df = df[df.link == feedo]
    df.text = df.text.fillna('')
    for row in df.text:
        if row[0] == 'R' and row[1] == 'T':
            continue
        else:
            for word in row.split():
                if word[0] == '@':
                    word = word.split("'")[0]
                    flist.append(word.lower())

# cleaning mentions from extra characters
    omentions = []
    for row in flist:
        for char in "[#!$%^&*()-+|:;,<>?./…]":
            row = row.replace(char, '')
        omentions.append(row)

# Counter for mentions
    dct = Counter(omentions)
    cist = sorted(dct.items(), key=operator.itemgetter(1), reverse=True)
    return(cist)


cmlist = []
df.link = df.link.fillna('')
df.link = df.link.str.replace('https://twitter.com/','@',regex=True)
for link in df.link:
    if link in cmlist:
        continue
    else:
        cmlist.append(link)
#cat = Counter(cmlist)
#print(cmlist)


# Mentions by feed owners
feedlist=[]
for feedo in cmlist:
    feedlist.append(feedomen(feedo))
    #feedomen(feedo)
print(feedlist)


# saving the dataframe
#feedl.to_csv('feedomentions.csv', header=['OMentions'])
#my_df = pd.DataFrame(feedlist)
#my_df.to_csv('feedom.csv', index=False, header=False)

