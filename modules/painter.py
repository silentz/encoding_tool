from PIL import Image, ImageDraw
from modules.line import Line


class Painter:

    def __init__(self, lines):
        self.lines = lines
        self.cell_height = 40
        self.cell_width = 10
        self.vpadding = 40
        self.hpadding = 40
        self.line_width = 2
        self.image = Image.new('RGB', self.get_size(), color='#FFFFFF')
        self.draw = ImageDraw.Draw(self.image)

    def get_level_count(self):
        return max([x.level for x in self.lines]) + 1

    def get_block_count(self):
        return sum([x.blocks for x in self.lines])

    def draw_dashed_line(self, blocks, height, colors):
        for block in range(0, blocks):
            xs = block * self.cell_width + self.hpadding
            xf = (block + 1) * self.cell_width + self.hpadding
            self.draw.line((xs, height, xf, height),
                           fill=colors[block % len(colors)], width=self.line_width)

    def get_size(self):
        height = (self.get_level_count() - 1) * self.cell_height + 2 * self.vpadding
        width = self.get_block_count() * self.cell_width + 2* self.hpadding
        return (width, height)

    def draw_grid(self):
        synchro_colors = ['#FF0000', '#00FF00']
        levels = self.get_level_count()
        base_line = (self.get_level_count() - 1) * self.cell_height + self.vpadding
        for level in range(0, levels):
            vy = base_line - level * self.cell_height + self.line_width
            self.draw_dashed_line(self.get_block_count(), vy, synchro_colors)

    def draw_data(self):
        beforex = self.hpadding
        beforey = (self.get_level_count() - 1) * self.cell_height + self.vpadding
        base_line = beforey
        for line in self.lines:
            newx = line.blocks * self.cell_width + beforex
            newy = base_line - line.level * self.cell_height
            self.draw.line((beforex, newy, newx, newy), fill='#000000', width=self.line_width)
            self.draw.line((beforex, beforey, beforex, newy), fill='#000000', width=self.line_width)
            beforex = newx
            beforey = newy

    def paint(self):
        self.draw_grid()
        self.draw_data()
        return self.image
