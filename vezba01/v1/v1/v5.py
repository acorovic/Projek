import sys

fin = open("dict_test.txt", "r")
line = fin.readline()

word = ""
dict = {}

while line:
    for i in line:
        if ((i == ',') or (i == ' ') or (i == '.')) :
            if word == "":
                continue
            if word in dict:
                val = dict[word]
                val += 1
                dict[word] = val
            else:
                dict[word] = 1
            word = ""
        else:
            word += i    
    line = fin.readline()

for k,v in dict.items():
    print(k,v)


