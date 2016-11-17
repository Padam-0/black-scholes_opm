import random

with open('large_matrix.in', 'w') as f:
    f.write("4000\n")
    b = []
    for i in range(4000):
        rand = []
        for j in range(4000):
            if random.random() > 0.8:
                rand.append(random.randint(1,9))
            else:
                rand.append(0)
        pivot = sum(rand) + 1
        rand[i] = pivot
        f.write(' '.join(["%s" % (str(value)) for value in rand]))
        f.write("\n")
        b.append(random.randint(1,9))
    f.write(' '.join(["%s" % (str(value)) for value in b]))
