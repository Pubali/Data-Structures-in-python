# delete consecutive same words in a sequence
def Remove_consecutive_same(arr,n):
    stack = []
    stack.append(arr[0])

    for i in range(1,n):
        if(len(stack)>0 and stack[len(stack)-1]==arr[i]):

            stack.pop()

        else:
            stack.append(arr[i])

    return len(stack)
arr = ['ab','aa','aa','bcd','ab']
print Remove_consecutive_same(arr,len(arr))
