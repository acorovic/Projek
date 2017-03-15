import random
import time
def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

list = random_list(1, 100, 50)
print (list)

#TO DO:
#----------------------------------------------------------------
start_time = time.clock()

def foo():
    print ("blah")

foo()

end_time = time.clock() - start_time
print ("Duration: ", end_time)

#----------------------------------------------------------------
