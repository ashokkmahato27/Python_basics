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
