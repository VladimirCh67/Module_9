def is_prime(func):
    def wrapper(a, b, c):
        x = func(a, b, c)
        print(x)
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                return "Составное"
        return "Простое"
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(4, 7, 6)
print(result)

