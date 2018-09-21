import os

import praw

competitors = ['PhoenixVersion1', 'jeepdave', 'waspstinger106', 'kotsthepro', 'BlackoutAviation']
scores = {}
reddit = praw.Reddit(client_id=os.environ['reddit_client_id'],
                     client_secret=os.environ['reddit_client_secret'],
                     password=os.environ['reddit_password'],
                     user_agent='SVTFOE command bot (by u/J_C___)',
                     username=os.environ['reddit_username'])


def get_scores(user, score=0):
    for submission in reddit.redditor(user).submissions.new():
        if '/269' in submission.title:
            # print(submission.title + ':' + str(submission.score))
            score = score + int(submission.score)
            # print(score)
    return score
