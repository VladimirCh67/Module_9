class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.pointer = start
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        else:
            self.step = step


    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step

        if self.step > 0 and self.pointer > self.stop:
            print('Перебор закончен')
            raise StopIteration()
        if self.step < 0 and self.pointer < self.stop:
            print('Перебор закончен')
            raise StopIteration()
        else:
            return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')

except StepValueError:
    print('Шаг указан неверно')

try:
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
        print()
except StepValueError:
    print('Шаг указан неверно')

try:
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
        print()
except StepValueError:
    print('Шаг указан неверно')

try:
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')
        print()
except StepValueError:
    print('Шаг указан неверно')
try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
        print()
except StepValueError:
    print('Шаг указан неверно')

