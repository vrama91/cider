__author__ = 'rama'
from tokenizer.ptbtokenizer import PTBTokenizer
from cider.cider import Cider
from ciderD.ciderD import CiderD

class CIDErEvalCap:
    def __init__(self, gts, res):
        print 'tokenization...'
        tokenizer = PTBTokenizer()
        _gts = tokenizer.tokenize(gts)
        print 'tokenized refs'
        _res = tokenizer.tokenize(res)
        print 'tokenized cands'
        self.gts = _gts
        self.res = _res


    def evaluate(self):
        # =================================================
        # Set up scorers
        # =================================================

        print 'setting up scorers...'
        scorers = [
            (Cider(), "CIDEr"), (CiderD(), "CIDErD")
        ]

        # =================================================
        # Compute scores
        # =================================================
        metric_scores = {}
        for scorer, method in scorers:
            print 'computing %s score...' % (scorer.method())
            score, scores = scorer.compute_score(self.gts, self.res)
            print "%s: %0.3f" % (method, score)
            metric_scores[method] = scores
        return metric_scores
