test1 = [
    ('M', 34), ('F', 42), ('M', 23), ('F', 26), ('M', 42), ('F', 27),
    ('M', 17), ('F', 28), ('M', 32), ('F', 41), ('M', 56), ('F', 62),
    ('M', 28), ('F', 55), ('M', 33), ('F', 32), ('M', 26), ('F', 14),
    ('M', 19), ('F', 22), ('M', 21), ('F', 37), ('M', 38), ('F', 45),
    ('M', 34), ('F', 41), ('M', 29), ('F', 31), ('M', 30), ('F', 20),
    ('F', 52), ('F', 29), ('F', 38)
]


def validate_data(data_lst):
    # checks if data conforms to the rules:
    # input is a list of tuples, where
    # the first element must be a string (either M or F)
    # the second element is an integer bigger than zero
    # returns True if data are valid, False otherwise
    if type(data_lst) != list:
        return False

    for elem in data_lst:
        if type(elem) != tuple:
            return False
        if len(elem) != 2:
            return False
        if type(elem[0]) != str:
            return False
        if elem[0] not in ['M', 'F']:
            return False
        if type(elem[1]) != int:
            return False
        if elem[1] < 1:
            return False

    return True


def split_data(data_lst):
    # splits data into categories and stores them in a dictionary
    # returns the dictionary
    dict_result = dict()

    for cat, num in data_lst:
        if cat in dict_result:
            dict_result[cat].append(num)
        else:
            dict_result[cat] = [num]

    return dict_result


def calculate_averages(data):
    # calculates the average for all categories in a dictionary
    # returns the averages as a list of tuples with pairs: category - average
    if type(data) != dict:
        return None

    averages = list()

    for category, lst in data.items():
        cat_average = sum(lst) / len(lst)
        averages.append((category, cat_average))

    return averages


if __name__ == '__main__':
    if validate_data(dict()):
        data_dct = split_data(test1)
        print(data_dct)
        avgs = calculate_averages(data_dct)
        for cat, avg in avgs:
            print("Category {}, average: {:.2f}".format(cat, avg))
