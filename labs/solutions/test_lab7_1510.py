from lab7 import *


def check_result(expected, real):
    if len(expected) != len(real):
        return False

    expected.sort(key=lambda x: x[0])
    real.sort(key=lambda x: x[0])

    for i in range(len(expected)):
        if expected[i][0] != real[i][0] or expected[i][1] != real[i][1]:
            return False

    return True


def test_calculate_averages():
    test1 = {'M': [34, 34], 'F': [56]}
    result = calculate_averages(test1)
    assert check_result([('F', 56.0), ('M', 34.0)], result), "Incorrect output"

    test2 = dict()
    result = calculate_averages(test2)
    assert result == list(), "Could not process empty dictionary"

    test3 = 5
    result = calculate_averages(test3)
    assert result is None, "Could not process input of wrong type"


if __name__ == '__main__':
    test_calculate_averages()
