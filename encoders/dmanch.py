from modules.painter import Painter
from modules.line import Line


class Encoder:

    def encode(self, data):
        lines = []
        before = 0
        for x in data:
            if x == '0':
                before = (before + 1) % 2
                lines.append(Line(before, blocks=1))
                before = (before + 1) % 2
                lines.append(Line(before, blocks=1))
            elif x == '1':
                lines.append(Line(before, blocks=1))
                before = (before + 1) % 2
                lines.append(Line(before, blocks=1))
        return Painter(lines=lines)
