#.............loops...............
"""name="ashok kumar"
for i in range(1,5):
    print(name)

for i in range(1,10,2):
    print(i)
"""

#.............dictionary............
"""a=[10,50,Ashok,ranjan,5.9]
for item in a:
    print(item)
st="programming"
n=len(st)
for i in range(n):
    print(st[i])"""
"""

#.............for else....
st="programming"
for i in st:
    print(i)
else:
    print("Else part")


#..............nested loop.........
for i in range(1,4):
    print("this is parent loop",i)
    for j in range(3):
        name=input("Enter your name:")
        print(f"this is child loop called by {name}",j)
print("loop end")
"""
"""
#............BREAK STATEMENT..........
for i in range(1,10)
    if i==5:
        break
    print(i)

#............CONTINUE STATEMENT..........
for i in range(10):
    if i==5:
        continue
    print(i)
#.................pass STATEMENT..........
for i in range(10):
    if i==5:
        pass
    print(i)
"""
#...........sum of elemnts of list..........
List1=[11,5,17,18,23]
sum=0
for i in range(0,len(List1)):
    sum=sum+List1[i]
print(f"Sum of elements of List1 is {sum}")
