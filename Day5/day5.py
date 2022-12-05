import re
import numpy as np
from copy import deepcopy

data = open(path).read().split('\n')

boxes = [[x for x in y[1::4]] for y in data[:8]]
boxes = [[y for y in ''.join(x).strip()] for x in np.rot90(boxes, 3)]

b = deepcopy(boxes)
b2 = deepcopy(boxes)

for d in data[10:]:
    m, f, t = list(map(int, re.findall('\d+', d)))
    b[t - 1].extend(b[f][-m:][::-1])
    b[f - 1] = b[f - 1][:-m]
    b2[t - 1].extend(b2[f][-m:])
    b2[f - 1] = b2[f - 1][:-m]
    
print(''.join([x[-1] for x in b]))
print(''.join([x[-1] for x in b2]))
