def createstack():
    stack = []
    return stack
def push(stack,data):
    stack.append(data)
def isEmpty(stack):
    return len(stack) == 0
def pop(stack):
    if isEmpty(stack):
        print "error"
    else:
        return stack.pop()
def printNGE(arr):

    S = createstack()
    push(S,arr[0])
    for i in range(1,len(arr),1):
        if isEmpty(S)== False:

            current = arr[i]
            element = pop(S)
            while(element<current):
                print element +'...'+ current
                if isEmpty(S):
                    break
                element = pop(S)
            if (element > current):
              push(S,element)
        push(S,arr[i])

    while(isEmpty(S)== False):
         element = pop(S)
         print element +'...'+ -1

arr = [11, 13, 21, 3]
printNGE(arr)

