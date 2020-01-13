import numpy as np
from time import time
import multiprocessing as mp


# def howmany_within_range(row, minimum, maximum):
#     """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
#     count = 0
#     for n in row:
#         if minimum <= n <= maximum:
#             count = count + 1
#     return count
#
# # results = []
# # for row in data:
# #     results.append(howmany_within_range(row, minimum=4, maximum=8))
# #
# # print(results[:10])
# import multiprocessing as mp
#
# if __name__=="__main__":
#     starttime = time()
#     print("starttime = {0}".format(starttime))
#
#     # Prepare data
#     np.random.RandomState(100)
#     arr = np.random.randint(0, 10, size=[200000, 5])
#     data = arr.tolist()
#     data[:5]
#     # Step 1: Init multiprocessing.Pool()
#
#     pool = mp.Pool(mp.cpu_count())
#
#     # Step 2: `pool.apply` the `howmany_within_range()`
#     results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]
#
#     # Step 3: Don't forget to close
#     pool.close()
#
#
#     print(results[:10])
#     print("total time = {0}".format(time() - starttime))

def plswork(templist1):
    print(print("IP = {0} ,Username = {1} ,Password = {2}".format(templist1[0], templist1[1], templist1[2])))


if __name__ == "__main__":
    pool = mp.Pool(5)
    f = open("server_info.txt", "r")
    content = f.readlines()
    print(type(content))
    res = []
    print(content)
    for i in range(len(content)):
        templist = []
        templist = content[i].split(",")
        pool.map(plswork, [templist])
    pool.close()
    print("total result".format(res))

    # for x in range(12):
    #     print(x)
    #     res.append(pool.map(plswork,[x]))
    # pool.close()
    # print(res)
