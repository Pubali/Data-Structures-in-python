class K_Stack_one_array():
    def __init__(self,n,k):
        self.stack = []
        # arr is the array of size n where k stacks will be implemented
        self.arr = [0]*n
        # top is the array to store k stacks's top indexes
        self.top = [0]*k
       # Array of size n to store next entry in all stacks and free list
        self.next = [0]*n

        for i in range(k):
            self.top[i] = -1
        self.free = 0

        for j in range(n-1):
            self.next[j] = j + 1
        self.next[n - 1] = -1

    def isFull(self):
        return (self.free == -1)

    def isEmpty(self,sn):
        return (self.top[sn] == -1);

    def push(self,item,stack_no):
        if(self.isFull()):
            print "stack is full"
            return
         # Store index of first free slot
        self.i=self.free

        self.free = self.next[self.i]

        self.next[self.i] = self.top[stack_no]

        self.top[stack_no] = self.i

        self.arr[self.i] = item

    def pop(self,stack_no):
        if (self.isEmpty(stack_no)):
            print "Stack is empty"
            return

        self.i = self.top[stack_no]
        self.top[stack_no] = self.next[self.i]
        self.next[self.i] = self.free
        self.free =  self.i
        return self.arr[self.i]
    def print_stacks(self):
        print self.arr

k = 3
n = 10
K = K_Stack_one_array(n,k)
K.push(4,0)
K.push(3,1)
K.push(2,0)
K.push(5,2)
K.print_stacks()
K.pop(1)
K.print_stacks()
