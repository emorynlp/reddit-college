#!/bin/bash
source venv/bin/activate
python src/subreddit_scrapper.py .credential subreddits/
git add subreddits/*/*.json
git commit -m $(date +%Y-%m-%d)
git push
