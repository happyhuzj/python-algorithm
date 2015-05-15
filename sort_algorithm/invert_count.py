count=0
def invert_count(a,p,r):
    global count
    if r-p <2:
        if a[p] > a[r] :
            a[p],a[r]=a[r],a[p]
            count+=1
    else :
        q=(p+r)/2
        invert_count(a,p,q)
        invert_count(a,q+1,r)
        merge(a,p,q,r)
    return a

def merge(a,p,q,r):
    global count
    L=[x for x in a[p:q+1]]
    R=[x for x in a[q+1:r+1]]
    i,j,k=0,0,p
    flag=0
    while i<len(L) and j <len(R) :
        if L[i] <R[j] :
            a[k] = L[i]
            flag =0
            i+=1
        else :
            if flag == 0:
                count +=j+1
            else:
                count +=1
            flag =1
            a[k]=R[j]
            j+=1
        k+=1
    if i==len(L) :
        a[r+1-len(R)+j:r+1]=R[j:len(R)]
    if j==len(R):
        count += (len(L)-i+1)*len(R)
        a[r+1-len(L)+i:r+1] = L[i:len(L)]
    


if __name__ == "__main__" :
       a=[1,3,5,7,9,11,2,4,6,8,10,12,0,-2,-1]
       #merge(a,1,5,11)
       invert_count(a,0,len(a)-1)
       print count
