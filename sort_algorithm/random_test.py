#"""rando test"""

import random
import math
def random_new(a,b):
    z=b-a+1
    while z > b-a:
        z=0
        for i in range(int(math.ceil(math.log(b-a+1)/math.log(2)))):
            z=z*2+random.randint(0,1)
    return z+a

def bias_random(p):
    if random.random() <p:
        return 1
    else:
        return 0

def justify_random(p):
    a=bias_random(p)
    b=bias_random(p)
    while a+b != 1:
        a=bias_random(p)
        b=bias_random(p)
    if a == 0  and b == 1 :
        return 0
    return 1

if __name__ == "__main__":
##    a,b=3,8
##    z1=[x+a for x in range(b-a+1)]
##    z2=[0]*(b-a+1)
##    zdict=dict(zip(z1,z2))
##    for i in range(100001):
##        zdict[random_new(a,b)] +=1
##    print zdict
    count = 0
    p=random.random()
    print p
    for i in range(100001):
        count+=justify_random(p)
    print count
