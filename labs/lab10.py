import matplotlib.pyplot as plt
import random
import math
from numpy import arange


def calculatePi(inCircle, total):
    return 0.0


def isInCircle(x, y):
    return False


def plotEstimates(estimates):
    pass


def throwDarts(numDarts, shouldPlot):
    pass


def findPi(numDarts, shouldPlot=False):
    piGuess = throwDarts(numDarts, shouldPlot)
    print("Estimated value of pi with {} darts: {}".format(numDarts, piGuess))


if __name__ == '__main__':
    findPi(1000, True)
