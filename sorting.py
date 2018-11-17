# Uses python3
import sys
import random

def partition3(A, l, r):
    lt = l
    i = l
    gt = r
    pivot = A[l]
    while i <= gt:
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def quick_sort(A, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]

    lt, gt = partition3(A, l, r)
    quick_sort(A, l, lt - 1)
    quick_sort(A, gt + 1, r)



input = sys.stdin.read()
n, *A = list(map(int, input.split()))
quick_sort(A, 0, n - 1)
for x in A:
    print(x, end=' ')
