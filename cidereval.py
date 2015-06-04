
# coding: utf-8

# In[1]:

# demo script for running CIDEr
from pydataformat.loadData import LoadData
import pdb
import json
from pyciderevalcap.eval import CIDErEvalCap as ciderEval

pathToData = 'data/'

refName = 'pascal50S.json'
candName = 'pascal_candsB.json'

resultFile = 'results.json'


# In[2]:

# load reference and candidate sentences
loadDat = LoadData(pathToData)
gts, res = loadDat.readJson(refName, candName)


# In[3]:

# calculate cider scores
scorer = ciderEval(gts, res)
# scores: dict of list with key = metric and value = score given to each candidate
scores = scorer.evaluate()


# In[7]:

# scores['CIDEr'] contains CIDEr scores in a list for each candidate
# scores['CIDErD'] contains CIDEr-D scores in a list for each candidate

with open(result_file, 'w') as outfile:
    json.dump(scores, outfile)



