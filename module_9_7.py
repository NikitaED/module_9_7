# Декоратор для проверки, является ли результат простым числом
def is_prime(func):
    def wrapper(*args, **kwargs):
        # Вызов основной функции
        result = func(*args, **kwargs)
        # Проверка простоты числа
        if result <= 1:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        return result

    return wrapper


# Функция для сложения 3 чисел
@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
