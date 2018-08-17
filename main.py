import praw

client_secret = ''
client_id = ''
user_agent = ''

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)
ids = []
subreddit = reddit.subreddit('theydidthemonstermath')
total_posts = 0
matched_posts = 0
for submission in subreddit.hot(limit=1000):
    ids.append(submission.id)
    all_comments = list(submission.comments)
    for comment in all_comments:
        f = False
        if 'at least' in comment.body.lower():
            replies = comment.replies
            for c in replies:
                if 'r/technicallythetruth' in c.body:
                    matched_posts += 1
                    f = True
                    break
        if f:
            break
    total_posts += 1
    print("Parsed {} posts".format(total_posts))

print("{0} / {1}".format(matched_posts, total_posts))


