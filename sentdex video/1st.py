import praw

reddit = praw.Reddit(client_id = "_WkPL3qfOww1xw",
                     client_secret = "W74sDxX2UGPSFUmnrHGu9dFJkrw",
                     username = "prasadgujar16",
                     password = "tooweaktooslow",
                     user_agent = "prawtutoral")

subreddit = reddit.subreddit('python')

hot_python =  subreddit.hot(limit=5)

for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(submission.title,
                                                                          submission.ups,
                                                                          submission.downs,
                                                                          submission.visited))
    subreddit.subscribe()    

