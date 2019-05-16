import pprint
import shelve
import os

print('<----------------------------->')
print('You currently in:', end=' ')
print(os.getcwd())

print('<----------------------------->')
file = open('./data/message-from-netflix.txt')
print(file.read())
print(file.readlines())

print('<----------------------------->')
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

print('<----------------------------->')
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

print('<----------------------------->')
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

print('<----------------------------->')
cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]
fileObj = open('./crash-course/myCats.py', 'w')
fileObj.write('cats = ' + str(cats) + '\n')

fileObj.close()

# print('<----------------------------->')
# print(myCats.cats)
# print(myCats.cats[0])
# print(myCats.cats[0]['name'])
