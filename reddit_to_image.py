from modules.reddit_top_subs import LifeProTip
from modules.image_post import Post

# life_pro_tip = LifeProTip()
# new_subs = life_pro_tip.get_lpt()

path = "./LTP_Posts/"

post = Post(500, path)
post.combine_gradient_and_text("Ujs jhasjd jhasd jhasd jhasd ajdasdjhasdjshd jsjjajajaks jhsjjs jshde jsdr")
post.show()
