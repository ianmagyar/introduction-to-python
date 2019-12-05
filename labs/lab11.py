import random
from math import sqrt, pi, cos, sin
import matplotlib.pyplot as plt
from time import sleep


class Location:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def move(self, dx, dy):
        return Location(self.x + float(dx), self.y + float(dy))

    def getCoords(self):
        return self.x, self.y

    def getDistance(self, other):
        o_x, o_y = other.getCoords()
        xDist = self.x - o_x
        yDist = self.y - o_y
        return sqrt(xDist ** 2 + yDist ** 2)


class Direction:
    def __init__(self, angle):
        # TODO: set angle, normalize for range 0 - 2pi
        pass

    def move(self, dist):
        # TODO: return difference in x and y values
        return (-1, -1)

    def getAngle(self):
        return self.angle


class Field:
    def __init__(self, human, mosquito):
        self.human = human
        self.mosquito = mosquito

    def moveHuman(self):
        self.human.move()

    def moveMosquito(self):
        self.mosquito.move()

    def getHumanCoords(self):
        return self.human.getCoords()

    def getMosquitoCoords(self):
        return self.mosquito.getCoords()

    def getHuman(self):
        return self.human

    def getMosquito(self):
        return self.mosquito

    def getActorDistance(self):
        # TODO: return distance between human and mosquito
        return 0

    def found(self):
        # TODO: return if mosquito found human (distance between them < 2)
        return False


class Actor:
    def __init__(self, name, speed, x, y):
        self.name = name
        self.speed = speed
        self.field = None
        self.loc = Location(x, y)

    def isPathClear(self):
        pass

    def move(self):
        pass

    def getCoords(self):
        return self.loc.getCoords()

    def getLoc(self):
        return self.loc


class Human(Actor):
    def __init__(self, name, speed, x, y):
        Actor.__init__(self, name, speed, x, y)

    def move(self):
        # TODO: take a step in a random direction
        pass


class Mosquito(Actor):
    def __init__(self, name, speed, x, y):
        Actor.__init__(self, name, speed, x, y)
        self.found_prey = False
        self.field = None
        self.lastDistance = None
        self.lastDirection = None
        self.changes = list()

    def setField(self, field):
        self.field = field

    def move(self):
        # TODO: implement mosquito's movement
        # while distance > 90 - random directions
        # if distance < 90 - found human scent
        # fly in random direction - if scent stronger, continue
        # if scent weaker, turn around
        # if scent is lost, fly in random direction
        pass


def performTrial():
    human_x = random.randint(-50, 50)
    human_y = random.randint(-50, 50)
    human = Human("Janko Hrasko", 1, human_x, human_y)
    mosquito = Mosquito("Mosquito", 1, 10, 10)
    field = Field(human, mosquito)
    mosquito.setField(field)

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([-100, 100])
    ax.set_ylim([-100, 100])

    human_pos = field.getHumanCoords()
    mosquito_pos = field.getMosquitoCoords()

    human_plot_point, = ax.plot(human_pos, 'bo')
    mosquito_plot_point, = ax.plot(mosquito_pos, 'rx')
    fig.canvas.draw()
    fig.canvas.flush_events()

    while not field.found():
        human_pos = field.getHumanCoords()
        mosquito_pos = field.getMosquitoCoords()

        human_plot_point.set_xdata(human_pos[0])
        human_plot_point.set_ydata(human_pos[1])

        mosquito_plot_point.set_xdata(mosquito_pos[0])
        mosquito_plot_point.set_ydata(mosquito_pos[1])
        fig.canvas.draw()
        fig.canvas.flush_events()
        field.moveMosquito()
        sleep(0.1)


if __name__ == '__main__':
    performTrial()
