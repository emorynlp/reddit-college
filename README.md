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

| Date       | ATC   | AA    | C       | CA   | CM    | CR    | E     | GS    |  Total |
|:----------:|------:|------:|--------:|-----:|------:|------:|------:|------:|-------:|
| 2021-10-15 | 2,466 | 1,857 |   2,922 |  818 | 1,119 | 1,697 | 1,350 | 1,842 | 14,073 |
| 2021-10-14 | 2,235 | 1,856 |   2,852 |  818 | 1,117 | 1,684 | 1,350 | 1,817 | 13,729 |
| 2021-10-13 | 1,996 | 1,856 |   2,737 |  818 | 1,115 | 1,670 | 1,344 | 1,790 | 13,326 |
| 2021-10-12 | 1,739 | 1,854 |   2,630 |  818 | 1,114 | 1,664 | 1,342 | 1,768 | 12,929 |
| 2021-10-04 |     0 |     0 |   1,714 |  817 | 1,091 | 1,518 |     0 | 1,418 |  6,558 |

* ATC: ApplyingToCollege
* AA: AskAcademia
* C: College
* CA: CollegeAdvice
* CM: CollegeMajors
* CR: CollegeRant
* E: Emory
* GS: GradSchool
