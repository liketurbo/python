# Python

## Operators

| Operator | Name                              | Example         |
| -------- | --------------------------------- | --------------- |
| `*`      | Multiplication                    | `3 * 5 ⇒ 15`    |
| `**`     | Exponent                          | `2 ** 3 ⇒ 8`    |
| `/`      | Division                          | `22 / 8 ⇒ 2.75` |
| `//`     | Integer division/floored quotient | `22 // 8 ⇒ 2`   |

```
'Ramzan' (+|-|/) 2 ⇒ error
'Ramzan' * 2.0 ⇒ error
'Ramzan' * 2 ⇒ RamzanRamzan
['Ramzan'] * 2 ⇒ ['Ramzan', 'Ramzan']
```

## Statement vs expression

> if you can assign it to a variable - <b>expression</b>

```
2 + 2
3 * 7
1 + 2 + 3 * (8 ** 9) - sqrt(4.0)
min(2, 22)
max(3, 94)
round(81.5)
"foo"
"bar"
"foo" + "bar"
None
True
False
2
3
4.0
```

> if you can't - <b>statement</b>

```
if CONDITION:
elif CONDITION:
else:
for VARIABLE in SEQUENCE:
while CONDITION:
try:
except EXCEPTION as e:
class MYCLASS:
def MYFUNCTION():
return SOMETHING
raise SOMETHING
with SOMETHING:
```

## Variable rules

- It can be only one word
- It can use only letters, numbers, and the underscore (\_) character
- It can’t begin with a number

- primitives: `bool` `int` `float` `str` stores variable
- non-primitives: `tuple` `list` stores reference

## Analogy with Javascript

### I/O

| Python                              | Javascript                  |
| ----------------------------------- | --------------------------- |
| `input(default_value)`              | `prompt(msg, defaultValue)` |
| `print(...args, sep=' ', end='\n')` | `console.log(...args)`      |

### Module

| Python                       | Javascript                         |
| ---------------------------- | ---------------------------------- |
| `import random`              | `import random from 'random'`      |
| `from random import randint` | `import { randint } from 'random'` |
| `type(something)`            | `typeof something`                 |

### Expression

| Python                             | Javascript                               |
| ---------------------------------- | ---------------------------------------- |
| `'Ramzan' + str(1996)`             | `'Ramzan' + 1996`                        |
| -                                  | -                                        |
| `[1, 2, 3] + [4, 5]`               | `[1, 2, 3].concat([4, 5])`               |
| `[1, 2, 3].append(4)`              | `[1, 2, 3].push(4)`                      |
| `[1, 2, 3].insert(0, 4)`           | `[1, 2, 3].unshift(4)`                   |
| `del arr[i]`                       | `arr.splice(i, 1)`                       |
| `[1, 2, 3].remove(2)`              | `[1, 2, 3].splice([1, 2, 3].indexOf(2))` |
| `'Ramzan' in ['Ramzan', 1996]`     | `['Ramzan', 1996].includes('Ramzan')`    |
| `'Ramzan' not ['Ramzan', 1996]`    | `!['Ramzan', 1996].includes('Ramzan')`   |
| `(1, 2, 3)`                        | `Object.freeze([1, 2, 3])`               |
| `tuple([1, 2, 3]) list((1, 2, 3))` | `Array(1, 2, 3)`                         |
| `copy.copy([1, 2, 3])`             | `_.clone([1, 2, 3])`                     |

### Data types and variables

| Python              | Javascript                  |
| ------------------- | --------------------------- |
| `True`              | `true`                      |
| `False`             | `false`                     |
| `False`             | `false`                     |
| `None`              | `undefined` `null`          |
| `one, two = [1, 2]` | `const [one, two] = [1, 2]` |

#### List

> index

```
anim = ['cat', 'bat', 'rat', 'elephant']

anim[1] # 'bat'
anim[-1] # 'elephant'
```

> slice

```
# f_number - start index; s_number - up to, but not include
anim[1:3] # ['bat', 'rat']
anim[2:-1] # ['rat']
anim[1:] # ['bat', 'rat', 'elephant']
anim[:-1] # ['cat', 'bat', 'rat']
anim[:] # ['cat', 'bat', 'rat', 'elephant']
```

### Conditions

| Python                   | Javascript                      |
| ------------------------ | ------------------------------- |
| `True or False`          | `true \|\| false`               |
| `True and False`         | `true && false`                 |
| `not True`               | `!true`                         |
| `if name == 'Ramzan':`   | `if (name === 'Ramzan') {}`     |
| `elif name == 'Ramzan':` | `else if (name === 'Ramzan) {}` |

### Loops

| Python                      | Javascript                           |
| --------------------------- | ------------------------------------ |
| `for i in range(5):`        | `for (let i = 0; i < 5; i++) {}`     |
| `for i in range(12, 16):`   | `for (let i = 12; i < 16; i++) {}`   |
| `for i in range(1, 10, 2):` | `for (let i = 1; i < 10; i += 2) {}` |
| `for i in [1, 10, 2]:`      | `for (const i of [1, 10, 2]) {}`     |

### Functions

| Python          | Javascript        |
| --------------- | ----------------- |
| `len('Ramzan')` | `'Ramzan'.length` |

## Answers (Albert Sweigart - Automate the Boring Stuff with Python)

### Chapter 1

1. operator; value; value; operator; operator; operator; value;
2. spam - variable; 'spam' - string;
3. str, int, float;
4. expressions consist values; expressions always evaluate;
5. assignments store values;
6. 20
7. spamspamspam; spamspamspam;
8. (look at variable rules)
9. str(), int(), float()
10. (look at operators)

### Chapter 2

1. True, False
2. and, or, not
3. True and True ⇒ True, True and False ⇒ False, False and False ⇒ True; True or True ⇒ True, True or False ⇒ True, False or False ⇒ False; not True ⇒ False, not False ⇒ True
4. False, False, True, False, True
5. ==, !=, <, >, <=, >=
6. one comparison, another assignment
7. a condition (that is, an expression that evaluates to True or False); in statements
8. if, if, else
9. `if spam == 1: print('Hello') elif spam == 2: print('Howdy') else: print('Greeting')`
10. Ctrl-C
11. break - breaks loop, continue - same as reaching end of a loop
12. (look at loops)
13. `for i in range(1, 11): print(i)`; `i = 1 while i < 11: print(i)`
14. `spam.bacon()`

### Chapter 3

1. group code that get executed multiple times
2. defined after `def` statement, executed when function is called, called after defining
3. `def`
4. function call unlike function evaluate what inside function
5. one global scope, as many local scope as many functions
6. it stops existing
7. value that would be returned by function; yes, it can be part of expression
8. `None`
9. by reserved word `global`
10. NoneType data type
11. it defines variable named `areallyourpetsnamederic`
12. spam.bacon()
13. use `try: except Exception:`
14. in `try` goes everything before it been catch by `Exception`

### Chapter 4

1. a list value
2. `spam[2] = 'Hello'`
3. `d`
4. `d`
5. `['a', 'b']`
6. returns `1`
7. adds `99` at the end of a list
8. removes value `cat` from a list
9. `+`, `copy.copy`
10. `append` adds at the end, `insert` inserts value at selected index
11. by index `del arr[num]`, by value `arr.remove(value)`
12. strings as list has index, substring, include
13. tuple alike to list immutable
14. `(42)`
15. tuple ⇒ list `list(tuple_arr)`, list ⇒ tuple `tuple(list_arr)`
16. address to the list
17. `copy.deepcopy` alike `copy.copy` copies inner lists as well
