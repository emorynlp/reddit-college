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
|:----------:|:-----:|:-----:|:-------:|:----:|:-----:|:-----:|:-----:|:-----:|:------:|
| 2021-11-11 | 9,397 | 2,128 |   5,502 |  818 | 1,198 | 2,047 | 1,457 | 2,585 | 25,132 |
| 2021-11-05 | 8,405 | 2,066 |   4,933 |  818 | 1,178 | 1,972 | 1,431 | 2,425 | 23,228 |
| 2021-11-02 | 7,693 | 2,023 |   4,621 |  818 | 1,168 | 1,937 | 1,422 | 2,339 | 22,021 |
| 2021-11-01 | 7,176 | 2,007 |   4,452 |  818 | 1,165 | 1,911 | 1,411 | 2,296 | 21,236 |
| 2021-10-28 | 6,152 | 1,963 |   4,179 |  818 | 1,158 | 1,874 | 1,397 | 2,221 | 19,762 |
| 2021-10-26 | 5,605 | 1,945 |   3,993 |  818 | 1,149 | 1,840 | 1,392 | 2,169 | 18,911 |
| 2021-10-25 | 5,135 | 1,934 |   3,859 |  818 | 1,148 | 1,818 | 1,383 | 2,136 | 18,231 |
| 2021-10-21 | 4,132 | 1,916 |   3,500 |  818 | 1,137 | 1,772 | 1,372 | 2,031 | 16,678 |
| 2021-10-20 | 3,818 | 1,906 |   3,388 |  818 | 1,132 | 1,755 | 1,367 | 1,992 | 16,176 |
| 2021-10-19 | 3,494 | 1,891 |   3,264 |  818 | 1,128 | 1,738 | 1,366 | 1,955 | 15,654 |
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
