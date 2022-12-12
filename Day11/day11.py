data = [x.replace(',', ' ').split(' ') for x in open(path).read().split('\n')]

def get_ans(rounds):
    m = [[] for _ in range(8)]
    p = [0] * 8
    l = np.prod([int(data[x][-1]) for x in range(3, len(data), 7)])
    c = 0
    r = 1

    for r in range(rounds):
        c = 0
        for i in range(0, len(data), 7):
            if r == 1:
                m[c].extend([x for x in data[i+1] if x.isdigit()])
            for n in m[c]:
                p[c] += 1
                if data[i+2][-1] == 'old':
                    if rounds > 21:
                        x = str(int(int(n)*int(n) % l))
                    else:
                        x = str(int(int(n)*int(n) / 3))
                else:
                    if rounds > 21:
                        x = str(int(eval(n + ''.join(data[i+2][-2:])) % l))
                    else:
                        x = str(int(eval(n + ''.join(data[i+2][-2:])) / 3))
                if int(x) % int(data[i+3][-1]) == 0:
                    m[int(data[i+4][-1])].append(x)
                else:
                    m[int(data[i+5][-1])].append(x)
                m[c] = []
            c += 1
    print(sorted(p)[-1] * sorted(p)[-2])

get_ans(21)
get_ans(10001)
