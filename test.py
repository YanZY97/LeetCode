import re

a = ' 0.2 21.013, 0.5  0.6啊0.5, 2    .9kjhljklkjl'
b = re.findall(r"[0-9]+\.[0-9]+|\.*[0-9]+", a)
c = ' '.join(i for i in b)
# print(c)


class Trainer:
    def __init__(self, usage):
        self.usage = usage

    def upload_data(self):
        print(self.usage)


