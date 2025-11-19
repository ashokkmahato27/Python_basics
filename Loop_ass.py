
#_1........ print "software" 10 times...........
a="software"
for i in range(10):
    print(a)  

#_2...........Sum of a list ...........

a=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in a:
    sum=sum+i
print(sum)

#_3............print each character using indexing.........
a="software"
for i in range(len(a)):
    print(a[i])

#_4.....write a program to display integer from of a list. given list=[1,"a","c",2,3,4].....
a=[1,"a","c",2,3,4]
for i in a:
    if type(i)==int:
        print(i)

#_5.........multiplication of a each element. given list=[4,5,3,2].........
list=[4,5,3,2]
mul=1
for i in list:
    mul=mul*i
print(mul)

#_6..........multiplication table of a given number..............
num = int(input("Enter a number: "))
print(f"Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

#_7.........reverse a list...............
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

#_8...............Python program to check the validity of username and password input by users....

username= input("Enter your username:")
password= input("Enter your password:")
if username=="ashok":
    if password=="murkha123":
        print("bahut bahut swagat hai")
    elif password=="1234":
        print("Bahut Kamjor Password Hai, Thora dhyan do")
    else:
        print("Galat hai be")
else:
    if username=="ranjan":
        if password=="1234":
            print("Bahut Kamjor Password Hai, Thora dhyan do")
        else:
            print("Galat hai be")
    else:
        print("Galat hai be")

#_9............Write a for loop which print "Hello!, " plus each name in the list......
a = ["ram", "shyam", 1, 2]

for item in a:
    if type(item) == str:      
        print("Hello!", item)

#_10............Write a for loop which print "Hello!, " plus each name in the list.....
lst=["ashok","ranjan","shyam","ram",1,2]
for i in lst:
    print("Dr.",i)

#_11.............removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"]...

bad_chars = [';', ':', '!', '*']

text = input("Enter a string: ")

cleaned_text = ""

for char in text:
    if char not in bad_chars:
        cleaned_text += char

print("Cleaned string:", cleaned_text)

#_12.............Write a for loop to find the sum of even and odd numbers separately in a range from 1 to 100.
sumofeven=0
sumofodd=0
for i in range(1,100):
    if i%2==0:
        sumofeven=sumofeven+i
    else:
        sumofodd=sumofodd+i
print(f"Sum of even number is {sumofeven} and sum of odd number is {sumofodd}")

#_13...............program to check given number is palindrome or not....

num = int(input("Enter a number: "))
original = num  
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print(original, "is a palindrome number.")
else:
    print(original, "is NOT a palindrome number.")

#_14.........program to check given number is armstrong or not......

num = int(input("Enter a number: "))
n = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
    
