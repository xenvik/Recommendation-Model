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
# SOFTWARE.import re

import pandas as pd
from collections import Counter
df = pd.read_csv('D:/Thesis/crypto_twitter_reddit.csv', index_col=0)
df = df[df.type == 'twitter']  # only twitter data


# finding mentions in data
flist = []
df.text = df.text.fillna('')
for row in df.text:
    for word in row.split():
        if word[0] == '@':
            word = word.split("'")[0]
            flist.append(word.lower())

# cleaning mentions from extra characters
mentions = []
for row in flist:
    for char in "[#!$%^&*()-+|:;,<>?./…]":
        row = row.replace(char, '')
    mentions.append(row)

# Counter for mentions
dct = Counter(mentions)

import operator # Descending order

list= sorted(dct.items(), key=operator.itemgetter(1), reverse=True)
dfm = dict(list)

dfm = pd.DataFrame.from_dict(data=dfm, orient='index')
print(dfm)

#saving the dataframe
dfm.to_csv('Mentions.csv', header=['Mentions'])
