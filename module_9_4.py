import random
from pprint import pprint

first = 'Мама мыла раму'
second = 'Рамена мало было'

lmbd = list(map(lambda x,y: x == y, first, second))

print(lmbd)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "a", encoding = 'utf8') as file:
            for x in data_set:
                if isinstance(x, str):
                    file.write(x)
                    file.write('\n')
                else:
                    for y in x:
                        if isinstance(y, str):
                            file.write(y)
                            file.write('\n')
                        elif isinstance(y, int):
                            file.write(str(y))
                            file.write('\n')


    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words


    def __call__(self):
        return random.choice(self.words)


# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())