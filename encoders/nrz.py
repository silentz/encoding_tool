from modules.painter import Painter
from modules.line import Line

class Encoder:

    def encode(self, data):
        lines = [Line(int(x), blocks=2) for x in data]
        return Painter(lines=lines)
