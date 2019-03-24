class Node:
    def __init__(self):
        self.offset: int = 0
        self.length: int = 0
        self.char: str = str()


class Coder:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.result = []

    def encode(self):
        while self.pos < len(self.text):

            length = 0
            start_pos = -1
            not_found = True
            node = Node()

            for i in range(self.pos, len(self.text)):
                node = Node()

                # Поиск совпадений
                count = self.text.rfind(self.text[self.pos:self.pos + length + 1], 0, self.pos)

                if count >= 0:
                    length += 1
                    start_pos = count
                    not_found = False

            if not_found:
                # Если совпадений нет, то просто записываем текущий символ
                node.char = self.text[self.pos]
                self.pos += 1

                self.result.append(node)

            else:
                if self.pos + length < len(self.text):
                    node.offset = self.pos - start_pos
                    node.length = length
                    node.char = self.text[self.pos+length]

                    self.pos += length + 1
                    self.result.append(node)

    def decode(self):
        decoded_string = str()

        for node in self.result:
            if node.offset == 0 and node.length == 0:
                decoded_string += node.char
            else:
                decoded_string += decoded_string[len(decoded_string) - node.offset: len(decoded_string) - node.offset +
                                  node.length] + node.char

        print(decoded_string)


if __name__ == '__main__':
    coder = Coder(text='sir_sid_eastman_r')
    coder.encode()
    coder.decode()