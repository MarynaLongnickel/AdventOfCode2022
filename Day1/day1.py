data = open(path).read()

cals = sorted([sum(list(map(int, x.split()))) for x in data.split('\n\n')])

print(max(cals))
print(sum(cals[-3:]))
