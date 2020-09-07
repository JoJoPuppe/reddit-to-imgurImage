import praw
import time


class RedditSubmissions(object):
    def __init__(self, min_score=100):
        self.reddit = None
        self.min_score = min_score

    def authenticate(self, client_id, client_secret, password, user_agent, username):
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             password=password,
                             user_agent=user_agent,
                             username=username)
        self.reddit = reddit

    def get_top_subs(self, sub_name):
        subs = []
        for submission in self.reddit.subreddit(sub_name).hot(limit=10):
            if submission.score < self.min_score: continue
            formatted_date = time.strftime("%Y-%m-%d %H:%H:%S", time.localtime(submission.created_utc))
            subs.append((submission.id, formatted_date))
        return subs

    def sub_title(self, sub_id):
        oldest_sub = praw.models.Submission(self.reddit, id=sub_id)
        return oldest_sub.title
