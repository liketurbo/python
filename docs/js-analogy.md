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

```python
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

```python
anim = ['cat', 'bat', 'rat', 'elephant']

anim[1] # 'bat'
anim[-1] # 'elephant'
```

> slice

```python
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
