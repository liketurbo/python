## Files

### Reading

```python
file = open(file, 'r')
file.read()
file.close()
```

### Writing

```python
baconFile = open(file, 'w')
file.write(text)
file.close()
```

### Append

```python
baconFile = open(file, 'a')
file.write(text)
file.close()
```

### _shelve_ module

```python
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
```
