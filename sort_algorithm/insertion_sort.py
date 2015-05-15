##def insertion_sort(a):
##    L=a[:]
##    for j in range(1,len(L)):
##        key = L[j]
##        i=j-1
##        while i >=0 and L[i] > key :  
##            L[i+1]=L[i]
##            i -= 1
##        L[i+1]=key
##        print L         
##    return L

def insertion_sort(a,n) :
    if n == 0:
        return a
    else :
        insertion_sort(a,n-1)
##        insert(a,n-1)
        insert(a,0,n-1)
    return a

##def insert(a,n):
##    key=a[n]
##    i=n-1
##    while i>=0 and a[i] > key:
##        a[i+1]=a[i]
##        i-=1
##    a[i+1]=key

def insert(a,p,r):
    if r-p <2:
        if a[p] > a[r]:
            a[p],a[r]=a[r],a[p]
    else:
        q=(r+p-1)/2
        key=a[r]
        if a[q] < key :
            insert(a,q+1,r)
        else :
            a[q+2:r+1]=a[q+1:r]
            a[q+1]=key
            insert(a,p,q+1)

if __name__ == "__main__" :
    a=[5,2,6,3,4,1]
    print insertion_sort(a,len(a))
