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

## Regex

1. `import re`
2. `regex = re.compile(r'...', re.DOTALL?)`
3. `match = regex.search(text)`
4. `finding = match.group()`

> <tt><small>group(0) = group(), group(0, 1, 2, ...)</small></tt> > <tt><small>groups() - tuple of groups without `0`</small></tt>

> <tt>greedy</tt> - <small>longest</small> <tt>non-greedy</tt> - <small>shortest</small>

| Mark  | Meaning                         |
| ----- | ------------------------------- |
| `*`   | match zero or more              |
| `*?`  | match zero or more (non-greedy) |
| `+`   | match one or more               |
| `+?`  | match one or more (non-greedy)  |
| `()`  | mini regex (group)              |
| `{}`  | range                           |
| `{}?` | range (non-greedy)              |
| `[]`  | any of                          |
| `[^]` | !any of                         |
| `.`   | any character (except `\n`)     |

| Python                                                   | Javascript                                     |
| -------------------------------------------------------- | ---------------------------------------------- |
| `re.compile(r'search_value').sub(replace_value, string)` | `string.replace(/searchValue/g, replaceValue)` |

## Files

### Reading

```
file = open(file, 'r')
file.read()
file.close()
```

### Writing

```
baconFile = open(file, 'w')
file.write(text)
file.close()
```

### Append

```
baconFile = open(file, 'a')
file.write(text)
file.close()
```

### _shelve_ module

```
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
```

## Analogy with Javascript

### I/O

| Python                              | Javascript                  |
| ----------------------------------- | --------------------------- |
| `input(default_value)`              | `prompt(msg, defaultValue)` |
| `print(...args, sep=' ', end='\n')` | `console.log(...args)`      |

### Modules

