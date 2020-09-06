from modules.reddit_subs_db import MysqlSubmissions
import yaml

config = yaml.safe_load(open("./config.yml"))
mysql_credentials = config["mysql_credentials"]

# initialise database
def create_table():
    database = MysqlSubmissions()
    database.connect(mysql_credentials["host"],
                     mysql_credentials["database"],
                     mysql_credentials["user"],
                     mysql_credentials["password"])

    database.create_table("life_pro_tips")

if __name__ == "__main__":
    create_table()
