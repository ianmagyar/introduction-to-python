from lab7 import *  # import lab7


def check_output(expected, real):
    if len(expected) != len(real):
        return False

    expected.sort(key=lambda tup: tup[0])
    real.sort(key=lambda tup: tup[0])

    return expected == real


def test_calculate_averages():
    test_case1 = {'M': [34, 34], 'F': [65]}
    result = calculate_averages(test_case1)
    assert check_output([('M', 34.0), ('F', 65.0)], result), "Unexpected output"

    test_case2 = {}
    result = calculate_averages(test_case2)
    assert check_output([], result), "Unexpected output"

    test_case3 = 5
    result = calculate_averages(test_case3)
    assert result is None, "Unexpected output; can't handle invalid input"


if __name__ == '__main__':
    test_calculate_averages()
