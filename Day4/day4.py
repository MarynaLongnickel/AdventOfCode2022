data = open(path).read().split('\n')

pairs = [[list(map(int, y[0].split('-'))), list(map(int, y[1].split('-')))] for y in [x.split(',') for x in data]]

c1, c2 = 0, 0

for s in pairs:
    if (s[0][0] <= s[1][0] and s[0][1] >= s[1][1]) or \
       (s[0][0] >= s[1][0] and s[0][1] <= s[1][1]): 
        c1 += 1

for s in pairs:
    if not((s[1][0] > s[0][1]) or (s[1][1] < s[0][0])): 
        c2 += 1
        
print(c1, c2)
