from PIL import Image, ImageDraw
from random import random, uniform
import colorsys
import copy


class Gradient(object):
    def __init__(self, image_size):
        self.image_size = image_size

    def generate_color(self):
        hue, lightness, satuation = random(), \
            uniform(0.45, 0.65), uniform(0.6, 1)

        return {"hue": hue, "lightness": lightness,
                "satuation": satuation}

    def generate_second_color(self, color):
        second_color = copy.copy(color)
        hue = second_color["hue"] + (1 / 360 * 90)
        if hue > 1:
            hue = hue - 1

        second_color["hue"] = hue
        return second_color

    def convert_hls_to_rgb(self, hls_color):
        rgb_color = colorsys.hls_to_rgb(hls_color["hue"],
                                        hls_color["lightness"],
                                        hls_color["satuation"])
        rgb_color = list(map(lambda x: int(x * 255), rgb_color))

        return rgb_color

    def random_gradient(self):
        img = Image.new("RGB", (self.image_size, self.image_size), "#FFFFFF")
        draw = ImageDraw.Draw(img)

        first_color = self.generate_color()
        second_color = self.generate_second_color(first_color)

        first_color = self.convert_hls_to_rgb(first_color)
        second_color = self.convert_hls_to_rgb(second_color)

        r, g, b = first_color[0], first_color[1], first_color[2]
        delta_r = (second_color[0] - r) / float(self.image_size)
        delta_g = (second_color[1] - g) / float(self.image_size)
        delta_b = (second_color[2] - b) / float(self.image_size)
        for i in range(self.image_size):
            r, g, b = r + delta_r, g + delta_g, b + delta_b
            draw.line((i, 0, i, self.image_size),
                      fill=(int(r), int(g), int(b)))

        img = img.rotate(45)
        scaled_size = self.image_size + self.image_size * 0.45
        img = img.resize((int(scaled_size), int(scaled_size)))
        x = (self.image_size * 0.45) / 2
        x2 = self.image_size + ((self.image_size * 0.45) / 2)
        img = img.crop((int(x), int(x), int(x2), int(x2)))

        return img
