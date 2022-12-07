import numpy as np
threes = np.sum(
    np.arange(0, 1000, 3)
    )
fives = np.sum(
    np.arange(0, 1000, 5)
    )
fifteens = np.sum(
    np.arange(0, 1000, 15)
    )
total = (threes+fives) - fifteens
print(total)