![](http://heropublic.oss-cn-beijing.aliyuncs.com/080516.png)

| Python                                                   | Javascript                                         |
| -------------------------------------------------------- | -------------------------------------------------- |
| `import random`                                          | `import random from 'random'`                      |
| `from random import randint`                             | `import { randint } from 'random'`                 |
| `type(something)`                                        | `typeof something`                                 |
| `re.compile(r'search_value').sub(replace_value, string)` | `string.replace(/searchValue/g, replaceValue)`     |
| `os.getcwd()`                                            | `process.cwd()`                                    |
| `os.chdir('..')`                                         | `process.chdir('..')`                              |
| `os.listdir(os.getcwd())`                                | `fs.readdirSync(process.cwd(), (err, fol) => fol)` |
| `os.path.getsize(file)`                                  | `fs.statSync(file).size`                           |

### Expression

#### Dictionary

| Python                                | Javascript                                                |
| ------------------------------------- | --------------------------------------------------------- |
| `'name' in {name: 'Ramzan', age: 23}` | `Object.keys({name: 'Ramzan', age: 23}).includes('name')` |
| `{name: 'Ramzan', age: 23}.items()`   | `_.toPairs({name: 'Ramzan', age: 23})`                    |

#### String

| Python                 | Javascript                                                  |
| ---------------------- | ----------------------------------------------------------- |
| `'Ramzan' + str(1996)` | `'Ramzan' + 1996`                                           |
| `len('Ramzan')`        | `'Ramzan'.length`                                           |
| `'Ramzan'.isalpha()`   | `/^[a-z]+$/i.test('Ramzan')`                                |
| `'Ramzan'.isalnum()`   | `/^[a-z0-9]+$/i.test('Ramzan')`                             |
| `'Ramzan'.isdecimal()` | `/^[0-9]+$/.test('Ramzan')`                                 |
| `'Ramzan'.isspace()`   | `/^\s+$/.test('Ramzan')`                                    |
| `'Ramzan'.istitle()`   | `/^([\W\d]|\b[A-Z]+\s?|\b[A-Z][a-z]+\s?)+$/.test('Ramzan')` |
| `'Ramzan'.strip()`     | `'Ramzan'.trim()`                                           |
| `'Ramzan'.split()`     | `'Ramzan'.split(' ')`                                       |

```
# String
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
```

#### List and Tuple

| Python                                | Javascript                               |
| ------------------------------------- | ---------------------------------------- |
| `[1, 2, 3] + [4, 5]`                  | `[1, 2, 3].concat([4, 5])`               |
| `[1, 2, 3].append(4)`                 | `[1, 2, 3].push(4)`                      |
| `[1, 2, 3].insert(0, 4)`              | `[1, 2, 3].unshift(4)`                   |
| `del arr[i]`                          | `arr.splice(i, 1)`                       |
| `[1, 2, 3].remove(2)`                 | `[1, 2, 3].splice([1, 2, 3].indexOf(2))` |
| `'Ramzan' in ['Ramzan', 1996]`        | `['Ramzan', 1996].includes('Ramzan')`    |
| `'Ramzan' not ['Ramzan', 1996]`       | `!['Ramzan', 1996].includes('Ramzan')`   |
| `(1, 2, 3)`                           | `Object.freeze([1, 2, 3])`               |
| `tuple([1, 2, 3]) list((1, 2, 3))`    | `Array(1, 2, 3)`                         |
| `copy.copy([1, 2, 3])`                | `_.clone([1, 2, 3])`                     |
| `', '.join(['cats', 'rats', 'bats'])` | `['cats', 'rats', 'bats'].join(', ')`    |

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

### Data types and variables

| Python              | Javascript                  |
| ------------------- | --------------------------- |
| `True`              | `true`                      |
| `False`             | `false`                     |
| `False`             | `false`                     |
| `None`              | `undefined` `null`          |
| `one, two = [1, 2]` | `const [one, two] = [1, 2]` |

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

### Chapter 5

1. `{}`
2. `{ 'foo': 42 }`
3. unlike to list data type for indexes in dictionary can be `str`
4. it return 100
5. no difference
6. `'cat' in spam` is are same as `'cat' in spam.keys()`
7. `spam.setdefault('color', 'black')`
8. `pprint.pprint()`

### Chapter 6

1. escape character - character that impossible put into string
2. `\t` - tab, `\n` - newline
3. `\\`
4. because it ends string
5. with using triple quotes `'''`
6. e, Hello, Hello, lo World!
7. HELLO, True, hello
8. `['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']`
9. `rjust()`, `ljust()`, `center()`
10. `rstrip()`, `lstrip()`, `strip()`

### Chapter 7

1. `re.compile(pattern)`
2. backslashes in python using for escaping, we do not same behavior in regex
3. search returns a Match object
4. you can get actual strings with `group` method of Match object
5. in `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, group(0) covers whole match, group(1) 3 first digits, groups(2) 7 last digits
6. I would specify that I want actual regex match to parentheses or period character with `\`
7. `findall` returns list of string or tuples (if it's been specified group(s))
8. `|` means one of
9. `?` means match zero or one of the preceding group
10. `*` - zero or more, `+` - one or more
11. `{3}` match which exactly 3, `{3,5}` match all between 3 and 5
12. `\d` - numeric; `\w` - letter, numeric, underscore; `\s` - space, tab, newline
13. `\D` - !numeric; `\W` - !letter, !numeric, !underscore; `\s` - !space, !tab, !newline
14. you make case insensitive with flag `re.I`
15. `.` match every character except newlines, with flag `re.DOTALL` it also will match to newlines
16. `.*?` unlike `.*` activates non-greedy mode (which means stop at first match)
17. `[0-9a-z]` all numbers and lowercase letter
18. `re.compile(r'\d+').sub('X', '12 drummers, 11 pipers, five rings, 3 hens')` should return string with replaced number with `X`
19. `re.VERBOSE` makes ignore `#` and everything after it, also ignores extra spaces
20. `(^\d{,3}$)|(^\d,(\d{3}\,?)+)` for matching number with commas for every three digits
21. `([A-Z]\w+)\sNakamoto` for matching full name of someone whose last name is Nakamoto
22. `(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$` for matching certain sentences

### Chapter 8

1. relative path is relative program's cwd **not to file!**
2. absolute path start with the root folder
3. `os.getcwd()` return string of cwd, `os.chdir()` changes cwd
4. `.` - cwd, `..` - parent to cwd
5. in `C:\bacon\eggs\spam.txt`, `C:\bacon\eggs` is dirname and `spam.txt` is base name
6. `open` can be called with mode `r, w, a`
7. write mode overwrite the existing file
8. `read()` returns string, `readlines` returns list
9. shelf resemble to dictionary data type
