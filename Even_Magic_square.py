'''         35	1	6	    26	19	24
            30	5	7	    21	23	25
            31	9	2	    22	27	20

            8	28	33	    17	10	15
            3	32	34	    12	14	16
            4	36	29	    13	18	11
'''

# num = int(input("Enter the Number: "))

def even2(num):
    n1 = num//2    #for saprate then in odd value  like 6//2 = 3 3 3 3
    n2 = n1*n1
    array = [[[0 for i in range(num//2)] for j in range(num//2)] for i in range(4)]
    count = 1
    m = 0
    while m<4:
        i = 0
        j = n1//2
        n = n1
        while count<=(n2*(m+1)):
            if j>=n and i<0:
                j = n-1
                i +=2
            elif i<0:
                i = n-1
            elif j>=n:
                j = 0
            if array[m][i][j]!=0:
                i+=2
                j-=1
                array[m][i][j]=count
                count+=1
            else:
                array[m][i][j]=count
                count+=1
            i-=1
            j+=1
        m += 1

    # This is for swapping
    array[1], array[2] = array[2], array[1]
    array[2], array[3] = array[3], array[2]

    # This is original Array
    # for i in range(n1):
    #     print(*array[0][i],*array[1][i])
    # for i in range(n1):
    #     print(*array[2][i],*array[3][i])

    # print()

    count1 = 0
    while count1<(n1-2):
        if count1>(n1-2)//2:
            for i in range(n1):
                array[1][i][count1],array[3][i][count1] = array[3][i][count1], array[1][i][count1]
        else:
            for i in range(n1):
                array[0][i][count1],array[2][i][count1] = array[2][i][count1], array[0][i][count1]
        count1+=1   
    # print(array)

    for i in range(n1):
        print(*array[0][i],*array[1][i])

    for i in range(n1):
        print(*array[2][i],*array[3][i])





