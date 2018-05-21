# If an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
# then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
# Time Complexity is O(n)
def stockspan(arr,S,n):
    # Create a stack and push index of fist element to it
    st = []
    st.append(0)
    # Create a stack and push index of fist element to it
    S[0] =1
    for i in range(1,n):
        # Pop elements from stack whlie stack is not
        # empty and top of stack is smaller than price[i]
        while(len(st)>0 and price[st[len(st)-1]]<=price[i]):

            st.pop()
         # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i]  is
        # greater than elements after top of stack
        S[i] = i+1 if len(st)<=0 else (i-st[len(st)-1])

        # Push this element to stack
        st.append(i)
        print st
def printArray(arr, n):
    print arr

price = [100, 80, 60, 70, 60, 75, 85]
n = len(price)
S = [0 for i in range(len(price))]
stockspan(price,S,n)
printArray(S,n)
