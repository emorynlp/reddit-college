# Copyright 2021 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

