Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=["vandana","joshna","manoj",1,2,3]
l[0]
'vandana'
l[0:2]
['vandana', 'joshna']
l.append(4)
l
['vandana', 'joshna', 'manoj', 1, 2, 3, 4]
l.insert(3,"kamala")
l
['vandana', 'joshna', 'manoj', 'kamala', 1, 2, 3, 4]
l.insert(4,"apparao")
l
['vandana', 'joshna', 'manoj', 'kamala', 'apparao', 1, 2, 3, 4]
l1=[5,6,7]
l.extend(l1)
l
['vandana', 'joshna', 'manoj', 'kamala', 'apparao', 1, 2, 3, 4, 5, 6, 7]
x=l.copy()
x
['vandana', 'joshna', 'manoj', 'kamala', 'apparao', 1, 2, 3, 4, 5, 6, 7]
l.append(1,2,3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.append(1,2,3)
TypeError: list.append() takes exactly one argument (3 given)
l.append(1)
l
['vandana', 'joshna', 'manoj', 'kamala', 'apparao', 1, 2, 3, 4, 5, 6, 7, 1]
l.count(1)
2
l.count(9)
0
sum(l)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sum(l)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
l1=[1,2,3,4,5]
sum(l1)
15
max(l1)
5
min(l1)
1
len(l1)
5
l.reverse()
l
[1, 7, 6, 5, 4, 3, 2, 1, 'apparao', 'kamala', 'manoj', 'joshna', 'vandana']
l1.reverse()
l1
[5, 4, 3, 2, 1]
l.sorted()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    l.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
l.sort()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
l1
[5, 4, 3, 2, 1]
l1.sort()
l1
[1, 2, 3, 4, 5]
l.pop(0)
1
l
[1, 2, 3, 4, 5, 6, 7, 'apparao', 'kamala', 'manoj', 'joshna', 'vandana']
l1.pop(0)
1
l1
[2, 3, 4, 5]
del(l[0])
l
[2, 3, 4, 5, 6, 7, 'apparao', 'kamala', 'manoj', 'joshna', 'vandana']
l1
[2, 3, 4, 5]
del(l1[0])
l1
[3, 4, 5]
l1.remove(5)
l1
[3, 4]
l.clear()
l
[]
l1.clear()
l1
[]
