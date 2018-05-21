# def next_line():
#   return input().strip()
#
# T = int(next_line())
#
# for _ in range(T):
#     N = int(next_line())
#     A = [int(x) for x in next_line().split(" ")]

# Given a set of time intervals in any order,
#  merge all overlapping intervals into one and output the result
#  which should have only mutually exclusive intervals.

N = 4
A =[1,3, 2, 4, 6, 8, 9, 10]
pairs = []

# for i in range(N):
#     start = i*2
#     pairs.append((A[start], A[start+1]))
# pairs = sorted(pairs, key=lambda p: p[0])

# another way of creating intervals
for _ in range(N):
        (i, j), A = A[0:2], A[2:]
        pairs.append((i,j))
stack = [pairs[0]]
print pairs
for i in range(1, N):
    topIndex = len(stack)-1
    top = stack[topIndex]
    
    pair = pairs[i]

    if top[1] >= pair[0]:
          stack[topIndex] = (top[0], max(top[1], pair[1]))
    else:
          stack.append(pair)
print stack
# print(" ".join(["{} {}".format(x,y) for x,y in stack]))
