from PIL import Image, ImageDraw


class Painter:

    def __init__(self, data, height):
        self.data = data
        self.white = '#FFFFFF'
        self.black = '#000000'
        self.secondary = '#63FF36'
        self.CELL_WIDTH = 30
        self.CELL_HEIGHT = 40
        self.VERTICAL_PADDING = 10
        self.HORIZONTAL_PADDING = 10
        self.max_value = height - 1
        self.height = self.max_value * self.CELL_HEIGHT + 2 * self.VERTICAL_PADDING
        self.width = len(self.data) * self.CELL_WIDTH + 2 * self.HORIZONTAL_PADDING

    def rectangle_coord(self, block):
        startx = self.HORIZONTAL_PADDING + block * self.CELL_WIDTH
        finishx = startx + self.CELL_WIDTH
        starty = self.height - self.VERTICAL_PADDING
        finishy = starty - self.max_value * self.CELL_HEIGHT
        return startx, starty, finishx, finishy

    def line_coord(self, block, value):
        startx = self.HORIZONTAL_PADDING + block * self.CELL_WIDTH
        finishx = startx + self.CELL_WIDTH
        starty = self.height - self.VERTICAL_PADDING - value * self.CELL_HEIGHT
        finishy = starty
        return startx, starty, finishx, finishy

    def draw_grid(self, image_draw):
        for block in range(1, len(self.data), 2):
            startx, starty, finishx, finishy = self.rectangle_coord(block)
            image_draw.rectangle((startx, starty, finishx, finishy), fill=self.secondary)

        image_draw.line((self.HORIZONTAL_PADDING, self.height - self.VERTICAL_PADDING,
                        self.width - self.HORIZONTAL_PADDING // 2, self.height - self.VERTICAL_PADDING),
                        fill=self.black, width=1)
        image_draw.line((self.HORIZONTAL_PADDING, self.height - self.VERTICAL_PADDING,
                        self.HORIZONTAL_PADDING, self.VERTICAL_PADDING // 2),
                        fill=self.black, width=1)

    def draw_data(self, image_draw):
        bottom = self.height - self.VERTICAL_PADDING
        beforex = self.HORIZONTAL_PADDING
        beforey = bottom
        for index, value in enumerate(self.data):
            startx, starty, finishx, finishy = self.line_coord(index, value)
            image_draw.line((startx, starty, finishx, finishy), fill=self.black, width=2)
            image_draw.line((beforex, beforey, startx, starty), fill=self.black, width=2)
            beforex = finishx
            beforey = finishy

    def paint(self):
        image = Image.new('RGB', (self.width, self.height), color=self.white)
        draw = ImageDraw.Draw(image)
        self.draw_grid(draw)
        self.draw_data(draw)
        return image
