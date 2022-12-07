import numpy as np


fibonacci = np.zeros(51)
#creates an empty array for the sequence to go in to

pos = 2
#pos is the current position which needs to equal the sum of the 2 positions before that. We need to assign the first two positions of the sequence to 1 and 2, then start at 3

fibonacci[0] = 1
fibonacci[1] = 2
#first 2 numbers are set, now loop needs to start us at current pos, add the two positions prior, set current pos to the sum, then move the position up one


for i in np.arange(2, 50):
    magicnum = fibonacci[pos-1] + fibonacci[pos-2]
    fibonacci[i] = magicnum
    pos = pos + 1
    if fibonacci[i] >= 4000000:
        break
