from modules.commander import Commander


class Encoder:

    def encode(self, data):
        return Commander(data=[int(x) for x in data], height=2)
