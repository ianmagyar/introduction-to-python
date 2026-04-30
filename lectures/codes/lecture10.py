# Abstract Factory
class WindowsButton:
    def click(self):
        return "Windows Button clicked"

class MacButton:
    def click(self):
        return "Mac Button clicked"

class WindowsCheckbox:
    def check(self):
        return "Windows Checkbox checked"

class MacCheckbox:
    def check(self):
        return "Mac Checkbox checked"

class WindowsFactory:
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory:
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

class Application:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render(self):
        print(self.button.click())
        print(self.checkbox.check())

###

# Factory Method
class EmailNotification:
    def send(self, message):
        print("Sending Email: " + message)

class SMSNotification:
    def send(self, message):
        print("Sending SMS: " + message)

class NotificationCreator:
    def create_notification(self):
        pass

class EmailNotificationCreator(NotificationCreator):
    def create_notification(self):
        return EmailNotification()

class SMSNotificationCreator(NotificationCreator):
    def create_notification(self):
        return SMSNotification()

def app(creator, message):
    notification = creator.create_notification()
    notification.send(message)

###

# Builder
class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show(self):
        for item in self.items:
            print("- " + item)

class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def add_main_item(self):
        pass

    def add_drink(self):
        pass

    def add_dessert(self):
        pass

    def get_meal(self):
        return self.meal

class VegMealBuilder(MealBuilder):
    def add_main_item(self):
        self.meal.add_item("Veggie Burger")

    def add_drink(self):
        self.meal.add_item("Orange Juice")

    def add_dessert(self):
        self.meal.add_item("Fruit Salad")

class NonVegMealBuilder(MealBuilder):
    def add_main_item(self):
        self.meal.add_item("Chicken Sandwich")

    def add_drink(self):
        self.meal.add_item("Cola")

    def add_dessert(self):
        self.meal.add_item("Ice Cream")

class MealDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_meal(self):
        self.builder.add_main_item()
        self.builder.add_drink()
        self.builder.add_dessert()
        return self.builder.get_meal()

###

# Prototype
import copy

class Shape:
    def __init__(self):
        self.color = "Black"

    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        pass

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 5

    def draw(self):
        print("Drawing Circle with radius", self.radius, "and color", self.color)

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 5

    def draw(self):
        print("Drawing Rectangle with width", self.width, "height", self.height, "and color", self.color)

def app():
    original_circle = Circle()
    original_circle.color = "Red"

    cloned_circle = original_circle.clone()
    cloned_circle.radius = 10

    original_rectangle = Rectangle()
    original_rectangle.color = "Blue"

    cloned_rectangle = original_rectangle.clone()
    cloned_rectangle.width = 20

    print("Original Circle:")
    original_circle.draw()

    print("Cloned Circle:")
    cloned_circle.draw()

    print("\nOriginal Rectangle:")
    original_rectangle.draw()

    print("Cloned Rectangle:")
    cloned_rectangle.draw()

###

# Adapter
class OldPrinter:
    def old_print(self, text):
        print("Printing from OldPrinter:", text)

class Printable:
    def print_text(self, text):
        pass

class PrinterAdapter(Printable, OldPrinter):
    def print_text(self, text):
        self.old_print(text)

def app(printer):
    printer.print_text("Hello, Adapter Pattern!")

###

# Bridge
class DrawingAPI1:
    def draw_circle(self, x, y, radius):
        print("API1 drawing circle at ({}, {}) with radius {}".format(x, y, radius))

class DrawingAPI2:
    def draw_circle(self, x, y, radius):
        print("API2 drawing circle at ({}, {}) with radius {}".format(x, y, radius))

class Shape:
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    def draw(self):
        pass

    def resize_by_percentage(self, percent):
        pass

class CircleShape(Shape):
    def __init__(self, x, y, radius, drawing_api):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def resize_by_percentage(self, percent):
        self.radius *= percent / 100.0

###

# Decorator
class Text:
    def __init__(self, content):
        self._content = content

    def render(self):
        return self._content

class TextDecorator:
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return self._wrapped.render()

class BoldDecorator(TextDecorator):
    def render(self):
        return "<b>" + self._wrapped.render() + "</b>"

class ItalicDecorator(TextDecorator):
    def render(self):
        return "<i>" + self._wrapped.render() + "</i>"

class UnderlineDecorator(TextDecorator):
    def render(self):
        return "<u>" + self._wrapped.render() + "</u>"

###

# Facade
class CPU:
    def freeze(self):
        print("Freezing processor")

    def jump(self, position):
        print("Jumping to address", position)

    def execute(self):
        print("Executing instructions")

class Memory:
    def load(self, position, data):
        print("Loading data '{}' into address {}".format(data, position))

class HardDrive:
    def read(self, sector):
        print("Reading data from sector", sector)
        return "boot_data"

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        data = self.hard_drive.read("0x1FF")
        self.memory.load("0x00", data)
        self.cpu.jump("0x00")
        self.cpu.execute()

def startup():
    computer = Computer()
    computer.start()

###

# Proxy
class Document:
    def display(self):
        pass

class ConfidentialReport(Document):
    def display(self):
        print("ConfidentialReport: Displaying sensitive content")

class ReportProxy(Document):
    def __init__(self, real_report):
        self.real_report = real_report
        self.access_granted = False

    def login(self, password):
        if password == "admin123":
            self.access_granted = True

    def display(self):
        if self.access_granted:
            print("ReportProxy: Access granted")
            self.real_report.display()
        else:
            print("ReportProxy: Access denied")

