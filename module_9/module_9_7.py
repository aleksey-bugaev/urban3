def is_prime(func):
    def wrapper(*args):
        i = func(*args)

        if i == 1:
            return "Составное"

        if int(pow(i, 1 / 2)) == 1:
            return "Простое"

        for n in range(2, int((i ** 0.5)) + 1):

            if i % n == 0:
                return "Составное"
            else:
                return "Простое"

    return wrapper


@is_prime
def sum_three(*args):
    result = sum(args)
    print(result)
    return result


result = sum_three(2, 3, 6)
print(result)
