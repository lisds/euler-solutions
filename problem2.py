import numpy as np


fibonacci = np.zeros(33)
fibevens = np.zeros(33)

pos = 2
fibonacci[0] = 1
fibonacci[1] = 2

for i in np.arange(2, 32):
    magicnum = fibonacci[pos-1] + fibonacci[pos-2]
    fibonacci[i] = magicnum
    pos = pos + 1
    if fibonacci[i] >= 3000000:
        break
for v in np.arange(33):
    if fibonacci[v]%2 == 0:
        fibevens[v] = fibonacci[v]
    else:
        pass
answer = np.sum(fibevens)
print(answer)