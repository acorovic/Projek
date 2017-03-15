import sys

s1 = sys.argv[1]
s2 = sys.argv[2]

lenS1 = len(s1)
if lenS1 > 3:
    lenS1 = 3
lenS2 = len(s2)
if lenS2 > 3:
    lenS2 = 3

s3 = ""

for i in range(1,3):
    for k in range(0,lenS1):
        s3 += s1[k]

for i in range(1,3):
    for k in range(len(s2) - lenS2, len(s2)):
        s3 += s2[k]

print(s3)