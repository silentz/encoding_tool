from modules.painter import Painter

class Encoder:

    def encode(self, data):
        new_sequence = []
        current_element = 0
        for element in data:
            if element == '1':
                current_element = (current_element + 1) % 2
            new_sequence.append(current_element)
        return Painter(data=new_sequence, height=2)
