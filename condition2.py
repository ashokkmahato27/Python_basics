# ...........ticket price fo theatre................
#wap to make a ticket system

age=int(input("Enter your age:"))
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

#..............Utility company charges ................

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

# ...........Restaurant Bill with Discount ........

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

#............Online Shopping Discount System.............
