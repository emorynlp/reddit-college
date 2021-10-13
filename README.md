# Reddit Data

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

## Statistics

| Date       | ApplyingToCollege | AskAcademia | College | CollegeAdvice | CollegeMajors | CollegeRant | Emory | GradSchool |  Total |
|:----------:|------------------:|------------:|--------:|--------------:|--------------:|------------:|------:|-----------:|-------:|
| 2021-10-12 |             1,739 |       1,854 |   2,630 |           818 |         1,114 |       1,664 | 1,342 |      1,768 | 12,929 |
| 2021-10-04 |                 0 |           0 |   1,714 |           817 |         1,091 |       1,518 |     0 |      1,418 |  6,558 |

