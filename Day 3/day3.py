data = open(path).read().split('\n')

l = [list(set(x[:len(x)//2]).intersection(set(x[len(x)//2:])))[0] for x in data]
l2 = [list(set(data[x:x+3][0]).\
          intersection(set(data[x:x+3][1])).\
          intersection(set(data[x:x+3][2])))[0] for x in range(0, len(data), 3)]

print(sum([ord(i) - 96 if i.islower() else ord(i) - 38 for i in l]))
print(sum([ord(i) - 96 if i.islower() else ord(i) - 38 for i in l2]))
