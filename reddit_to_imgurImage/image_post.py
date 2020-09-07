from PIL import ImageDraw, ImageFont
from reddit_to_imgurImage.textfitter import CenterdTextImage
from reddit_to_imgurImage.gradient import Gradient
from datetime import datetime


class Post(object):
    def __init__(self, size, font_path):
        self.size = size
        self.post_size = (size, size)
        self.image = None
        self.font_path = font_path

    def create_text_image(self, text):
        text_box_size = (self.size - 100, self.size - 100)
        image = CenterdTextImage(self.post_size, text_box_size, self.font_path)
        image.load_text(text)
        image = image.write_text_lines()

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

    def add_source(self, source_string):
        font = ImageFont.truetype(self.font_path, 15)
        draw = ImageDraw.Draw(self.image)
        position = (40, self.size - 50)
        draw.text(position, source_string,
                  fill=(255, 255, 255, 255), font=font)

    def save(self, file_path):
        if self.image is None:
            print("No image generated")
            return None
        self.image.save(file_path, "JPEG")

    def show(self):
        if self.image is None:
            print("No image generated")
            return None
        self.image.show()
