from modules.painter import Painter
from modules.line import Line


class Encoder:

    def next(self, before, old):
        if before == 2:
            return 1
        elif before == 0:
            return 1
        elif old == 0:
            return 2
        else:
            return 0

    def encode(self, data):
        lines = []
        before = 1
        old = 0
        for x in data:
            if x == '0':
                lines.append(Line(before, blocks=2))
            elif x == '1':
                before, old = self.next(before, old), before
                lines.append(Line(before, blocks=2))
        return Painter(lines=lines)
