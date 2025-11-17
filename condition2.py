#_1 ...........ticket price fo theatre................
#wap to make a ticket system
age=int(i
        nput("Enter your age:"))
if age<12:
    print("Ticket Free")
elif age>=12 and age<=60:
    user=input("Enter your membership,yes or no:")
    if user=="yes":
        print("Ticket Price is 150")
    else:
        print("Ticket Price is 200")
else:
    print("Ticket Price is 100")

#_2..............Utility company charges ................

usage= int(input("Enter the  units:"))
if usage<=100:
    amount=usage*5
elif usage>=100 and usage<=300:
    useafter100 =usage-100
    amount=  100*5+ useafter100*8 
else:
    useafter300=usage-300
    amount= useafter300*10 +100*5 +200*8
print(f"the rate for {usage} unit is {amount}")

#_3...........Restaurant Bill with Discount ........

bill=int(input("Enter the bill amount:"))
user=input("Enter your membership,yes or no:")
discount=0
if user=="yes":
    if bill>1000 and bill<2000:
        discount=bill*0.15
    elif bill>2000:
        discount=bill*0.20
else:
    if bill>1000 and bill<2000:
        discount=bill*0.10
    elif bill>2000:
        discount=bill*0.15
total_bill=bill-discount
print(f"Your total bill is {total_bill} and discount is {discount}")

#_4............Online Shopping Discount System.............
price=int(input("Enter the price:"))
member=input("Enter you are prime member,yes or no:")
discount=0
if (price>5000):
    if (member=="yes"):
        discount=price*0.20
    else:
        discount=price*0.10
elif (price>2000 and price<5000):
    if (member=="yes"):
        discount=price*0.10
    else:
        discount=price*0.05
total_price=price-discount
print(f"The total bill is: {total_price} and Discount is {discount}")


#_5................Grading System with Bonus..............

marks = int(input("Enter the student's marks: "))
if (marks >= 90):
    print("Grade A")
elif (marks >= 75 and marks <= 89):
    print("Grade B")
elif (marks >= 60 and marks <= 74):
    print("Grade C")
else:
    print("Fail")

#_6..............Hotel Room Booking System..............
room_type = input("Enter room type (deluxe/standard): ")
nights = int(input("Enter number of nights: "))
deluxe_price = 5000
standard_price = 3000
if room_type == "deluxe":
    cost = nights * deluxe_price

    if nights > 5:
        cost = cost - (cost * 0.20)
elif room_type== "standard":
    cost = nights * standard_price
    if nights > 5:
        cost = cost - (cost * 0.10)
else:
    print("Invalid room type!")
    cost = 0

print(f"Total Cost of room is Rs.{cost}")

#_7...............Vehicle Insurance Premium Calculator...............

car_type = input("Enter vehicle type (Sedan/SUV): ")
age = int(input("Enter driver's age: "))
ncb = input("Do you have No Claim Bonus (yes/no): ")
if car_type== "sedan":
    premium = 5000
elif car_type == "suv":
    premium = 8000
else:
    print("Invalid vehicle type!")
    premium = 0
if premium != 0:
    if age < 25:
        premium = premium + (premium * 0.10)
    elif age > 60:
        premium = premium + (premium * 0.15)
    else:
        premium = premium
    if ncb== "yes":
        premium = premium - (premium * 0.20)

    print("Final Insurance Premium: Rs.", premium)
