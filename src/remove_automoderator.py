__author__ = 'Jinho D. Choi'

import glob
import json
import os
import sys

if __name__ == '__main__':
    INPUT_DIR = sys.argv[1]
    for jsonfile in glob.glob(os.path.join(INPUT_DIR, '*/*.json')):
        d = json.load(open(jsonfile))
        comments = d['comments']
        cids = {cid for cid, comment in comments.items() if comment['author'] == 'AutoModerator'}
        if cids:
            print(os.path.basename(jsonfile))
            for cid in cids: del comments[cid]
            with open(jsonfile, 'w') as fout: json.dump(d, fout)

