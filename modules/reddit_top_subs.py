import praw
import config
import time


class LifeProTip(object):
    def __init__(self):
        self.reddit = self._auth_reddit()
        self.sub_name = "LifeProTips"
        self.min_score = 100

    def _auth_reddit(self):
        reddit = praw.Reddit(client_id=config.red_client_id,
                             client_secret=config.red_client_secret,
                             password=config.red_password,
                             user_agent=config.red_agent,
                             username=config.red_username)
        return reddit

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
