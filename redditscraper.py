#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:11:16 2020

@author: matthew
"""


import praw

reddit = praw.Reddit(user_agent="Comment Extraction 1.0 by /u/throwaway341234124",
                     client_id="f24NsSX3Tfsi7A", client_secret="M6H92zuFNGxUoYNJCH8fas7giqg",)

url = "https://www.reddit.com/r/politics/comments/hrvc1m/ruth_bader_ginsburg_discharged_from_the_hospital/"
submission = reddit.submission(url=url)

submission.comments.replace_more(limit=None)
comment_list = []
for top_level_comment in submission.comments:
    comment_list.append(top_level_comment.body)   

del comment_list[0]