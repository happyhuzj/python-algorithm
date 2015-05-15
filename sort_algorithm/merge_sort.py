def merge_sort(a,p,r):
    if r-p <2:
        if a[p] > a[r] :
            a[p],a[r]=a[r],a[p]
    else :
        q=(p+r)/2
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)
    return a

def merge(a,p,q,r):
    L=[x for x in a[p:q+1]]
    R=[x for x in a[q+1:r+1]]
    i,j,k=0,0,p
    while i<len(L) and j <len(R) :
        if L[i] <R[j] :
            a[k] = L[i]
            i+=1
        else :
            a[k]=R[j]
            j+=1
        k+=1
    if i==len(L) :
        a[r+1-len(R)+j:r+1]=R[j:len(R)]
    if j==len(R):
        a[r+1-len(L)+i:r+1] = L[i:len(L)]
    


if __name__ == "__main__" :
       a=[1,3,5,7,9,11,2,4,6,8,10,12,0,-2,-1]
       #merge(a,1,5,11)
       merge_sort(a,0,len(a)-1)
       print a
