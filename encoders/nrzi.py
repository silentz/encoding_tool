from modules.painter import Painter
from modules.line import Line


class Encoder:

    def encode(self, data):
        lines = []
        current_element = 0
        for element in data:
            if element == '1':
                current_element = (current_element + 1) % 2
            lines.append(Line(current_element, blocks=2))
        return Painter(lines=lines)
