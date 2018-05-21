# Find maximum difference between nearest left and right smaller elements
# Time C = O(n)

def left_right_elements(arr,n,SA):
    stack = []
    top = len(stack)-1
    for i in range(n):

        while (len(stack)>0 and stack[top]>=arr[i]):
            stack.pop()
        if stack!=[]:
            SA[i] = stack[top]
        else:
            SA[i] = 0
        stack.append(arr[i])
    return SA

def findMaxDiff(arr,n):
    #ls and rs are two empty arrays to store the nearest left and right smaller element of every element in thei/p array
    ls =[0]*n
    rs = [0]*n
    ls = left_right_elements(arr,n,ls)
    rs = left_right_elements(arr[::-1],n,rs)
    print "ls",ls
    print "rs",rs
    res = -1
    for i in range(n):
        res = max(res,abs(ls[i]-rs[n-i-1]))
    return res


# Driver Program
if __name__=='__main__':
    arr = [2, 4, 8, 7, 7, 9, 3]
    print "Maximum Diff :", findMaxDiff(arr, len(arr))
