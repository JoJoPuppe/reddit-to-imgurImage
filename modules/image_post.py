from PIL import ImageDraw
from modules.textfitter import CenterdTextImage
from modules.gradient import Gradient
from datetime import datetime
import config
import re


class Post(object):
    def __init__(self, size, path):
        self.size = size
        self.post_size = (size, size)
        self.save_path = path
        self.image = None

    def create_text_image(self, text):
        font_path = config.font_path
        text_box_size = (self.size - 100, self.size - 100)
        image = CenterdTextImage(self.post_size, text_box_size, font_path)
        clean_text = self.clean_ltp_string(text)
        image = image.write_text_lines(clean_text)

        return image

    def combine_gradient_and_text(self, text):
        gradient = Gradient(self.size)
        gradient_img = gradient.random_gradient()
        text_box = self.create_text_image(text)

        text_image = ImageDraw.Draw(text_box)
        text_image.rectangle([(25, 25), (self.size - 25, self.size - 25)],
                             outline=(255, 255, 255), width=3)

        gradient_img.paste(text_box, (0, 0, self.size, self.size), text_box)

        self.image = gradient_img

    def save(self):
        if self.image is None:
            print("No image generated")
            return None

        utc_string = datetime.utcnow()
        post_name = self.save_path + str(utc_string)
        self.image.save(post_name, "JPEG")

    def show(self):
        if self.image is None:
            print("No image generated")
            return None
        self.image.show()

    def clean_ltp_string(self, text):
        new_text = re.search(r'(?![ltp\W]).+', text, flags=re.IGNORECASE)
        return new_text.group(0)
