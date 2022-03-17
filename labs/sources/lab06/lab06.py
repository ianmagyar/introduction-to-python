test = ['F', 'F', 'B', 'B', 'F', 'B', 'B', 'F', 'F', 'B']
test2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
test3 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
test4 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']


def switch_to_one(cap_list):
    # given a list of characters that can take two values - F and B - flip
    # them so all elements are the same in the list
    # the goal is to find the smallest number of instructions
    pass


def switch_to_one_opt(cap_list):
    # given a list of characters that can take two values - F and B - flip
    # them so all elements are the same in the list
    # the goal is to find the smallest number of instructions
    # use only one pass through the list
    pass


def switch_to_one_hatless(cap_list):
    # given a list of characters that can take three values - F, B and H - flip
    # them so all elements are the same in the list or H
    # the goal is to find the smallest number of instructions
    pass


switch_to_one(test)
switch_to_one(test2)
switch_to_one(test3)

switch_to_one_opt(test)
switch_to_one_opt(test2)
switch_to_one_opt(test3)

switch_to_one_hatless(test4)
