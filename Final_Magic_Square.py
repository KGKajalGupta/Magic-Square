import Even_Magic_square
import Even_Magic_Squre_divisibleBy4
import Odd_Magic_Square2

number = int(input("Enter the row : "))

if number%4==0:
    Even_Magic_Squre_divisibleBy4.even4(number)

elif number%2==0:
    Even_Magic_square.even2(number)
    
else:
    Odd_Magic_Square2.odd_magic(number)