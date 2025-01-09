#If Statement
#Exercise 1: Check if the number is even.
num = 6
if num % 2 == 0:
    print ('Ex1:The number is even.')
#Exercise 2: Display a message if a list is empty.
my_list = [ ]
if len(my_list) == 0:
    print ('Ex2:list is empty')

#else Statement

#Exercise 1: Write a script to check if a number as odd or even
#n1 = int(input("write a number") )
n1 = 11
if n1%2==1:
    print ('Ex3:n1 is odd')
else:
    print ('Ex3:n1 is even')
#NUM = input("write a number") 
#print(f"Reversed string: {NUM}")

#elif Statement
#temp = int(input("write a temperature: ") )
temp = 15.07
if temp <= 0:
    print('Its Freezing Colddd!')
elif temp <= 10:
    print('Its Cold')
elif temp <= 20:
    print('Its Moderate')
elif temp <= 25:
    print('Its warm')
else:
    print('Its Hotttt!')

#for Loop

#Exercise 1: Print each character in a string.
string = 'Hello,World'
for char in string:
    print(char)
#Exercise 2: Create a list of squares of the first 10 natural numbers
squares = [i ** 2 for i in range(1, 11)]
print(squares)


#while Loop
#Exercise 1: Add numbers until sum reaches 100.
total_sum = 0
current_number = 1
while total_sum < 100:
    total_sum += current_number
    current_number += 1
print('The sum of numbers until reaching 100 is:', total_sum)

#Infinite Loops and break
#Exercise : Guessing game with break on correct guess.
#num= 0
import random
CorrectNum = random.randint(1,10)
while True:
  
  Num= int(input("Guessing a number: ") )
  if Num == CorrectNum:
    break
  if num>= CorrectNum:
      print(Num,'is a wrong number, try again ')
      print('The correct number is smaller than',Num)
  else :
      print(Num,'is a wrong number, try again ')
      print('The correct number is higher than',Num)    
  
print(CorrectNum,'is a correct number !')