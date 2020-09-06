from modules.reddit_subs_db import MysqlSubmissions
from modules.reddit_top_subs import RedditSubmissions
import yaml

config = yaml.safe_load(open("./config.yml"))
mysql_credentials = config["mysql_credentials"]
reddit_credentials = config["reddit_credentials"]

# initialise database
database = MysqlSubmissions()
database.connect(mysql_credentials["host"],
                 mysql_credentials["database"],
                 mysql_credentials["user"],
                 mysql_credentials["password"])

database.create_table("life_pro_tips")

# get current not posted submission from database
reddit_subs = RedditSubmissions()
reddit_subs.authenticate(reddit_credentials["client_id"],
                         reddit_credentials["client_secret"],
                         reddit_credentials["password"],
                         reddit_credentials["agent"],
                         reddit_credentials["username"])

def get_subs():
    return reddit_subs.get_top_subs("LifeProTips")

def insert_to_db(subs):
    database.insert(subs)

if __name__ == "__main__":
    subs = get_subs()
    insert_to_db(subs)
