data = open(path).read().split('\n')

def get_pts(k):
    r = np.array([[0, 0] for i in range(k)])
    pts = []
    for d in data:
        d = d.split()
        for i in range(int(d[1])):
            if d[0] == 'R': r[0][0] += 1
            elif d[0] == 'L': r[0][0] += -1
            elif d[0] == 'U': r[0][1] += 1
            elif d[0] == 'D': r[0][1] += -1
            for i in range(len(r) - 1):
                x = r[i] - r[i + 1]
                if sum(x**2) >= 4:
                    r[i + 1] += np.sign(x)
            pts.append(','.join(map(str, r[-1])))
    return len(set(pts))

print(get_pts(2))
print(get_pts(10))
