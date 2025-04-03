class Product:
    counter = 0

    def __init__(self, price, name):
        self.__price = price
        self.name = name
        self.id = Product.counter
        Product.counter += 1

    def __eq__(self, other):
        return self.id == other.id

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def get_counter(self):
        return Product.counter


# print(Product.counter)
# test1 = Product(500, "abc")
# print(test1.get_price())
# test1.__price = 2000
# print(test1.get_price())
# test1.set_price(1000)
# print(test1.get_price())
# test2 = Product(750, "abc")
# print(test1.id)
# print(test2.id)

# print(test1 == test2)
# print(test1.name)
# print(test1.get_price())
# print(test1.get_price())
# print(test1.get_counter())
# print(Product.counter)
# print(test1.counter)

# test2 = Product(750, "def")
# print(test2.get_price())
# print(test2.get_counter())

# print(test1.get_price())
# print(test1.get_counter())


class Person:
    def __init__(self, name):
        print('setting name in person')
        self.name = name

    def calculate(self):
        return 8


class Student(Person):
    def __init__(self, name, year):
        # print('setting name in student')
        # self.name = name
        super().__init__(name)
        self.year = year

    def calculate(self):
        return super().calculate() * 2

    def __str__(self):
        return "Student " + self.name


# student = Student("John Doe", 1)
# print(student)
# print(type(student))
# print(isinstance(student, Person))
# print(student.name)
# print(student.year)
# print(student.calculate())
# print(Student.calculate(student))
# print(dir(student))
# print(dir(Student))

# person = Person("John Doe")
# print(type(person))
# print(person.name)
# print(person.year)  # AttributeError
# print(person.calculate())
