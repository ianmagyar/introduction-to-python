def power(number, power_param=2, print_result=False):
    result = number ** power_param

    if print_result:
        print(result)

    return result


# print(power(10, print_result=True))


def square(number: int) -> int:
    """
    Returns the square of a number (integer).
    """
    if type(number) != int:
        return -1

    return number ** 2


# a = 5
# print(square(a))
# print(square(a))


def void_function():
    print("Hello")


# print(void_function())


def function2():
    return 1, 2


# val1, val2 = function2()
# print(val1)
# print(val2)

# val = function2()
# print(val)


def cube(number: int) -> int:
    return number ** 3


x = 4
# print(eval("x * x"))
# print(x * x)

# func = input("Please enter a function: ")
# for number in range(1, 11):
#     print(eval(func))

# func = cube
# print(func(5))


def is_palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True

    return string[0] == string[-1] and is_palindrome(string[1:-1])


# print(is_palindrome(""))
# print(is_palindrome("a"))
# print(is_palindrome("abc"))
# print(is_palindrome("abacaba"))


def get_fib(n):
    if n == 0 or n == 1:
        return n

    return get_fib(n - 2) + get_fib(n - 1)


# print(get_fib(0))
# print(get_fib(1))
# print(get_fib(2))
# print(get_fib(3))
# print(get_fib(10))


def barnyard(heads, legs):
    for chicken in range(0, heads + 1):
        rabbits = heads - chicken
        if 2 * chicken + 4 * rabbits == legs:
            return chicken, rabbits


# print(barnyard(48, 128))


def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        c = a + b
        a, b = b, c


# gen = fib_generator()
# for _ in range(1000):
#     print(next(gen))


my_list = [1, 5, 4, 8, 3, 7, 13, 28, 45]
new_list = list(filter(lambda x: x % 2 == 0, my_list))
print(new_list)

my_list2 = ["id0", "id18", "id24", "id3", "id4"]
print(sorted(my_list2))
print(sorted(my_list2, key=lambda x: int(x[2:])))

my_list3 = [
    {"name": "A B", "age": 23},
    {"name": "D A", "age": 31},
    {"name": "E H", "age": 27},
    {"name": "F G", "age": 48},
    {"name": "C B", "age": 16},
]
print(sorted(my_list3, key=lambda x: x['age']))
