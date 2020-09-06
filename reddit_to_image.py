from modules.reddit_top_subs import LifeProTip
from modules.reddit_subs_db import MysqlSubmissions
from modules.image_post import Post
from datetime import datetime

import config

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%H:%S")

database = MysqlSubmissions()
database.connect(config.host,
                 config.database,
                 config.user,
                 config.password)

database.create_table("life_pro_tips")

# get current not posted submission from database

lpt = LifeProTip()
subs = lpt.get_top_subs("LifeProTips")

database.insert(subs)
new_post = database.get_new_post()
if new_post:
    new_title = lpt.sub_title(new_post[0][0])

    path = "./Posts/"
    post = Post(500, path)

    post.combine_gradient_and_text(new_title)
    post.add_source("r/LifeProTips")
    post.show()

    database.set_posted(new_post[0][0])
else:
    print("no_new_posts")
