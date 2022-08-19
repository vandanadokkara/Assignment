"""l=[2,4,6,8,12]
print(l)
l.append(14)
print(l)
l.insert(1,3)
print(l)
l1=[11,12,13]
l.extend(l1)
print(l)
print(sum(l))
print(l.count(2))
print(l.count(88))
print(min(l))
print(max(l))
l.reverse()
print(l)
l.sort()
print(l)
l.pop(1)
print(l)
l.remove(2)
print(l)
l.copy()
print(l)
l.clear()
print(l)
#List slicing
l=[22,65,98,21,13,60,14,40,8]
print(l)
print(l[2:6])
print(l[:6])
print(l[3:])
print(l[4:4])
print(l[:-4])
print(l[0:-2])
print(l[-5:5])
print(l[:])
print(l[::3])"""
#Reverse the elements of the list
"""l=[]
x=int(input("Enter no.of elements in the list:"))
for i in range(0,x):
    a=input("Enter the elemets:")
    l.append(a)
print(l)
p=l[::-1]
print("List in reverse order:",p)
#Concatenation of two lists index-wise
l1=[2,4,6,8,10]
l2=[1,3,5,7,9]
l3=[i+j for i,j in zip(l1,l2)]
print(l3)
#Turn every item of list into lists square
l=[2,4,6,8,10]
result=[a*a for a in l]
print(result)"""
#TUPLES:
"""t=(2,4,1,3,7,5,8,7,6,2)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(t.index(5))
print(t.count(2))
print(sorted(t))
print(sorted(t,reverse=True))
print(tuple([0,9,0,7]))
print(tuple("vandana"))
print(tuple({6,7,8}))
t=(3,6,9,1,7)
for i in t:
    print(i)
#Slicing tuples
t=(12,87,34,76,26)
print(t[1:4])
print(t[:3])
print(t[5:])
print(t[4:4])
print(t[:-2])
print(t[-1:])
print(t[0:-2])
print(t[-4:2])
print(t[:])
print(t[::3])
#Reverse the given tuple
t=[]
x=int(input("Enter no.of elements in tuple:"))
for i in range(0,x):
    a=input("Enter the elements:")
    t.append(a)
print(tuple(t))
p=t[::-1]
print("Tuple in reverse order:",p)"""
#Swap two tuples
"""l1=[2,3,4,5]
l2=[6,7,8,9]
print(l1)
print(l2)
print("After Swapping:")
l1,l2=l2,l1
print(l1)
print(l2)
#Count
l=[1,7,4,2,4,6]
print(l)
p=int(input("Enter a number you want to count:"))
print(l.count(p))"""
#Sets:
"""s={3,8,5,1,6,1}
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(sorted(s))
print(sorted(s,reverse=True))
s.add(9)
print(s)
s.update([30,40,10],{50,60})
print(s)
s1={1,2,3}
s2={4,5,6}
s3={7,8,9}
print(s1.union(s2,s3))
print(s1.intersection(s2))
s1={2,4,5}
s2={2,4,6}
print(s1.difference(s2))"""
"""s1={2,4,6}
s2={2,3,4}
print(s1.symmetric_difference(s2))
s1=s2.copy()
print(s1)
print(s1.isdisjoint(s2))
s1={1,2,3}
s2={1,2,3,4}
print(s1.issubset(s2))
print(s1.issuperset(s2))
a={1,2,3,4}
for i in a:
    print(i)"""

      

