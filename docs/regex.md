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
