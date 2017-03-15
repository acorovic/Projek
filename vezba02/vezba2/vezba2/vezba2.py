#insertionSort
import math

def insertionSort(n):
    for j in range(1,len(n)):
        key = n[j]
        i = j - 1
        while i >= 0 and n[i] > key:
            n[i+1] = n[i]
            i -= 1
        n[i+1] = key

def mergeSort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        print("merdzuje")
        print(p, q, r)
        merge(A, p, q, r)
        print(A)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(1,n1+1):
        L.append(A[p + i -1])
    for j in range(1, n2+1):
        R.append(A[q + j])
    L.append(math.inf)
    R.append(math.inf)
   
    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1

def binarySearch(n, start, end, val):
    mid = math.floor((start+end)/2)
    if(n[mid] == val):
        return True
    else:
        if(start == end):
            return False
        if(n[mid] > val):
            return binarySearch(n,start,mid,val)
        elif (n[mid] < val):
            return binarySearch(n,mid+1,end,val)


        