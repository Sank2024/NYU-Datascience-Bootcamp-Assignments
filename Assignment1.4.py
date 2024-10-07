# Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.

a = int (input("Enter an integer: ")) # Asking user for int input 
b = int (input("Enter another integer: ")) # Asking user for another integer 

def sum_of_integers(a:int ,b:int ):
    sum = (a + b)
    return sum


sum_total = sum_of_integers(a, b)
print (sum_total)




