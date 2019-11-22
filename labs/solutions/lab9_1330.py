class HashTable:
    def __init__(self):
        pass

    def hash_function(self, value):
        pass

    def get(self, value):
        pass

    def has(self, value):
        pass

    def insert(self, value):
        pass

    def delete(self, value):
        pass

    def print_table(self):
        pass


class HashTableDict(HashTable):
    def __init__(self):
        HashTable.__init__(self)
        self.table = dict()

    def hash_function(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("You can only add numbers to this table")
        return round(value % 5)

    def get(self, value):
        if self.has(value):
            return value
        else:
            return None

    def has(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("This table only has numbers")
        key = self.hash_function(value)
        if key in self.table:
            return value in self.table[key]
        return False

    def insert(self, value):
        key = self.hash_function(value)
        try:
            self.table[key].append(value)
        except KeyError:
            self.table[key] = [value]

    def delete(self, value):
        key = self.hash_function(value)
        try:
            self.table[key].remove(value)
            return True
        except (KeyError, ValueError):
            return False

    def print_table(self):
        print(self.table)


class HashTableList(HashTable):
    def __init__(self):
        HashTable.__init__(self)
        self.table = [[], [], [], [], []]

    def hash_function(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("You can only add numbers to this table")
        return round(value % 5)

    def get(self, value):
        if self.has(value):
            return value
        else:
            return None

    def has(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("This table only has numbers")
        key = self.hash_function(value)
        return value in self.table[key]

    def insert(self, value):
        key = self.hash_function(value)
        self.table[key].append(value)

    def delete(self, value):
        key = self.hash_function(value)
        try:
            self.table[key].remove(value)
            return True
        except ValueError:
            return False

    def print_table(self):
        print(self.table)


if __name__ == '__main__':
    hash_table = HashTableList()
    values = [3, 4, 7, 2, 9, 1, 2.34, 68.5, 3, 1, 5, 9]
    for value in values:
        hash_table.insert(value)

    hash_table.delete(23)

    hash_table.print_table()
