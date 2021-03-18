# import math


# def is_prime(number):
#     if number % 2 == 0:
#         return False
#     for x in range(3, math.ceil(math.sqrt(number)), 2):
#         if number % x == 0:
#             return False
#     return True


# print(is_prime(9))
# print(is_prime(123475862311))



# steps = 0


# def fib(a):
#     global steps

#     steps += 1
#     # print("Calculating fib for", a)
#     if a == 0 or a == 1:
#         return 1
#     else:
#         return fib(a - 1) + fib(a - 2)


# n = 10
# print("The {}th Fibonacci number is".format(n), fib(n))
# print("Needed", steps, "steps to calculate it")
# print("-----")


# num_calls = 0


# def fib_smart(a, memo):
#     global num_calls

#     num_calls += 1
#     print("fib_smart called with", a)
#     if a not in memo:
#         memo[a] = fib_smart(a - 2, memo) + fib_smart(a - 1, memo)
#     return memo[a]


# memo = {0: 1, 1: 1}
# print("The {}th Fibonacci number is".format(n), fib_smart(n, memo))
# print("Needed", num_calls, "steps to calculate it")


# import numpy as np
# import matplotlib.pyplot as plt


# X = np.arange(0, 21)
# Y1 = X ** 2
# Y2 = 2 ** X

# plt.plot(X, Y1, marker='o', color='b')
# plt.plot(X, Y2, marker='x', color='r')
# plt.show()


def max_val(w, v, i, aW):
    # print("max_val called with", i, aW)
    global num_calls
    num_calls += 1
    if i == 0:
        if w[i] <= aW:
            return v[i]
        else:
            return 0
    without_i = max_val(w, v, i - 1, aW)

    if w[i] > aW:
        return without_i
    else:
        with_i = v[i] + max_val(w, v, i - 1, aW - w[i])

    return max(with_i, without_i)


# weights = [5, 3, 2]
# values = [9, 7, 8]
# knapsack_size = 5
# num_calls = 0
# res = max_val(weights, values, len(values) - 1, knapsack_size)
# print("Max Val is", res)
# print("Calculated in", num_calls, "steps")

# weights = [1, 5, 3, 4]
# values = [15, 10, 9, 5]
# knapsack_size = 8
# num_calls = 0
# res = max_val(weights, values, len(values) - 1, knapsack_size)
# print("Max Val is", res)
# print("Calculated in", num_calls, "steps")

weights = [1, 1, 5, 5, 3, 3, 4, 4]
values = [15, 15, 10, 10, 9, 9, 5, 5]
num_calls = 0
knapsack_size = 8
res = max_val(weights, values, len(values) - 1, knapsack_size)
print("Max Val is", res)
print("Calculated in", num_calls, "steps")

# weights = [
#     5, 5, 1, 8, 2, 9, 7, 5, 2, 8,
#     1, 2, 7, 3, 5, 7, 8, 5, 5, 8,
#     4, 6, 2, 8, 3, 7, 4, 2, 1, 9
# ]
# values = [
#     5, 5, 3, 5, 6, 7, 2, 3, 7, 1,
#     8, 3, 6, 8, 8, 6, 5, 6, 8, 4,
#     4, 7, 6, 8, 9, 1, 3, 5, 6, 4
# ]
# num_calls = 0
# knapsack_size = 40
# res = max_val(weights, values, len(values) - 1, knapsack_size)
# print("Max Val is", res)
# print("Calculated in", num_calls, "steps")

# 90, 28675705 steps

# with print
# weights = [1, 1, 5, 5, 3, 3, 4, 4]
# values = [15, 15, 10, 10, 9, 9, 5, 5]
# num_calls = 0
# knapsack_size = 8
# res = max_val(weights, values, len(values) - 1, knapsack_size)
# print("Max Val is", res)
# print("Calculated in", num_calls, "steps")


def fast_max_val(w, v, i, aW, m):
    global num_calls
    num_calls += 1

    try:
        return m[(i, aW)]
    except KeyError:
        if i == 0:
            if w[i] <= aW:
                m[(i, aW)] = v[i]
                return v[i]
            else:
                m[(i, aW)] = 0
                return 0

        without_i = fast_max_val(w, v, i - 1, aW, m)
        if w[i] > aW:
            m[(i, aW)] = without_i
            return without_i
        else:
            with_i = v[i] + fast_max_val(w, v, i - 1, aW - w[i], m)
        res = max(with_i, without_i)
        m[(i, aW)] = res
        return res


# weights = [1, 1, 5, 5, 3, 3, 4, 4]
# values = [15, 15, 10, 10, 9, 9, 5, 5]
# num_calls = 0
# knapsack_size = 8
# memo = {}
# res = fast_max_val(weights, values, len(values) - 1, knapsack_size, memo)
# print("Max Val is", res)
# print("Calculated in", num_calls, "steps")

# 90, 28675705 steps
weights = [
    5, 5, 1, 8, 2, 9, 7, 5, 2, 8,
    1, 2, 7, 3, 5, 7, 8, 5, 5, 8,
    4, 6, 2, 8, 3, 7, 4, 2, 1, 9
]
values = [
    5, 5, 3, 5, 6, 7, 2, 3, 7, 1,
    8, 3, 6, 8, 8, 6, 5, 6, 8, 4,
    4, 7, 6, 8, 9, 1, 3, 5, 6, 4
]
num_calls = 0
knapsack_size = 40
memo = {}
res = fast_max_val(weights, values, len(values) - 1, knapsack_size, memo)
print("Max Val is", res)
print("Calculated in", num_calls, "steps")
