# -*- coding: cp936 -*-
#种群数： NP
#遗传代数：NG
#交叉概率：pc
#变异概率：pm
#离散精度：eps
#上下限：  (a,b)
from math import ceil,log,fsum,floor,sqrt,cos,sin
#import math
from random import random,randint
import functools

int2 = functools.partial(int,base=2)

def log2(a):
    return log(a)/log(2)

def initial(L,NP,fitness,a,b):
    Lt=[]
    for i in range(NP):
        z=[gen_bin(L) for x in range(NP)]
        fx=[fitness(x) for x in dec(a,b,z)]
        Lt.append(z[fx.index(max(fx))])
    return Lt
        
##    return [gen_bin(L) for x in range(NP)]

def gen_bin(L):
    x=randint(0,pow(2,L)-1)
    xb=bin(x)
    x1='0'*(L+2-len(xb))
    x2=xb[2:]
    return x1+x2

def dec(a,b,x):
    L=[]
    lx=len(x[0])
    for i in range(len(x)):
        L.append(a+float(int2(x[i]))/(pow(2,lx)-1)*float(b-a))
    return L

def roll_round(fx):
    fall=fsum(fx)
    fxp=[x/fall for x in fx]
    fxa=[]
    fxa.append(fxp[0])
    for i in range(1,len(fxp)):
        fxa.append(fxa[i-1]+fxp[i])
    sat=random()
    i=0
    while sat > fxa[i]:
        i +=1
    return i
        
def loser(fx):
    return fx.index(min(fx))
        

def mutation(x,i):
    xx=int2(x)^pow(2,i)
    xb=bin(xx)
    return '0'*(len(x)+2-len(xb)) +xb[2:]

def GA(fitness,a,b,NP,NG,pc,pm,eps) :
    L=int(ceil(log2((b-a)/eps)))
    x=initial(L,NP,fitness,a,b);
    xd=dec(a,b,x)
    print xd
    for i in range(NG):
        fx=[fitness(z) for z in xd]
        father=roll_round(fx)
        lmin=loser(fx)
        mother=int(floor(random()*NP))
        if random() < pc:
            cutp=int(floor(random()*L))
##            print lmin,father,cutp,mother
##            print x
            x[lmin]=x[father][:cutp]+x[mother][cutp:]
            if random() <pm :
                cum=int(floor(random()*L))
                x[lmin]=mutation(x[lmin],cum)
        xd=dec(a,b,x)
    fv=fitness(xd[0])
    xv=xd[0]
    print xd
    for i in range(2,len(x)):
        fitx =fitness(xd[i])
        if fv <fitx:
            fv =fitx
            xv =xd[i]
    return fv,xv
                

def fitness(x):
    #return abs(1/(float(x)*x -5))
    return cos(5*x)-sin(3*x)+10

if __name__ == '__main__' :
    #print initial(10,4)
    pm = 0.1
    pc = 0.9
    a,b=(1,7)
    eps=0.0001
    NP =20
    NG =200
    print GA(fitness,a,b,NP,NG,pc,pm,eps)

