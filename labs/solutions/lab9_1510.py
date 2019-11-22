class HashTable:
    def __init__(self):
        pass

    def hash_function(self, value):
        pass

    def has(self, value):
        pass

    def insert(self, value):
        pass

    def delete(self, value):
        pass

    def get(self, value):
        pass

    def print_table(self):
        pass


class HashTableDict(HashTable):
    def __init__(self):
        HashTable.__init__(self)
        self.table = dict()

    def hash_function(self, value):
        return round(value % 5)

    def has(self, value):
        key = self.hash_function(value)
        if key in self.table:
            return value in self.table[key]
        return False

    def insert(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("You can only add numbers to the hash table")
        key = self.hash_function(value)
        if key in self.table:
            self.table[key].append(value)
        else:
            self.table[key] = [value]

    def delete(self, value):
        if self.has(value):
            key = self.hash_function(value)
            self.table[key].remove(value)
            return True
        return False

    def get(self, value):
        if self.has(value):
            return value
        return None

    def print_table(self):
        print(self.table)


class HashTableList(HashTable):
    def __init__(self):
        HashTable.__init__(self)
        self.table = [[], [], [], [], []]

    def hash_function(self, value):
        return round(value % 5)

    def has(self, value):
        key = self.hash_function(value)
        return value in self.table[key]

    def insert(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("You can only add numbers to the hash table")
        key = self.hash_function(value)
        self.table[key].append(value)

    def delete(self, value):
        if self.has(value):
            key = self.hash_function(value)
            self.table[key].remove(value)
            return True
        return False

    def get(self, value):
        if self.has(value):
            return value
        return None

    def print_table(self):
        print(self.table)


if __name__ == '__main__':
    hash_table = HashTableList()
    values = [4, 5, 2, 0, 9, 23.6, 47.5, 6, 3]
    for value in values:
        hash_table.insert(value)

    hash_table.print_table()
