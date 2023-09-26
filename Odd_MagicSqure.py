num = int(input("Enter odd Number: "))
magicSquare = [[0 for x in range(num)] for y in range(num)]
# print(magicSquare)

# for i in range(len(magicSquare)):
i = num//2
j = 0
c = 1
while c<=(num*num):
    if i>=num:
        i=0
    elif j<0:
        j = num-1
    elif i<=0 and j>=num:
        j=1
        i=num-1
    if magicSquare[j][i]!=0:
        j+=2
        i-=1
    else:
        magicSquare[j][i]=c
        j-=1
        i+=1
        c+=1
# print(magicSquare)
print("____"*num)
print( )

for m in range(num):
    for n in range(num):
        print("",magicSquare[m][n], end="  ")
    print("\n"+"____"*num)
    print( )
