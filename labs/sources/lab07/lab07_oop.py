class HashTable:
    def __init__(self):
        self.table = dict()

    def hash_function(self, number):
        # number is an integer or float
        # calculates and returns hash value for number
        pass

    def insert(self, number):
        # number is an integer or float
        # adds number into the hash table under its hash value
        pass

    def has(self, number):
        # number is an integer or float
        # returns True if number is in hash table, False otherwise
        pass

    def get(self, number):
        # number is an integer or float
        # returns number if number is in hash table, None otherwise
        pass

    def delete(self, number):
        # number is an integer or float
        # deletes number from table
        # returns True if number was deleted, False if number was not in table
        pass


if __name__ == '__main__':
    hash_table = HashTable()
    numbers = [3, 4, 7, 2, 9, 1, 2.34, 68.5, 3, 1, 5, 9]
    for number in numbers:
        hash_table.insert(number)
        print(hash_table.table)

    print(hash_table.has(7))
    print(hash_table.delete(7))
    print(hash_table.table)

    assert hash_table.has(4) is True
    assert hash_table.has(68.5) is True
    assert hash_table.has(19) is False
    assert hash_table.has(0.38) is False

    assert hash_table.delete(4) is True
    assert hash_table.delete(4) is False
    assert hash_table.delete(23) is False
