import random

with open('sample_inputs/large_matrix.in', 'w') as f:
    f.write("1000\n")
    b = []
    for i in range(1000):
        rand = []
        for j in range(1000):
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
