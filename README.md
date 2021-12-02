# Reddit College

Subreddits related to college.

* Last update: 2021-11-29
* Contact: [Jinho D. Choi](https://github.com/jdchoi77)


## Statistics

* [ApplyingToCollege](dat/ApplyingToCollege): 12,819
* [AskAcademia](dat/AskAcademia): 2,376
* [College(](dat/College): 7,086
* [CollegeAdvice](dat/CollegeAdvice): 818 (last update: 2021-10-12)
* [CollegeMajors](dat/CollegeMajors): 1,235
* [CollegeRant](dat/CollegeRant): 2,235
* [Emory](dat/Emory): 1,520
* [GradSchool](dat/GradSchool): 3,033
* Total: 30,304


## Format

A subreddit is represented by a dictionary whose key-value pairs are as follows:

* `sid`: the subreddit ID (`str`).
* `link`: the relative URL to the subreddit (`str`).
* `title`: the title (`str`).
* `text`: the content (`str`).
* `author`: the author ID (`str`).
* `created`: the time that the subreddit was created in milliseconds (`int`).
* `updated`: the last time that the subreddit was updated in milliseconds (`int`).
* `over_18`: `true` if this subreddit is marked as NSFW; otherwise, `false` (`bool`).
* `upvotes`: the number of upvotes (`int`).
* `upvote_ratio`: the percentage of upvotes from all votes (`float`).
* `comments`: a dictionary where each pair of the key is a comment ID and the value is its corresponding comment.

A comment is represented by a dictionary whose key-value pairs are as follows:

* `link`: the relative URL to the comment (`str`).
* `text`: the content (`str`).
* `author`: the author ID (`str`).
* `created`: the time that the subreddit was created in milliseconds (`int`).
* `upvotes`: the number of upvotes (`int`).
* `replies`: a dictionary where each pair of the key is a comment ID and the value is its corresponding comment.