def login():
    report = ConfidentialReport()
    proxy = ReportProxy(report)

    print("Trying to view without login:")
    proxy.display()

    print("\nLogging in and trying again:")
    proxy.login("admin123")
    proxy.display()

###

# Chain of responsibility
class Support:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle_request(self, level, message):
        pass

class BasicSupport(Support):
    def handle_request(self, level, message):
        if level == "basic":
            print("BasicSupport: Handling -", message)
        elif self.next_handler:
            self.next_handler.handle_request(level, message)

class ManagerSupport(Support):
    def handle_request(self, level, message):
        if level == "intermediate":
            print("ManagerSupport: Handling -", message)
        elif self.next_handler:
            self.next_handler.handle_request(level, message)

class DirectorSupport(Support):
    def handle_request(self, level, message):
        if level == "advanced":
            print("DirectorSupport: Handling -", message)
        elif self.next_handler:
            self.next_handler.handle_request(level, message)

def app():
    basic = BasicSupport()
    manager = ManagerSupport()
    director = DirectorSupport()

    basic.set_next(manager).set_next(director)

    basic.handle_request("basic", "Reset password")
    basic.handle_request("intermediate", "Approve refund")
    basic.handle_request("advanced", "Negotiate contract")
    basic.handle_request("unknown", "Unknown issue")

###

# Command
class Action:
    def execute(self):
        pass

class LightOnCommand(Action):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Action):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class MusicPlayCommand(Action):
    def __init__(self, music_player):
        self.music_player = music_player

    def execute(self):
        self.music_player.play()

class MusicStopCommand(Action):
    def __init__(self, music_player):
        self.music_player = music_player

    def execute(self):
        self.music_player.stop()

class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

class MusicPlayer:
    def play(self):
        print("Music is playing")

    def stop(self):
        print("Music has stopped")

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

def smart_house():
    light = Light()
    music_player = MusicPlayer()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    play_music = MusicPlayCommand(music_player)
    stop_music = MusicStopCommand(music_player)

    remote = RemoteControl()

    remote.set_command(light_on)
    remote.press_button()

    remote.set_command(play_music)
    remote.press_button()

    remote.set_command(stop_music)
    remote.press_button()

    remote.set_command(light_off)
    remote.press_button()

###

# Mediator
class Mediator:
    def send(self, message, colleague):
        pass

class ChatRoom(Mediator):
    def __init__(self):
        self.colleagues = []

    def add_colleague(self, colleague):
        self.colleagues.append(colleague)

    def send(self, message, colleague):
        for c in self.colleagues:
            if c != colleague:
                c.receive(message)

class Colleague:
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name
        mediator.add_colleague(self)

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send(message, self)

    def receive(self, message):
        print(f"{self.name} receives: {message}")

if __name__ == "__main__":
    chatroom = ChatRoom()

    john = Colleague(chatroom, "John")
    jane = Colleague(chatroom, "Jane")
    alice = Colleague(chatroom, "Alice")

    john.send("Hi everyone!")
    jane.send("Hello John!")
    alice.send("Hey John and Jane!")

###

# Observer
class Observer:
    def update(self, temperature):
        pass

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self._notify_observers()

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"PhoneDisplay: The current temperature is {temperature}°C.")

class LaptopDisplay(Observer):
    def update(self, temperature):
        print(f"LaptopDisplay: The current temperature is {temperature}°C.")

class WindowDisplay(Observer):
    def update(self, temperature):
        print(f"WindowDisplay: The current temperature is {temperature}°C.")

###

# Strategy
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Bitcoin.")

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        self._strategy.pay(amount)

if __name__ == "__main__":
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()
    bitcoin_payment = BitcoinPayment()

    payment_context = PaymentContext(credit_card_payment)
    payment_context.execute_payment(100)

    payment_context.set_strategy(paypal_payment)
    payment_context.execute_payment(150)

    payment_context.set_strategy(bitcoin_payment)
    payment_context.execute_payment(200)

###

# Visitor
class Item:
    def accept(self, visitor):
        pass

class Electronics(Item):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        visitor.visit_electronics(self)

class Clothing(Item):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        visitor.visit_clothing(self)

class TaxVisitor:
    def visit_electronics(self, electronics):
        pass

    def visit_clothing(self, clothing):
        pass

class USATaxVisitor(TaxVisitor):
    def visit_electronics(self, electronics):
        tax = electronics.price * 0.10
        print(f"USA Tax on Electronics: ${tax:.2f} for ${electronics.price}")

    def visit_clothing(self, clothing):
        tax = clothing.price * 0.05
        print(f"USA Tax on Clothing: ${tax:.2f} for ${clothing.price}")

class CanadaTaxVisitor(TaxVisitor):
    def visit_electronics(self, electronics):
        tax = electronics.price * 0.13
        print(f"Canada Tax on Electronics: ${tax:.2f} for ${electronics.price}")

    def visit_clothing(self, clothing):
        tax = clothing.price * 0.08
        print(f"Canada Tax on Clothing: ${tax:.2f} for ${clothing.price}")

if __name__ == "__main__":
    electronics = Electronics(1000)
    clothing = Clothing(50)

    usa_tax_visitor = USATaxVisitor()
    canada_tax_visitor = CanadaTaxVisitor()

    print("Calculating Taxes in the USA:")
    electronics.accept(usa_tax_visitor)
    clothing.accept(usa_tax_visitor)

    print("\nCalculating Taxes in Canada:")
    electronics.accept(canada_tax_visitor)
    clothing.accept(canada_tax_visitor)
