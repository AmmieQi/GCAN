
# coding: utf-8

# In[ ]:


##read the Data 
import numpy as np
import os
path=r""
files= os.listdir(path)
a=[]
k=[]
for file in range(0,data size):
    f = open(r"{}.txt".format(file))
    results=[]
    k.append(file)    
    next(f)
    for line in f.readlines():
        results.append(list(map(float,line.split(','))))
    results=np.array(results)
    results=results.tolist()
    a.append(results)  
    
##let all the rewteet user size of news be the same
import random
from sklearn import preprocessing
data_all=[]
for i in range(0,data size):
    if len(a[i])>=rewteet user size:
        k=a[i][0:rewteet user size]
        
        data_all.append(k)
    else:
        a[i]=np.asarray(a[i])
        q=a[i][np.random.choice(a[i].shape[0],rewteet user size,replace=True),:]
        q=q.tolist()
        a[i]=a[i].tolist()
        k=a[i].extend(q)
        k=a[i][0:rewteet user size]
        
        data_all.append(k)
        
##use the user profile to calculate their cosine similarity for building the graph
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
path=r"  "
files= os.listdir(path)
a=[]
cos=[]
for j in data_all:
    adj=[]
    data=pd.read_csv(data_all[j])
    
    for i in range(0,retweet user size):
        a=data.iloc[i,:]
        a=np.array(a)
        a=a.reshape(1,-1)
        similar=[]
        
        for k in range(0,retweet user size):
            b=data.iloc[k,:]
            b=np.array(b)
            b=b.reshape(1,-1)
            cosine=cosine_similarity(a,b)
            similar.append(np.round(cosine,2))
            
        similar=np.array(similar)
        similar=similar.flatten()
        adj.append(similar)
    cos.append(adj)

#encode the news content
import pandas as pd
import numpy as np
with open(r".txt", 'r') as f: # read all the news content 
    next(f)
    contents = f.readlines()
    
from keras.preprocessing.text import one_hot
vocab_size=
encoded_docs=[one_hot(d,vocab_size) for d in contents]

from keras.preprocessing.sequence import pad_sequences
padded_docs=pad_sequences(encoded_docs,maxlen= ,padding="post") #let all the word embedding be the same length

