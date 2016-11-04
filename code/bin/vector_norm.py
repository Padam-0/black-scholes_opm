import math

#||v|| = sqrt(v1^2 + v2^2 +... +vn^2)

def vectornorm(v):
    norm = 0
    for element in v:
        norm += element ** 2
    return math.sqrt(norm)