# Python

- [Debugging](./docs/debugging.md)
- [Files](./docs/files.md)
- [Analogy with Javascript](./docs/js-analogy.md)
- [Regex](./docs/regex.md)

## Operators

| Operator | Name                              | Example         |
| -------- | --------------------------------- | --------------- |
| `*`      | Multiplication                    | `3 * 5 ⇒ 15`    |
| `**`     | Exponent                          | `2 ** 3 ⇒ 8`    |
| `/`      | Division                          | `22 / 8 ⇒ 2.75` |
| `//`     | Integer division/floored quotient | `22 // 8 ⇒ 2`   |

```
'Bob' (+|-|/) 2 ⇒ error
'Bob' * 2.0 ⇒ error
'Bob' * 2 ⇒ BobBob
['Bob'] * 2 ⇒ ['Bob', 'Bob']
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

### Chapter 9

1. `shutil.copy` copies single file, while `shutil.copytree` copies directory
2. `shutil.move` used for renaming files `shutil.move(source, destination)` "move and rename"
3. `shutil.rmtree` removes permanently folder (only, not file), `send2trash` sends to trash file and folders
4. `zip_file = zipfile.ZipFile('file.zip'); zip_file.write('./spam.txt'); zip_file.close();`

### Chapter 10

1. `assert spam > 10, 'spam less than zero'`
2. `assert egg.lower() != bacon.lower(), 'egg and bacon are the same string'`
3. `assert False, 'this errors always trigger`
4. `import logging; logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')`
5. `import logging; logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')`
6. `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
7. `logging.disable(logging.CRITICAL)`
8. You've have to separate program print from debug print and less powerful api
9. `Step` goes line by line; `Over` line by line, but doesn't go inside of function; `Out` gets you out of function
10. Debugger stops at breakpoint
11. Breakpoint is selected line where debugger stops
12. By clicking on line

### Chapter 11

1. `webbrowser` - web browser controller, `requests` - making http requests, `BeautifulSoup` - html parser, `selenium` - simulator of human interactions
2. `requests.get` returns `Response` object; to get text value use `res.text`
3. To check that download worked, use `requests.raise_for_status()`
4. Get status code with `res.status_code`
5. `file = open('file_name')` `file.write(chunk)` `file.close`
6. `ctrl-shift-j` - for console, `ctrl-shift-i` - for inspect
7. I guess, by clicking 😁
8. To find element with an id attribute of main - `#main`
9. To find elements with a CSS class of highlight - `.highlight`
10. To find all the <div> elements inside another <div> element - `div > div`
11. To find the <button> element with a value attribute set to favorite - `button[value="favorite"]`
12. `elem.innerText` of JS works as `elem.getText()` of Python
13. Get all attributes `elem.attrs`
14. Import selenium `from selenium import webdriver`
15. `find_element` returns one element, `find_elements` returns array of elements
16. `elem.click` mouse click simulation, `elem.send_keys('keys')` keyboard simulating
17. You can call on any element submit method `elem.submit()`
18. `browser.back()` `browser.forward()` `browser.refresh()` `browser.quite()`

### Chapter 12

1. `openpyxl.load_workbook()` returns value of _workbook_ data type
2. `get_sheet_names()` returns list of names of sheets
3. To retrieve sheet named _'Sheet1'_ I'll use method `get_sheet_by_name(<name>)`
4. To retrieve active sheet I'll use method called `get_active_sheet()`
5. I would retrieve value from cell _C5_ using `sheet['C5'].value` or `sheet.cell(r=3, c=5)`
6. I would write value to cell _C5_ using `sheet['C5'] = 'value'` or `sheet.cell(r=3, c=5).value = 'value'`
7. Already mentioned it in the answer _5_ and _6_
8. `max_row` and `max_column` it is property of integer
9. I can get index of _'M'_ with `column_index_from_string(<letter[s]>)`
10. I can get letter of _14_ with `get_column_letter(<index>)`
11. Get range from _A1_ to _F1_ `sheet['A1':'F1']`
12. To save changes `wb.save(<file_name>)`
13. U set formula just like u set another value
14. If you wanna retreat result instead of formula itself `openpyxl.load_workbook(<name_of_file>, data_only=True)`
15. Sets height of row 5 to 70 `sheet.row_dimensions[5].height = 70`
16. Hides column C `sheet.column_dimensions['B'].width = 20`
17. _OpenPyXL 2.1.4_ doesn't know how to load
18. _Freeze pane_ it's row or column that stays when you scroll
19. Creating bar chart
    1. Create _Reference_ object `openpyxl.charts.Reference(sheet, start_tuple, end_tuple)`
    2. Create _Series_ object `series_obj = openpyxl.charts.Series(ref_object, title)`
    3. Creating _Chart Object_ `chart_obj = openpyxl.charts.BarChart()`
    4. Adding _Series_ to _Chart Object_ `chart_obj.append(series_obj)`
    5. Adding _Chart Object_ to _Sheet_ `sheet.add_chart(chart_obj)`

