data = open(path).read()

for n in (4, 14):
    for i in range(len(data)):
        s = data[i : i + n]
        if len(set(s)) == len(s):
            print(i + n)
            break
