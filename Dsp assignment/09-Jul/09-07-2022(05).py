#Given number is positive or negative
"""x=int(input("Enter a number:"))
if x<0:
    print("The entered number is negative",x)
else:
    print("The entered number is positive",x)
#Number Even or Odd
x=int(input("Enter a number:"))
if x%2==0:
    print("The Entered number is even",x)
else:
    print("The entered number is odd",x)
#Given year is leap year or not
year=int(input("Entered a year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("The given year is leapyear")
        else:
            print("The given year is not a leapyear")
    else:
        print("The given year is  a leapyear")
else:
    print("The given year is not a leapyear")

#Printing greatest number
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>b & a>c:
    print("a is big")
elif b>a & b>c:
    print("b is big")
else:
    print("c is big")
#program to print 1-10 and 10-1
print("The numbers from 1-10 are:")
for i in range(1,11,1):
    print(i)
print("The numbers from 10-1 are:")
for i in range(10,0,-1):
    print(i)
#Even and odd numbers upto 100
print("The even numbers upto 100:")
for i in range(2,101,2):
    print(i)
print("The odd numbers upto 100:")
for i in range(1,100,2):
    print(i)
#Print sum of n numbers
n=int(input("Enter a number:"))
temp=0
for i in range(1,n+1,1):
    temp+=i
    print(temp)
#Factorial of a number
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1,1):
    fact=fact*i
    print(fact)"""
#Sum of squares of number
n=int(input("Enter a number:"))
temp=0
for i in range(1,n+1,1):
    temp=temp+i*i
    print(temp)
    
    
        
    
