# python cant handle > 1 billion
#python cant handle 10^9 elements
# if f > 8 = a billion

from time import clock
import random

#testing list at varying values of n
for q in range(3,9):
    print("")
    n = 10**q
    print("n: " + str(n))
    array = [None]*n
    m_list = []
    for f in range(0,q):
        if f < 8:
            m_list.append(10 ** f)

    #testing each number of ms for list of n
    for m in m_list:
        print("m: " + str(m))
        for o in range(1, m):
            randomNum = random.randint(0, n - 1)
            array[randomNum] = 3
        num = random.randint(0, n - 1)
        start = clock()
        array[num] = 3
        end = clock()
        print("Set: {0:.5f} ms".format((end - start)*1000))
        num = random.randint(0, n - 1)
        start = clock()
        array[num]
        end = clock()
        print("Get: {0:.5f} ms".format((end - start)*1000))






