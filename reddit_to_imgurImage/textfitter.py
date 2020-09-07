from PIL import Image, ImageDraw, ImageFont


class CenterdTextImage(object):
    def __init__(self, size, text_box_size, font_filename,
                 mode='RGBA', background=(0, 0, 0, 0)):
        self.height = size[1]
        self.width = size[0]
        self.text_box_height = text_box_size[1]
        self.text_box_width = text_box_size[0]
        self.image = Image.new(mode, (self.width, self.height),
                               color=background)
        self.draw = ImageDraw.Draw(self.image)
        self.x = int((self.width - self.text_box_width) / 2)
        self.y = int((self.height - self.text_box_height) / 2)
        self.font_filename = font_filename

    def write_text(self, pos, text, font_size=11,
                   color=(255, 255, 255)):
        font = ImageFont.truetype(self.font_filename, font_size)
        self.draw.text(pos, text, font=font, fill=color)

    def get_text_size(self, font_size, text):
        font = ImageFont.truetype(self.font_filename, font_size)
        return font.getsize(text)

    def build_lines(self, text, font_size):
        words = text.split()
        lines = []
        line = []
        for word in words:
            new_line = ' '.join(line + [word])
            size = self.get_text_size(font_size, new_line)
            if size[0] <= self.text_box_width:
                line.append(word)
            else:
                lines.append(line)
                line = [word]
        if line:
            lines.append(line)
        return lines

    def get_max_text_size(self, lines, font_size):
        size_array = []
        for line in lines:
            line = ' '.join(line)
            size = self.get_text_size(font_size, line)
            size_array.append(size)

        return max(size_array, key=lambda x: x[0])

    def get_optimal_font_size(self, text):
        lines = []
        font_size = 0
        height_sum = 0
        size = [0, 0]
        while height_sum < self.text_box_height:
            font_size += 1
            lines = self.build_lines(text, font_size)
            size = self.get_max_text_size(lines, font_size)
            text_height = size[1]
            height_sum = len(lines) * text_height

        font_size -= 1
        return font_size

    def write_text_lines(self, text, color=(255, 255, 255)):
        font_size = self.get_optimal_font_size(text)
        lines = self.build_lines(text, font_size)
        size = self.get_max_text_size(lines, font_size)
        height_sum = len(lines) * size[1]

        height = int((self.height - height_sum) / 2) - \
            int(size[1] / 5)
        lines = [' '.join(line) for line in lines if line]
        for index, line in enumerate(lines):
            total_size = self.get_text_size(font_size, line)
            x_left = int(self.x + ((self.text_box_width - total_size[0]) / 2))
            self.write_text((x_left, height), line,
                            font_size, color)

            height += size[1]

        return self.image
