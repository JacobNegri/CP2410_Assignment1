from SparseArray import SparseArray
import random
from time import clock
for q in range(3,13):
    print("")
    n = 10**q
    print("n: " + str(n))
    array = SparseArray(n)
    m_list = []
    for f in range(0,q):
        if f < 8:
            m_list.append(10 ** f)

    #testing each number of ms in the sparse array of n
    for m in m_list:
        print("m: " + str(m))
        for m in range(1, m):
            num = random.randint(0, n-1)
            array[num] = 3

        #testing setting a random location
        rndnum = random.randint(0, n - 1)
        start = clock()
        array[rndnum] = 3
        end = clock()
        print("Set: {0:.5f} ms".format((end - start)*1000))

        #testing getting a random location
        rndnum = random.randint(0, n - 1)
        start = clock()
        array[rndnum]
        end = clock()
        print("Get: {0:.5f} ms".format((end - start)*1000))
