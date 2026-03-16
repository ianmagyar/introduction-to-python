test_intervals1 = [
    ('Daniel', 7, 9),
    ('Palo', 8, 11),
    ('Danka', 10, 12),
    ('Miro', 9, 1),
    ('Lubos', 11, 12),
    ('Milan', 10, 12),
    ('Noro', 9, 11),
    ('Radka', 8, 10),
    ('Martina', 7, 8),
    ('Peto', 9, 11)
]
test_intervals2 = [
    ('Daniel', 10, 12),
    ('Palo', 9, 12),
    ('Danka', 10, 12),
    ('Miro', 9, 1),
    ('Lubos', 10, 11),
    ('Milan', 11, 2),
    ('Noro', 10, 1),
    ('Radka', 9, 12),
    ('Martina', 9, 11),
    ('Peto', 9, 1),
    ('Julka', 10, 12),
    ('Riso', 10, 11),
    ('Mato', 11, 3),
    ('Brano', 10, 1),
    ('David', 9, 11)
]
test_intervals_weights = [
    ('Daniel', 8, 10, 1),
    ('Palo', 8, 11, 2),
    ('Danka', 8, 9, 3),
    ('Miro', 11, 1, 4),
    ('Lubos', 9, 12, 2),
    ('Milan', 10, 12, 2),
    ('Noro', 10, 3, 1),
    ('Radka', 11, 12, 2),
    ('Martina', 10, 12, 1),
    ('Peto', 8, 11, 2)
]


def load_intervals(intervals):
    # returns a list of intervals as tuples
    pass


def choose_time(interval_list):
    # return best time to party and number of friends present
    pass


def when_to_go(friends_list):
    # process intervals from list
    # call function to calculate best time for party
    # print results
    pass


def choose_time_constrained(interval_list, y_start, y_end):
    # return best time to party and number of friends present
    # look only in interval <y_start, y_end)
    pass


def choose_time_with_weights(interval_list):
    # return best time to party and total weight
    pass
