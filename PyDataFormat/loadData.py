"""
Load the reference and candidate json files, which are to be evaluated using CIDEr.

Reference file: list of dict('image_id': image_id, 'caption': caption).
Candidate file: list of dict('image_id': image_id, 'caption': caption). One caption per image.

"""
import json
import os
from collections import defaultdict


class LoadData():
    def __init__(self, path):
        self.pathToData = path

    def readjson(self, refname, candname):

        path_to_ref_file = os.path.join(self.pathToData, refname)
        path_to_cand_file = os.path.join(self.pathToData, candname)

        ref_list = json.loads(open(path_to_ref_file, 'r').read())
        cand_list = json.loads(open(path_to_cand_file, 'r').read())

        gts = defaultdict(list)
        res = defaultdict(list)

        for l in ref_list:
            gts[l['image_id']].append({"caption": l['caption']})

        for l in cand_list:
            # if more than 1 candidate sentence exists, ignore the rest and only keep first
            if len(res[l['image_id']]) == 0:
                res[l['image_id']].append({"caption": l['caption']})

        return gts, res

