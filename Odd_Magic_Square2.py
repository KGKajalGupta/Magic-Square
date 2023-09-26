
# Grid = int(input("Enter the odd number of Row: "))

def odd_magic(Grid):

    list1 = [[0 for i in range(Grid)] for j in range(Grid)]

    i = Grid//2
    j = Grid-1

    num = 1
    while num<=(Grid**2):

        if j>=Grid and i<0:
            j = Grid-2
            i = 0
        elif i<0:
            i = Grid-1
        elif j>=Grid:
            j=0

        if list1[i][j]!=0:
            j = j-2
            i+=1
        else:
            list1[i][j] = num
            num += 1
            i-=1
            j+=1

    # print(list1)

    for i in range(Grid):
        for j in range(Grid):
            print(list1[i][j], end=" ")
        print()
        print("__"*Grid)
        print()