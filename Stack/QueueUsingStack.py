class Stack:

    def __init__(self):
        self.stack_list = []

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        return self.stack_list.pop()

    def size(self):
        return len(self.stack_list)

    def is_empty(self):
        return self.size() == 0


class Implement_Queue_using_Stack:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if not self.stack1.is_empty():
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
            res = self.stack2.pop()
            while self.stack2.size() > 0:
                self.stack1.push(self.stack2.pop())
            return res

if __name__ == '__main__':
    q = Implement_Queue_using_Stack()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    a = q.dequeue()
    print(a)
    b = q.dequeue()
    print(b)
    c = q.dequeue()
    print(c)
    d = q.dequeue()
    print(d)
    q.enqueue(50)
    q.enqueue(60)
    print(q.dequeue())
