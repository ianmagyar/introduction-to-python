# def exp1(a, b):
#     ans = 1
#     while (b > 0):
#         ans *= a
#         b -= 1
#     return ans


# def exp2(a, b):
#     if b == 1:
#         return a

#     if (b % 2) == 0:
#         return exp2(a * a, b / 2)
#     else:
#         return a * exp2(a, b - 1)


# def fib(a):
#     if a == 0 or a == 1:
#         return 1
#     else:
#         return fib(a - 1) + fib(a - 2)


from math import sqrt, ceil


def is_prime(number):
    for x in range(2, ceil(sqrt(number))):
        if number % x == 0:
            return False
    return True


# print(is_prime(8))
# print(is_prime(13))
# print(is_prime(123475862311))


steps = 0
n = 30


def fib_counter(a):
    global steps
    steps += 1
    # print("Calculating fib for", a)
    if a == 0 or a == 1:
        return 1
    else:
        return fib_counter(a - 1) + fib_counter(a - 2)


# print(fib_counter(n))
# print(steps, "calls")


def fib_smart(a, memo):
    global num_calls

    num_calls += 1
    # print("fib_smart called with", a)
    if a not in memo:
        memo[a] = fib_smart(a - 2, memo) + fib_smart(a - 1, memo)
    return memo[a]


memo = {0: 1, 1: 1}
num_calls = 0
print(fib_smart(n, memo))
print(num_calls, "calls")


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

# weights = [1, 1, 5, 5, 3, 3, 4, 4]
# values = [15, 15, 10, 10, 9, 9, 5, 5]
# num_calls = 0
# knapsack_size = 8
# res = max_val(weights, values, len(values) - 1, knapsack_size)
# print("Max Val is", res)
# print("Calculated in", num_calls, "steps")

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
# memo = {}
# res = fast_max_val(weights, values, len(values) - 1, knapsack_size, memo)
# print("Max Val is", res)
# print("Calculated in", num_calls, "steps")
