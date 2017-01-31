import timeit
import numpy as np
import matplotlib.pyplot as plt


def bruteforce(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            if sum(arr[i:j]) > res:
                res = sum(arr[i:j])
    return res

def recursive(arr):
    n = len(arr)
    if n <= 1:
        return sum(arr)
    mid = n // 2
    L = recursive(arr[:mid])
    R = recursive(arr[mid:])
    M = max(sum(arr[i:mid]) for i in range(mid-1, -1, -1)) \
        + max(sum(arr[mid:i]) for i in range(mid+1, n+1))
    return max(L, R, M)

def kadane(arr):
    lowest = res = total = start = end = 0
    for i, n in enumerate(arr):
        total += n
        if lowest > total:
            start = i
            lowest = total
        if total - lowest > res:
            end = i
            res = total - lowest
    return (res, arr[start+1:end+1])


times_recursive = []
times_kadane = []
times_bruteforce = []
for i in range(1, 101):
    arr = np.random.randint(-100, 100, size=i)
    print(i)
    
    time = timeit.timeit('bruteforce(arr)',
                         globals=globals(),
                         number=10)    
    times_bruteforce.append(time)
    
    time = timeit.timeit('recursive(arr)',
                         globals=globals(),
                         number=10)                         
    times_recursive.append(time)
    
    time = timeit.timeit('kadane(arr)',
                         globals=globals(),
                         number=10)
    times_kadane.append(time)

plt.plot(range(1, 101), times_bruteforce,
         range(1, 101), times_recursive,
         range(1, 101), times_kadane)
plt.show()

plt.plot(range(1, 21), times_bruteforce[:20],
         range(1, 21), times_recursive[:20],
         range(1, 21), times_kadane[:20])
plt.show()