data = open(path).read().split('\n')

path = '/'
files = {'/': 0}

for d in data[2:]:
    d = d.split()
    if d[0].isdigit():
        files[path] += int(d[0])
    elif d[-1] == 'ls':
        continue
    elif d[-1] == '..':
        path = '/'.join(path.split('/')[:-2]) + '/'
    elif d[1] == 'cd':
        path += d[-1] + '/'
    elif d[0] == 'dir':
        files[path + d[-1] + '/'] = 0

sums = {k: sum([files[l] for l in files if l.startswith(k)]) for k in files}
space = sums['/'] - 40000000

print(sum([sums[d] for d in sums if sums[d] <= 100000]))
print(min([sums[d] for d in sums if sums[d] >= space]))
