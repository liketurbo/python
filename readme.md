# Python learning

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
```

## Variable rules

- It can be only one word
- It can use only letters, numbers, and the underscore (\_) character
- It can’t begin with a number

## Analogy with Javascript

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

### Other

| Python                       | Javascript                         |
| ---------------------------- | ---------------------------------- |
| `len('Ramzan')`              | `'Ramzan'.length`                  |
| `input(default_value)`       | `prompt(msg, defaultValue)`        |
| `'Ramzan' + str(1996)`       | `'Ramzan' + 1996`                  |
| `import random`              | `import random from 'random'`      |
| `from random import randint` | `import { randint } from 'random'` |

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
