
import pandas as pd
import numpy as np
import pickle
from tempfile import TemporaryFile
sessions = pd.read_csv('./coursera_sessions_train.txt',delimiter=';', header=None,names=['viewed','bought'])
sessions.info()
sessions.head()
import collections

viewed = sessions.viewed.values
# коневертируем значения в строки
for idx, item  in enumerate(viewed):
    viewed[idx] = collections.Counter(viewed[idx].split(","))
    viewed[idx] = viewed[idx].split(",")

c = []
print 'end'
print viewed.size

for n in range(0,viewed.size):
    c = c + viewed[n]
print 'end'

with open('collection_viewed.txt', 'wb') as f:
    pickle.dump(c,f)

#np.savetxt('./views_colection.txt',c,fmt='%.18g')
#for n in range(0,viewed.size):
#    c = c + viewed[n]
#print 'end'

   
    