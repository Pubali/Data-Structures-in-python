# If A knows B, then A can’t be celebrity. Discard A, and B may be celebrity.
# If A doesn’t know B, then B can’t be celebrity. Discard B, and A may be celebrity.
# Repeat above two steps till we left with only one person.
# Ensure the remained person is celebrity.


# Complexity O(N). Total comparisons 3(N-1). 
def knows(a, b):
    return True if (matrix[a][b] == 1) else False
def getcelebrity(arr, n):

    if (n == 0 or len(arr) < n):
        print "Not enough elements"
        return
    st = []
    for i in range(n):
        st.append(i)
    while(len(st)>1):
        a = st.pop()
        b = st.pop()
        if(knows(a,b)):
            st.append(b)
        else:
            st.append(a)
    celeb_element = st.pop()
    for i in range(n):
        if (i!=celeb_element):
            if(knows(celeb_element,i) or not knows(i,celeb_element)):
                return -1
    return celeb_element


if __name__=='__main__':
    # t = int(input())
    # for i in range(t):
    # n = list(map(int, input().strip().split()))
    # arr = list(map(int, input().strip().split()))
    n= 4
    arr = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    matrix = [[0 for i in range(n)]for j in range(n)]

    c=0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = arr[c]

            c+=1
    print matrix
    print(getcelebrity(matrix, n))
