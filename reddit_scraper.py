from credentials import reddit

for submission in reddit.subreddit('nosleep').hot(limit=10):
    print(submission.title, [comment.body for comment in submission.comments])