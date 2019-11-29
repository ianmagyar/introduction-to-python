from matplotlib.pyplot import *
import random
import numpy as np

# plot([1, 2, 3, 4])
# show()

# plot([1, 2, 3, 4], [5, 6, 7, 8])
# show()

# plot([1, 2, 3, 4], [5, 6, 7, 8], 'ro')
# show()

# plot([1, 2, 3, 4], [5, 6, 7, 8], 'ro')
# plot([1, 2, 3, 4], [5, 6, 7, 8])
# show()


# plot([1, 2, 3, 4], [5, 6, 7, 8], 'ro')
# figure()
# plot([1, 2, 3, 4], [5, 6, 7, 8])
# title("Title of the graph")
# xlabel("x-axis label")
# ylabel("y-axis label")
# show()

# X = np.array([1, 2, 3, 4])
# Y = X ** 2
# plot(X, Y, 'rx')
# show()

vals = []
dieVals = [1, 2, 3, 4, 5, 6]
for i in range(10):
    vals.append(random.choice(dieVals))
hist(vals, bins=6)
show()
