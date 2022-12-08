data = open(path).read().split('\n')

g = [list(map(int,[*d])) for d in data]
count = 0
m = 0

for r in range(1, len(g) - 1):
    for c in range(1, len(g[0]) - 1):
        t = g[r][c]
        if t > max(g[r][:c]) or \
            t > max(g[r][c + 1:]) or \
            t > max([g[i][c] for i in range(0, r)]) or \
            t > max([g[i][c] for i in range(r + 1, len(g))]):
            count += 1
        
def vis(a, b, s, rc):
    count = 0
    for x in range(a, b, s):
        count += 1
        if g[x][c] >= g[r][c] and rc == 1 or \
           g[r][x] >= g[r][c] and rc == 2:
            break
    return count

    
for r in range(1, len(g) - 1):
    for c in range(1, len(g[0]) - 1):
        t = 1
        t *= vis(r - 1, -1, -1, 1)
        t *= vis(r + 1, len(g), 1, 1)
        t *= vis(c - 1, -1, -1, 2)
        t *= vis(c + 1, len(g[0]), 1, 2)
        if t > m:
            m = t
        
print(count + len(g) * 2 + len(g[0]) * 2 - 4)
print(m)
