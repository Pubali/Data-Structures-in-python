# Reversing the first K elements of a Queue
# Input : Q = [10, 20, 30, 40, 50, 60,
#             70, 80, 90, 100]
        # k = 5
# Output : Q = [50, 40, 30, 20, 10, 60,
#              70, 80, 90, 100]

from collections import deque

def reverse_numbers(queue,k):
    stack = []
    for i in range(k):
        stack.append(queue.popleft())
    while(stack!=[]):
        queue.append(stack.pop())
    for i in range(len(queue)-k):
        queue.append(queue.popleft())
    return queue
queue = deque([10,20,30,40,50])
queue.append(60)
k= 3
print "The original queue is :",queue
queue = reverse_numbers(queue,k)
print "The reversed queue is :",queue