### Chapter 13

1. To `PyPDF2.PdfFileReader()` you should pass _File Object_
2. For `PdfFileReader()` you pass _File Object_ opened in _rb_, for `PdfFileWriter()` opened in _wb_
3. You can get specific pages by passing number to `PdfFileReader(<FileObject>).getPage(<int>)
4. You can get number of pages with `PdfFileReader().numPages`
5. To decrypt use `PdfFileReader().decrypt(<password>)`
6. To rotate use methods `PageObject.rotateClockwise(<degree>)` `PageObject.rotateCounterClockwise(<degree>)`
7. To get _Document_ object for file named `docx.Document('./demo.docx')`
8. _Document_ contains _Paragraphs_ which contains _Runs_
9. `docx.Document(<filename>).paragraphs` returns list of paragraphs, so can access each one by index
10. _Run_ object has _bold_, _underline_, _italic_, _strike_ and _outline_ variables
11. _True_ attribute always enabled, _False_ always disabled, _None_ defaults to whatever the run's style is set to
12. To create a new document `docx.Document()` with no arguments
13. To add paragraph to _Document_ stored in variable named _doc_ `doc.add_paragraph('Hi there!')`
14. Headings can have levels from 0 to 4 (inclusive) `doc.add_heading('Some text', <heading_level>)`

### Chapter 14

1. Things that _CSV_ doesn't have oppose to _Excel_
   - Don't have type values
   - Don't have settings for font
   - Don't have multiple worksheets
   - Don't have width and height
   - Don't have merged cells
   - Don't have images and charts
2. To `csv.reader()` and `csv.writer()` you pass _File_ object
3. _Writer_ objects need be open with _'w'_ mode
4. `csv_writer.writerow()` takes in argument array
5. _delimiter_ separates columns, _lineterminator_ separates rows
6. `json.loads()` _JSON_ to _Python Object_
7. `json.dumps()` _Python Object_ to _JSON_

### Chapter 15

1. _Unix epoch_ is time reference commonly used in programming to 12 AM January 1, 1970
2. `time.time()` returns number of seconds as float value
3. `time.sleep(5)` pauses program for exactly 5 second
4. `round()` rounds float to precision you specify
5. _timedelta_ represents duration, rather moment in time
6. `threading.Thread(target=spam).start()` runs function _spam_ in separate thread
7. To avoid concurrency issues
   1. Do not use same variables from different threads
   2. Do not use same files at same time
8. `subprocess.Popen('calc')` launches calculator

### Chapter 16

1. Protocol for sending email - _SMTP_, protocol for checking and receiving email - _IMAP_
2. Log in to an _SMTP_ server
   1. `smtp_obj = smtplib.SMTP('smtp.mail.ru',587) # Creating SMTP object`
   2. `smtp_obj.ehlo() # Establish connection`
   3. `smtp_obj.starttls() # Enable encryption`
   4. `smtp_obj.login('andrey.lukin.1986@bk.ru', 'Sswwf3i0NDyo4Pv') # Login`
3. Log in to an _IMAP_ server
   1. `imap_obj = imapclient.IMAPClient('imap.mail.ru')`
   2. `imap_obj.login('andrey.lukin.1986@bk.ru', 'Sswwf3i0NDyo4Pv')`
4. `imap_obj.search()` takes array of _IMAP_ search keys
5. If got error of more that 10000 bytes, you can:
   1. Increase size limit `imapclient.imaplib._MAXLINE = 100000`
   2. Try to fetch less
6. `pyzmail` module helps parse raw messages from `imap_obj`
7. In order to use twilio you need:
   1. Twilio number
   2. Account SID
   3. Auth token
