from modules.painter import Painter


class Encoder:

    def encode(self, data):
        return Painter(data=[int(x) for x in data], height=2)
