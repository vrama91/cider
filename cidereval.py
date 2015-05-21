
# coding: utf-8

# In[1]:

# demo script for running CIDEr
from PyDataFormat.loadData import LoadData
import pdb
from pyciderevalcap.eval import CIDErEvalCap as cider

pathToData = '/Users/rama/Research/data/pyCider/'

refName = 'pascal50S.json'
candName = 'pascal_candsB.json'


# In[2]:

# load reference and candidate sentences
loadDat = LoadData(pathToData)
gts, res = loadDat.readjson(refName, candName)


# In[3]:

# calculate cider scores
cider_scorer = cider(gts, res)
# scores: dict of list with key = metric and value = score given to each candidate
scores = cider_scorer.evaluate()


# In[ ]:



