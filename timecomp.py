# measuring time efficiency method 1:-

# import time
# start = time.time()
# for i in range(1,100):
#     print(i)


# print(time.time() - start)
# 0.08823871612548828 this is time complexity using for loop

import time
start = time.time()
i = 1
while i<101:
    print(i)
    i+=1

# 0.048328399658203125 this is time comlexity using while loop.
# difference of time in two logic
# print(time.time() - start)


import time
start = time.time()
i = 1
while i<2:
    print(i)
    i+=1
#  0.001147508621215820 this is time complexity for small input
# but we cant use this bcz in this much small input we cant check the complexity
print(time.time() - start)