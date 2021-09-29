__author__ = 'Jinho D. Choi'

import glob
import json
import os
import sys
from datetime import datetime

import praw
from praw import Reddit
from praw.models import MoreComments


def praw_scrapper(filename):
    lines = open(filename).readlines()
    ID = lines[0].strip()
    SECRET = lines[1].strip()
    AGENT = lines[2].strip()
    return praw.Reddit(client_id=ID, client_secret=SECRET, user_agent=AGENT)


def subreddit_scrapper(scrapper: Reddit, cname: str, outdir: str):
    def aux(sms):
        count = 0
        for sm in sms:
            if (not sm.selftext) or (sm.stickied): continue

            submission = {
                'sid': sm.id,
                'link': sm.permalink,
                'title:': sm.title,
                'text': sm.selftext,
                'author': sm.author.name if sm.author else None,
                'created': round(sm.created_utc),  # datetime.fromtimestamp(created)
                'retrieved': round(datetime.now().timestamp()),
                'over_18': sm.over_18,
                'upvotes': sm.score,
                'upvote_ratio': sm.upvote_ratio}

            comments = submission.setdefault('comments', dict())
            sm.comment_sort = 'new'

            for cmt in sm.comments:
                if isinstance(cmt, MoreComments) or (not cmt.body): continue
                comments[cmt.id] = {
                    'link': cmt.permalink,
                    'text': cmt.body,
                    'author': cmt.author.name if cmt.author else None,
                    'created': round(cmt.created_utc),
                    'upvotes': cmt.score,
                }

            filename = '{}-{}-{}.json'.format(cname, submission['created'], submission['sid'])
            with open(os.path.join(outdir, filename), 'w') as fout:
                json.dump(submission, fout)

            if filename not in submissions:
                submissions.add(filename)
                count += 1
            break
        return count

    submissions = {os.path.basename(jsonfile) for jsonfile in glob.glob(os.path.join(outdir, '*.json'))}
    limit = None
    new  = aux(scrapper.subreddit(cname).hot(limit=limit))
    new += aux(scrapper.subreddit(cname).top(limit=limit))
    print('{:<15} -> Total: {:>5}, New: {:>3}'.format(cname, len(submissions), new))


if __name__ == '__main__':
    CNAMES = ['College', 'CollegeRant', 'GradSchool', 'CollegeMajors', 'CollegeAdvice']
    CREDENTIAL_FILE = sys.argv[1]
    OUTPUT_DIR = sys.argv[2]

    scrapper = praw_scrapper(CREDENTIAL_FILE)
    for cname in CNAMES: subreddit_scrapper(scrapper, cname, os.path.join(OUTPUT_DIR, cname))
