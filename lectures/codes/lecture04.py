# a = 3
# number = 10
# divide_by = 0

# try:
#     print(number / divide_by)
#     a += 1
# except ZeroDivisionError:
#     print("You're trying to divide by zero")
# except NameError:
#     print("You're trying to use a non-existent variable")
# else:
#     print("Everything went well")
# finally:
#     print(a)
#     print("I still get printed")

# my_dict = dict()
# if 'a' not in my_dict:
#     my_dict['a'] = 1
# else:
#     my_dict['a'] += 1

# try:
#     my_dict['a'] += 1
# except KeyError:
#     my_dict['a'] = 1

# print(my_dict)


# def error_func():
#     # try:
#     #     raise ValueError
#     # except ValueError:
#     #     print("handling in error_func")
#     number = 10
#     divide_by = 0
#     if divide_by == 0:
#         raise ZeroDivisionError("Chces delit 0")

#     return number / divide_by


# def calling_func():
#     try:
#         error_func()
#     except ZeroDivisionError:
#         print("handling in calling_func()")


# calling_func()


# class MyException(Exception):
#     def __init__(self, expression, message):
#         self.expression = expression
#         self.message = message


# def my_func(number, divide_by):
#     try:
#         print(number / divide_by)
#     except ZeroDivisionError:
#         raise MyException("Chces delit 0", "Chces delit 0")


# try:
#     my_func(10, 0)
# except MyException:
#     print("spracuje sa vynimka")


def is_even(number):
    if not isinstance(number, int):
        return -1

    return number % 2 == 0


# assert is_even(7) is False
# assert is_even(4) is True
# assert is_even(4.6) == -1


def is_palindrome(word):
    original_list = [let for let in word]
    test_list = original_list.copy()
    test_list.reverse()
    return test_list == original_list


# print(is_palindrome("abcba"))
# print(is_palindrome("abcde"))
