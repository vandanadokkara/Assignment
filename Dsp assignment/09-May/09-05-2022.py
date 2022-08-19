Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={1,2,3,4,5,6}
type(s)
<class 'set'>
help(s)
Help on set object:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

s.discard(6)
s
{1, 2, 3, 4, 5}
s.remove(6)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.remove(6)
KeyError: 6
s.discard(6)
s
{1, 2, 3, 4, 5}
s.remove(5)
s
{1, 2, 3, 4}
s.pop()
1
s
{2, 3, 4}
s.clear()
s
set()
s={1,2,3,4,5,6}
s.pop()
1
s
{2, 3, 4, 5, 6}
s.pop(2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.pop(2)
TypeError: set.pop() takes no arguments (1 given)
s.clear()
s
set()
s.add(1)
s
{1}
s.add(2,3)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.add(2,3)
TypeError: set.add() takes exactly one argument (2 given)
s.add(2)
s
{1, 2}
s.update([3,4,5],{6,7,8})
s
{1, 2, 3, 4, 5, 6, 7, 8}
s.clear()
s
set()
s.add(1)
s.update({2,3,4},{5,6,7})
s
{1, 2, 3, 4, 5, 6, 7}
len(s)
7
max(s)
7
min(s)
1
sum(s)
28
any(s)
True
all(s)
True
s1={0}
all(s1)
False
any(s1)
False
sorted(s)
[1, 2, 3, 4, 5, 6, 7]
s.discard(6)
s.discard(7)
s.discard(5)
s
{1, 2, 3, 4}
s1={}
s1.add(5)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s1.add(5)
AttributeError: 'dict' object has no attribute 'add'
s1={5}
s1.add(6)
s1.add(7)
s1.add(8)
s1
{8, 5, 6, 7}
s.union(s1)
{1, 2, 3, 4, 5, 6, 7, 8}
s1.union(s)
{1, 2, 3, 4, 5, 6, 7, 8}
s.intersection(s1)
set()
s1.intersection(s)
set()
s.difference(s1)
{1, 2, 3, 4}
s1.difference(s)
{8, 5, 6, 7}
s1={2,4,6}
s2={2,3,4}
s1.difference(s2)
{6}
s2.difference(s1)
{3}
s1.symmetric_difference(s2)
{3, 6}
s2.symmetric_difference(s1)
{3, 6}
s1.clear()
s1
set()
s1=s.copy()
s1
{1, 2, 3, 4}
s1.isdisjoint(s)
False
s1={2,4,6}
s1.isdisjoin(s)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s1.isdisjoin(s)
AttributeError: 'set' object has no attribute 'isdisjoin'. Did you mean: 'isdisjoint'?
s1.isdisjoint(s)
False
s
{1, 2, 3, 4}
s1={5,6,7,8}
s.isdisjoint(s1)
True
s1.isdijoint(s)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s1.isdijoint(s)
AttributeError: 'set' object has no attribute 'isdijoint'. Did you mean: 'isdisjoint'?
s1.isdsjoint(s)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    s1.isdsjoint(s)
AttributeError: 'set' object has no attribute 'isdsjoint'. Did you mean: 'isdisjoint'?
s1.isdisjoint(s)
True
s.issubset(s1)
False
s.issuperset(s1)
False
s
{1, 2, 3, 4}
s1={2,3}
s.issubset(s1)
False
s1.issubset(s)
True
s1.issuperset(s)
False
s.issuperset(s1)
True
1 in s
True
i not in s
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    i not in s
NameError: name 'i' is not defined. Did you mean: 'id'?
1 not in s
False
10 in s
False
10 not in s
True
for i in s
SyntaxError: expected ':'
for i i s:
    
SyntaxError: invalid syntax
for i in s:
    print(i)

    
1
2
3
4
{frozenset([1,2,3]:4)}
SyntaxError: invalid syntax
{frozenset([1,2,3]:4}
 
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
s={1,2,3,4}
 
s.update({5,6},{7,8})
 
s
 
{1, 2, 3, 4, 5, 6, 7, 8}
x={7,4,10,5,2}
 
sorted(x)
 
[2, 4, 5, 7, 10]
s1={1,2,3}
 
s2={3,4,5}
 
s1.union(s2)
 
{1, 2, 3, 4, 5}
s2.union(s1)
 
{1, 2, 3, 4, 5}
s1.intersection(s2)
 
{3}
s2.intersection(s1)
 
{3}
s1.difference(s2)
 
{1, 2}
s2.difference(s1)
 
{4, 5}
s1.symmetric_difference(s2)
 
{1, 2, 4, 5}
s2.symmetric_difference(s1)
 
{1, 2, 4, 5}
s1={1,2,3}
 
s2={3,4,5}
 
s1.isdisjoint(s2)
 
False
s2.isdisjoint(s1)
 
False
s1.issubset(s2)
 
False
s2.issubset(s1)
 
False
s={1,2,3,4}
 
s2={3,4,5}
 
s1.issubset(s2)
 
False
s1.issuperset(s2)
 
False
s2.issuperset(s1)
 
False
s3={1,2,3,4}
 
s4={3,4}
 
s3.issuperset(s4)
 
True
s4.issuperset(s3)
 
False
s1
 
{1, 2, 3}
s
 
{1, 2, 3, 4}
s2={3,4,5}
 
5 in s
 
False
5 not in s
 
True
3 not in s2
 
False
s={1,2,3,4}
 
for i in s:
 i=i*i
 print(i)

 
1
4
9
16
