# Uses python3
import sys
import math

def binary_search(a, x):
    left, right = 0, len(a)-1
    while(left <= right):
        mid = math.floor((right + left) / 2)
        if (a[mid] == x):
            return mid
        elif (a[mid] > x):
            right = mid - 1
        elif (a[mid] < x):
            left = mid + 1
    return -1

def majority_element(arr, length):
    arr.sort()
    crit = length / 2
    cand = arr[0]
    occur = 0
    while(len(arr) != 0):
        ind = binary_search(arr, cand)
        if(ind != -1):
            occur += 1
            arr.pop(ind)
        else:
            cand = arr[0]
            occur = 0
        if occur > crit:
            return 1
    return 0

input = sys.stdin.read()
n, *a = list(map(int, input.split()))
print(majority_element(a, n))
