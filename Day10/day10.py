data = [x.split(' ') for x in open(path).read().split('\n')]

c = 0
x = 1
a = []

for d in data:
    if d[0] == 'addx':
        for _ in range(2):
            c += 1
            if (c - 20) % 40 == 0:
                a.append(abs(x * c))
        x += int(d[1])
    elif d[0] == 'noop':
        c += 1
        if (c - 20) % 40 == 0:
            a.append(abs(x * c))
            
sum(a)
