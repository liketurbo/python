#! python3
# mad-libs - some silly program for generating sentences

adj = input('Enter an adjective: ')
noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
noun_2 = input('Enter a noun: ')

sent = '\
The %s panda walked to the %s and then %s. A nearby %s was \
unaffected by these events.' % (adj, noun, verb, noun_2)

print(sent)

file = open('./dist/sent.txt', 'w')
file.write(sent)
file.close()
