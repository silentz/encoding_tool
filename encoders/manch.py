from modules.painter import Painter
from modules.line import Line


class Encoder:

    def encode(self, data):
        lines = []
        for x in data:
            if x == '0':
                lines.append(Line(0, blocks=1))
                lines.append(Line(1, blocks=1))
            elif x == '1':
                lines.append(Line(1, blocks=1))
                lines.append(Line(0, blocks=1))
        return Painter(lines=lines)
