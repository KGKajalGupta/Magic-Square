'''
                    1	15	14	4
                    12	6	7	9
                    8	10	11	5
                    13	3	2	16

            
            1	63	62	4	5	59	58	8
            56	10	11	53	52	14	15	49
            48	18	19	45	44	22	23	41
            25	39	38	28	29	35	34	32
            33	31	30	36	37	27	26	40
            24	42	43	21	20	46	47	17
            16	50	51	13	12	54	55	9
            57	7	6	60	61	3	2	64
'''

# n = int(input("Enter the Number(Multiple of 4): "))

def even4(n):
    array1 = [[0 for i in range(n)] for j in range(n)]

    k = n*n
    j = 1
    for i in range(n):
        if (i%4==0) or ((i+1)%4==0):
            for m in range(n):
                if (m+1)%4==0 or m%4==0:
                    array1[i][m]=j
                else:
                    array1[i][m]=k
                j+=1
                k-=1
        else:
            for m in range(n):
                if (m+1)%4==0 or m%4==0:
                    array1[i][m]=k
                else:
                    array1[i][m]=j
                j+=1
                k-=1

    for row in array1:
        print(*row)
    
# print(array1)

# array = [(i+1) for i in range(4*4)]
# array1 = [[0 for i in range(8)] for j in range(8)]
# n = len(array1)

# k = 8*8
# j = 1

# flag = True
# for i in range(8):
#         if i==0 or i==3 or i==4 or i==(n-1):
#             for m in range(8):
#                 if m==0 or m==3 or m==4 or m==7:
#                     # print(j, end=" ")
#                     array1[i][m]=j
#                 else:
#                     array1[i][m]=k
#                     # print(k, end=" ")
#                 j+=1
#                 k-=1
#             # print()
#         else:
#             for m in range(8):
#                 if m==0 or m==3 or m==4 or m==(n-1):
#                     array1[i][m]=j
#                 else:
#                     array1[i][m]=k
#                 j+=1
#                 k-=1
# print(array1)
