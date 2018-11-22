# Uses python3
import sys

def dp_sequence(number):
    num_operations = [0] * (number + 1)
    num_operations[1] = 1
    sequence = []
    for i in range(2, number + 1):
        num_operations[i] = num_operations[i - 1] + 1
        if i % 2 == 0:
            num_operations[i] = min(num_operations[int(i/2)] + 1, num_operations[i])
        elif i % 3 == 0:
            num_operations[i] = min(num_operations[int(i / 3)] + 1, num_operations[i])
    i = number
    while i > 1:
        sequence.append(i)
        if num_operations[i - 1] == num_operations[i] - 1:
            i -= 1
        elif (i % 2 == 0 and num_operations[int(i / 2)] == num_operations[i] - 1):
            i = int(i / 2)
        elif (i % 3 == 0 and num_operations[int(i / 3)] == num_operations[i] - 1):
            i = int(i / 3)
    sequence.append(1)
    sequence.reverse()
    return sequence

input = sys.stdin.read()
n = int(input)
seq = dp_sequence(n)
print(len(seq) - 1)
for x in seq:
    print(x, end = ' ')
