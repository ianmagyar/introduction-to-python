def hash_function(number):
    # number is an integer or float
    # calculates and returns hash value for number
    pass


def insert(table, number):
    # table is a hash table of type dict
    # number is an integer or float
    # adds number into the hash table under its hash value
    pass


def has(table, number):
    # table is a hash table of type dict
    # number is an integer or float
    # returns True if number is in hash table, False otherwise
    pass


def get(table, number):
    # table is a hash table of type dict
    # number is an integer or float
    # returns number if number is in hash table, None otherwise
    pass


def delete(table, number):
    # table is a hash table of type dict
    # number is an integer or float
    # deletes number from table
    # returns True if number was deleted, False if number was not in table
    pass


if __name__ == '__main__':
    hash_table = dict()
    numbers = [3, 4, 7, 2, 9, 1, 2.34, 68.5, 3, 1, 5, 9]
    for number in numbers:
        insert(hash_table, number)
        print(hash_table)

    print(has(hash_table, 7))
    print(delete(hash_table, 7))
    print(hash_table)

    assert has(hash_table, 4) is True
    assert has(hash_table, 68.5) is True
    assert has(hash_table, 19) is False
    assert has(hash_table, 0.38) is False

    assert delete(hash_table, 4) is True
    assert has(hash_table, 4) is False
    assert delete(hash_table, 23) is False
