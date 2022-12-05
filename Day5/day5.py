import re
import numpy as np
from copy import deepcopy

data = open(path).read().split('\n')

boxes = [[x for x in y[1::4]] for y in data[:8]]
boxes = np.rot90(boxes, 3)
boxes = list([list([y for y in ''.join(x).strip()]) for x in boxes])

b = deepcopy(boxes)
b2 = deepcopy(boxes)

for d in data[10:]:
    n = list(map(int, re.findall('\d+', d)))
    m, f, t = n[0], n[1] - 1, n[2] - 1
    b[t].extend(b[f][-m:][::-1])
    b[f] = b[f][:-m]
    b2[t].extend(b2[f][-m:])
    b2[f] = b2[f][:-m]
    
print(''.join([x[-1] for x in b]))
print(''.join([x[-1] for x in b2]))
