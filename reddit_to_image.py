from modules.reddit_top_subs import RedditSubmissions
from modules.reddit_subs_db import MysqlSubmissions
from modules.imgur_image_upload import ImgurPost
from modules.image_post import Post
import modules.random_filename as helper
import os
import time
import yaml

config = yaml.safe_load(open("./config.yml"))
mysql_credentials = config["mysql_credentials"]
imgur_credentials = config["imgur_credentials"]
reddit_credentials = config["reddit_credentials"]

# initialise database
database = MysqlSubmissions()
database.connect(mysql_credentials["host"],
                 mysql_credentials["database"],
                 mysql_credentials["user"],
                 mysql_credentials["password"])

# initialise imgurClient
imgur_post = ImgurPost()
imgur_post.auth_client(imgur_credentials["client_id"],
                       imgur_credentials["client_secret"],
                       imgur_credentials["access_token"],
                       imgur_credentials["refresh_token"])

# get current not posted submission from database
reddit_subs = RedditSubmissions()
reddit_subs.authenticate(reddit_credentials["client_id"],
                         reddit_credentials["client_secret"],
                         reddit_credentials["password"],
                         reddit_credentials["agent"],
                         reddit_credentials["username"])

# next fix path of image (creation and imgur)


def create_imgur_post():
    new_post = database.get_new_post()
    if not new_post:
        print("no new posts available.")
        return

    title = reddit_subs.sub_title(new_post[0][0])
    new_title = helper.delete_ltp(title)

    file_name = helper.generate_file_name(new_title)
    path = "./Posts/"
    save_path = os.path.join(path, file_name)

    post = Post(500)
    post.combine_gradient_and_text(new_title)
    post.add_source("r/LifeProTips")
    post.save(save_path)
    time.sleep(1)
    description = "parsed from subreddit 'LifeProTips'"
    imgur_post.upload_post(file_name, file_name, description, save_path)

    database.set_posted(new_post[0][0])

if __name__ == "__main__":
    create_imgur_post()
