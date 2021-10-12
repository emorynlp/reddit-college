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
from datetime import datetime
from typing import Dict, Any, Set, Iterable, List

import praw
from praw import Reddit
from praw.models import MoreComments
from praw.reddit import Comment, Submission


def praw_scrapper(filename):
    lines = open(filename).readlines()
    ID = lines[0].strip()
    SECRET = lines[1].strip()
    AGENT = lines[2].strip()
    return praw.Reddit(client_id=ID, client_secret=SECRET, user_agent=AGENT)


def skip_subreddit(subreddit: Submission) -> bool:
    if not subreddit.selftext: return True
    if subreddit.stickied: return True
    return False


def skip_comment(comment: Comment) -> bool:
    if isinstance(comment, MoreComments): return True
    if not comment.body: return True
    if comment.stickied: return True
    if comment.author and comment.author.name == 'AutoModerator': return True
    return False


# def subreddit_scrapper(scrap: Reddit, cname: str, outdir: str):
#     retrieved_sids: Set[str]
#
#     submissions = {os.path.basename(jsonfile) for jsonfile in glob.glob(os.path.join(outdir, '*.json'))}
#     new = aux(scrap.subreddit(cname).hot(limit=None))
#     new += aux(scrap.subreddit(cname).top(limit=None))
#     print('{:<15} -> Total: {:>5}, New: {:>3}'.format(cname, len(submissions), new))
#     return len(submissions)














# def save_subreddits(scrap: Reddit, praw_subreddits: Iterable[Submission], retrieved_ids: Set[str], cname: str, outdir: str):
#     count = 0
#
#     for praw_subreddit in praw_subreddits:
#         if praw_subreddit.id in retrieved_ids or skip_subreddit(praw_subreddit): continue
#         filename = '{}-{}-{}.json'.format(cname, round(praw_subreddit.created_utc), praw_subreddit.id)
#         filepath = os.path.join(outdir, cname, filename)
#         dict_subreddit = json.load(open(filepath)) if os.path.isfile(filepath) else dict()
#
#         if retrieve_subreddit(scrap, praw_subreddit, dict_subreddit):
#             json.dump(dict_subreddit, open(filepath, 'w'))
#             count += 1
#
#     return count


def update_subreddits(scrap: Reddit, cname: str, outdir: str) -> int:
    count = 0

    for filepath in glob.glob(os.path.join(outdir, cname, '*.json')):
        filename = os.path.basename(filepath)
        sid = filename[filename.rfind('-')+1:-5]
        print(filename)
        praw_subreddit = scrap.submission(sid)
        if save_subreddit(scrap, praw_subreddit, cname, outdir):
            count += 1

    return count


def save_subreddit(scrap: Reddit, praw_subreddit: Submission, cname: str, outdir: str) -> bool:
    filename = '{}-{}-{}.json'.format(cname, round(praw_subreddit.created_utc), praw_subreddit.id)
    filepath = os.path.join(outdir, cname, filename)
    dict_subreddit = json.load(open(filepath)) if os.path.isfile(filepath) else dict()

    if retrieve_subreddit(scrap, praw_subreddit, dict_subreddit):
        json.dump(dict_subreddit, open(filepath, 'w'), indent=2)
        return True

    return False


def retrieve_subreddit(scrap: Reddit, praw_subreddit: Submission, dict_subreddit: Dict[str, Any]) -> bool:
    updated = False

    if not dict_subreddit:
        dict_subreddit['sid'] = praw_subreddit.id
        dict_subreddit['link'] = praw_subreddit.permalink
        dict_subreddit['title:'] = praw_subreddit.title
        dict_subreddit['text'] = praw_subreddit.selftext
        dict_subreddit['author'] = praw_subreddit.author.name if praw_subreddit.author else None
        dict_subreddit['created'] = round(praw_subreddit.created_utc)
        dict_subreddit['updated'] = 0
        dict_subreddit['over_18'] = praw_subreddit.over_18
        dict_subreddit['upvotes'] = praw_subreddit.score
        dict_subreddit['upvote_ratio'] = praw_subreddit.upvote_ratio
        dict_subreddit['comments'] = dict()
        updated = True

    if 'retrieved' in dict_subreddit:
        del dict_subreddit['retrieved']
        updated = True

    # sm.comment_sort = 'new'
    dict_comments = dict_subreddit['comments']
    praw_comments = praw_subreddit.comments
    praw_comments.replace_more(limit=None)

    for praw_comment in praw_comments:
        if skip_comment(praw_comment): continue
        if retrieve_comment(scrap, praw_comment, dict_comments.setdefault(praw_comment.id, dict())):
            updated = True

    if updated: dict_subreddit['updated'] = round(datetime.now().timestamp())
    return updated


def retrieve_comment(scrap: Reddit, praw_comment: Comment, dict_comment: Dict[str, Any]) -> bool:
    updated = False

    if not dict_comment:
        dict_comment['link'] = praw_comment.permalink
        dict_comment['text'] = praw_comment.body
        dict_comment['author'] = praw_comment.author.name if praw_comment.author else None
        dict_comment['created'] = round(praw_comment.created_utc)
        dict_comment['upvotes'] = praw_comment.score
        dict_comment['replies'] = dict()
        updated = True

    dict_replies = dict_comment.setdefault('replies', dict())  # TODO: dict_comment['replies']
    praw_replies = praw_comment.replies
    praw_replies.replace_more(limit=None)

    for praw_reply in praw_replies:
        if skip_comment(praw_reply): continue
        if retrieve_comment(scrap, praw_reply, dict_replies.setdefault(praw_reply.id, dict())):
            updated = True

    return updated


if __name__ == '__main__':
    # CNAMES = ['AskAcademia', 'College', 'CollegeAdvice', 'CollegeMajors', 'CollegeRant', 'Emory', 'GradSchool']
    CNAMES = ['College', 'CollegeAdvice', 'CollegeMajors', 'CollegeRant', 'GradSchool']

    # create a scrapper
    CREDENTIAL_FILE = sys.argv[1]
    OUTPUT_DIR = sys.argv[2]
    STATS_TXT = sys.argv[3]
    scrap = praw_scrapper(CREDENTIAL_FILE)

    # update existing subreddits
    with open(STATS_TXT, 'w') as fout:
        for cname in CNAMES:
            count = update_subreddits(scrap, cname, OUTPUT_DIR)
            fout.write('{}\t{}\n'.format(cname, count))
