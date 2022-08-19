Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
d[1]="vandana"
d[2]="manoj"
d[3]="joshna"
d
{1: 'vandana', 2: 'manoj', 3: 'joshna'}
d[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d[0]
KeyError: 0
d.index(1:"vandana")
SyntaxError: invalid syntax
d.index(1)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d.index(1)
AttributeError: 'dict' object has no attribute 'index'
type(d)
<class 'dict'>
d[1]
'vandana'
d[4]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d[4]
KeyError: 4
d.get(1)
'vandana'
d.get(3)
'joshna'
d[4]="kamala"
d[5]="apparao"
d
{1: 'vandana', 2: 'manoj', 3: 'joshna', 4: 'kamala', 5: 'apparao'}
d[1]="vandu"
d
{1: 'vandu', 2: 'manoj', 3: 'joshna', 4: 'kamala', 5: 'apparao'}
d.pop()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
d.pop(1)
'vandu'
d
{2: 'manoj', 3: 'joshna', 4: 'kamala', 5: 'apparao'}
d.popitem()
(5, 'apparao')
d
{2: 'manoj', 3: 'joshna', 4: 'kamala'}
del d
d
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
d
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
d[1]="vandana"d[2]="manoj"
SyntaxError: invalid syntax
d[1]="vandana"
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d[1]="vandana"
NameError: name 'd' is not defined. Did you mean: 'id'?
d[1]="vandana"
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d[1]="vandana"
NameError: name 'd' is not defined. Did you mean: 'id'?
x[0]="vandana"
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x[0]="vandana"
NameError: name 'x' is not defined
x={}
type(x)
<class 'dict'>
x[0]="vandana"
x[1]="manoj"
x[2]="kamala"
x
{0: 'vandana', 1: 'manoj', 2: 'kamala'}
x.clear()
x
{}
x[0]="vandana"
x[1]="manoj"
x[2]="kamala"
x
{0: 'vandana', 1: 'manoj', 2: 'kamala'}
x.values()
dict_values(['vandana', 'manoj', 'kamala'])
x.keys()
dict_keys([0, 1, 2])
a.items()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.items()
NameError: name 'a' is not defined
x.items()
dict_items([(0, 'vandana'), (1, 'manoj'), (2, 'kamala')])
d=x.copy()
d
{0: 'vandana', 1: 'manoj', 2: 'kamala'}
x={}
x={"a","v","m","k","j}
   
SyntaxError: unterminated string literal (detected at line 1)
x={"a","v","m","k","j"}
   
vaules=["vandana"]
   
d=dict.fromkey(x,values)
   
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    d=dict.fromkey(x,values)
AttributeError: type object 'dict' has no attribute 'fromkey'. Did you mean: 'fromkeys'?
d=dict.fromkeys(x,values)
   
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    d=dict.fromkeys(x,values)
NameError: name 'values' is not defined. Did you mean: 'vaules'?
x={"a","v","m","k","j"}
   
vaule=["vandana"]
   
d=dict.fromkeys(x,value)
   
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d=dict.fromkeys(x,value)
NameError: name 'value' is not defined. Did you mean: 'vaule'?
x={"a","v","m","k","j"}
   
value=["vandana"]
   
d=dict.fromkeys(x,vaule)
   
d
   
{'a': ['vandana'], 'v': ['vandana'], 'm': ['vandana'], 'k': ['vandana'], 'j': ['vandana']}
s=[1:"joshna"]
   
SyntaxError: invalid syntax
s={1:"joshna"}
   
d.update(s)
   
d
   
{'a': ['vandana'], 'v': ['vandana'], 'm': ['vandana'], 'k': ['vandana'], 'j': ['vandana'], 1: 'joshna'}
d[2]="Neelu"
   
d
   
{'a': ['vandana'], 'v': ['vandana'], 'm': ['vandana'], 'k': ['vandana'], 'j': ['vandana'], 1: 'joshna', 2: 'Neelu'}
