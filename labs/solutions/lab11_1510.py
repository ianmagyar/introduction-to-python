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
        if angle < 0:
            self.angle = angle + 2 * pi
        elif angle > 2 * pi:
            self.angle = angle - 2 * pi
        else:
            self.angle = angle

    def move(self, dist):
        xDist = dist * cos(self.angle)
        yDist = dist * sin(self.angle)
        return (xDist, yDist)

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
        return self.human.getLoc().getDistance(self.mosquito.getLoc())

    def found(self):
        return self.getActorDistance() < 2


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
        direction = Direction(random.random() * 2 * pi)
        dx, dy = direction.move(self.speed)
        self.loc = self.loc.move(dx, dy)


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
        if self.field is None:
            return

        distance = self.field.getActorDistance()
        if self.lastDistance is None:
            self.lastDistance = distance

        if distance < 90:
            self.found_prey = True
        else:
            self.found_prey = False

        if not self.found_prey or self.lastDirection is None:
            direction = Direction(random.random() * 2 * pi)
        elif distance < self.lastDistance:
            self.changes.append(-1)
            direction = self.lastDirection
        else:
            self.changes.append(1)
            if len(self.changes) > 4 and self.changes[-4:] == [-1, 1, -1, 1]:
                direction = Direction(random.random() * 2 * pi)
            else:
                direction = Direction(self.lastDirection.getAngle() + pi)

        dx, dy = direction.move(self.speed)
        self.loc = self.loc.move(dx, dy)
        self.lastDistance = distance
        self.lastDirection = direction


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
    counter = 1

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
        if not counter % 10:
            field.moveHuman()
        counter += 1
        sleep(0.1)

    sleep(3)


if __name__ == '__main__':
    performTrial()
