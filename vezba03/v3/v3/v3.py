import math

def parentH(i):
    return math.floor(i/2)

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def maxHeapify(A,i):
    l = left(i)
    r = right(i)
    if l <= A.heapsize and A.heap[l] > A.heap[i]:
        largest = l
    else:
        largest = i
    if r <= A.heapsize and A.heap[r] > A.heap[largest]:
        largest = r
    if largest != i:
        temp = A.heap[i]
        A.heap[i] = A.heap[largest]
        A.heap[largest] = temp
        maxHeapify(A, largest)

def buildMaxHeap(A):
    A.heapsize = len(A.heap) -1 
    for i in range(math.floor(len(A.heap)/2), 0, -1):
        maxHeapify(A, i)

def heapSort(A):
    buildMaxHeap(A)
    for i in range(len(A.heap)-1, 1, -1):
        temp = A.heap[1]
        A.heap[1] = A.heap[i]
        A.heap[i] = temp
        A.heapsize -= 1
        maxHeapify(A,1)

def heapMax(A):
    return A[1]

def heapExtractMax(A):
    if A.heapsize < 1:
        print("heap underflow")
        return
    max = A.heap[1]
    A.heap[1] = A.heap[A.heapsize]
    A.heapsize -= 1
    maxHeapify(A,1)
    return max

def maxHeapInsert(A, key):
    A.heapsize += 1
    A.heap.append(-math.inf)
    heapIncreaseKey(A, A.heapsize, key)

def heapIncreaseKey(A, i, key):
    if key < A.heap[i]:
        print("new key is smaller than current key")
        return
    A.heap[i] = key
    while i > 1 and A.heap[parentH(i)] < A.heap[i]:
        temp = A.heap[parentH(i)]
        A.heap[parentH(i)] = A.heap[i]
        A.heap[i] = temp
        i = parentH(i)

class HeapClass:
    heapsize = 0
    heap = ['x',10,12,8,5,9]

    def __init__(self):
        heapsize = 0

A = HeapClass()
buildMaxHeap(A)
print(A.heap, A.heapsize)
maxHeapInsert(A, 4)
print(A.heap)
