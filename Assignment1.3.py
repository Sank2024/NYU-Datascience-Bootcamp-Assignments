# Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.


num =1 


while num <=20: # Iterating through 1-20. 
   #conditioning if the modulus gives reminder to check even and odd.
    if num % 2 ==0:
        print (str(num) + " is even")
    else:
        print (str(num) + " is odd")

    num+=1 #Incrementing the number after checking oen at each time. 