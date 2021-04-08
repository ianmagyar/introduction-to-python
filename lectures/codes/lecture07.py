class Product:
    def __init__(self):
        self.__price = 1000

    def __set_price(self, new):
        self.__price = new

    def sell(self):
        print("Was sold for {}".format(self.__price))

    def raise_price(self, rate):
        self.__price *= (1.0 + rate)
        # self.set_price(self.__price * (1.0 + rate))


t = Product()
t.sell()
# name mangling
t._Product__set_price(100)
t.sell()


class Product:
    def __init__(self):
        self.__price = 1000

    def set_price(self, new):
        self.__price = new

    def sell(self):
        print("Was sold for {}".format(self.__price))

    def raise_price(self, rate):
        self.__price *= (1.0 + rate)
        # self.set_price(self.__price * (1.0 + rate))


t = Product()
t.sell()
t.set_price(100)
t.sell()


class Person:
    def __init__(self, name):
        self.name = 'Bc. ' + name

    def print_name(self):
        print(self.name)


class Student(Person):
    def __init__(self, name, year):
        super().__init__(name)
        self.year = year


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)


p = Person("bla bla")
p.print_name()

s = Student('s bla', 1)
s.print_name()

t = Teacher("t bla")
t.print_name()


class Person:
    pass


class Worker(Person):
    pass


class Boss(Person):
    pass


class Manager(Worker, Boss):
    pass


class Secretary(Worker):
    pass


class BoardMember(Boss):
    pass


class CEO(Manager, BoardMember):
    pass


print(CEO.__mro__)
