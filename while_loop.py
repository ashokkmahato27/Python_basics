#_1..............while loop program.........

while True:
    user_input = input("Enter your age (or type 'stop' to exit): ")
    
    if user_input.lower() == "stop":
        print("Program terminated.")
        break
    
    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue
    
    age = int(user_input)
    
    if age < 18:
        print("You are a minor.")
    elif 18 <= age <= 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

#_2...........Write a Python program that simulates waiting for a specific vehicle,

while True:
    V_name=input("Enter vehicle name:")
    if V_name=="bus":
        print("Your waiting is over")
        break
    else:
        print("waiting")

#_3.......... WAP that continuously prompts the user to input a fruit name ............

while True:
    fruit=input("Enter fruit name:")
    if fruit=="apple":
        print("You got it!")
        break
    else:
        print("Try again") 

#_4............program that asks the user to guess the password..........
while True:
    password=input("Enter password:")
    if password=="open sensane":
        print("You got it!")
        break
    else:
        print("Wrong password. Try again")

#_5...........Write a Python program that keeps asking the user to enter a day of the week
while True:
    day=input("Enter day:")
    if day=="sunday":
        print("Enjoy your weekend  !")
        break
    else:
        print("it's not wekend yet")

#_6...........program that generates a random number between 1 and 10 and prompts the user to guess the number.

import random
number=random.randint(1,10) 
attempts=0
while True:
    guess=int(input("enter the the number between 1 to 10:"))
    attempts+=1
    if guess>number:
        print("Try smaller number")
    elif guess<number:
        print("Try bigger number")
    else:
        print(f"You got the number in {attempts} attempt sand number is {number}")
        break

#_7.........Write a Python program that simulates a login system..............

True_username="admin"
True_password="1234"
attempts=0
while attempts<3:
    username=input("Enter username:")
    password=input("Enter password:")  
    if username==True_username and password==True_password:
        print("Login successful")
        break
    else:
        print("Login failed, try again")
        attempts+=1
    if attempts==3:
        print("You have exceeded the maximum number of attempts. Please try again later.")  

#_8.......... Write a Python program that simulates a basic arithmetic quiz.........
import random
print("Welcome to the Arithmetic Quiz! or Exit:")
while True:
    num1=random.randint(1,30)
    num2=random.randint(1,30)
    answer=input(f"Multiplication of {num1} * {num2}=")
    if answer=="exit":
        print("Program terminated")
        break
    if int(answer)==(num1*num2):
        print("Correct")
    else:
        print("Incorrect, Try again")

#_9..........The program should determine whether the number is prime or not.......
while True:
    number=(input("Enter the number or type exit:"))
    if number=="exit":
        print("Program terminated")
        break
    number=int(number)
    if number<2:
        print("Number is not prime")
        continue
    else:
        for i in range(2,number):
            if number%i==0:
                prime=False
        if prime:
            print("Number is prime")
        else:
            print("Number is not prime")
               
#_10........ asks the user to guess a pre-defined secret.........
secret_word = "python"

while True:
    guess = input("Guess the secret word (or type 'quit' to exit): ")

    if guess.lower() == "quit":
        print("Program terminated.")
        break

    if guess.lower() == secret_word:
        print("Congratulations, you guessed the word!")
        break
    else:
        print("Incorrect, try again.\n")
