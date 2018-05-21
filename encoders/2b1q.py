from modules.painter import Painter
from modules.line import Line


class Encoder:

    def encode(self, data):
        lines = []
        for i in range(0, len(data), 2):
            x = data[i: i + 2]
            if x == '00':
                lines.append(Line(0, blocks=2))
            elif x == '01':
                lines.append(Line(1, blocks=2))
            elif x == '10':
                lines.append(Line(2, blocks=2))
            elif x == '11':
                lines.append(Line(3, blocks=2))
        return Painter(lines=lines)