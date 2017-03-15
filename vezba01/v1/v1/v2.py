import sys

def sumSqr(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    return sum
n = int(sys.argv[1], 10)
print(sumSqr(n))

