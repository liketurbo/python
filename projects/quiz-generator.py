from os import path
from random import shuffle, sample
import re

file_path = './data/us-state-capitals.csv'

if (path.exists(file_path)):
  print('File exists, we\'re good to go')

if (path.isfile(file_path) and not path.isdir(file_path)):
  print('Not dir, it\'s file')

print('The file has size of {0} bytes'.format(path.getsize(file_path)))
print('File\'s dirname - "{0}", basename - "{1}"'.format(
    path.dirname(file_path), path.basename(file_path)))

state_capitals = {}
state_capitals_file = open(file_path, 'r')
for i, line in enumerate(state_capitals_file):
  state, capital = re.search(r'(.+),(.+),(.+),(.+)', line).groups()[0:2]
  state_capitals[state] = capital
state_capitals_file.close()

for quiz_num in range(35):
  quiz_file = open('./dist/capitals-quiz-%s' % (quiz_num + 1), 'w')
  answer_key_file = open('./dist/capitals-answers-%s' % (quiz_num + 1), 'w')

  quiz_file.write('Name:\nDate:\n\n')
  quiz_file.write('State Capitals Quiz #%s\n\n' % (quiz_num + 1))

  answer_key_file.write('State Capitals Answers #%s\n\n' % (quiz_num + 1))

  states = state_capitals.keys()
  shuffle(states)

  for question_num in range(50):
    correct_answer = state_capitals[states[question_num]]

    wrong_answers = state_capitals.values()
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = sample(wrong_answers, 3)

    answer_options = wrong_answers + [correct_answer]
    shuffle(answer_options)

    quiz_file.write('%s. Capital of %s is ...\n' %
                    (question_num + 1, states[question_num]))
    for i in range(4):
      quiz_file.write('  %s. %s\n' % ('ABCD'[i], answer_options[i]))
    quiz_file.write('\n')

    answer_key_file.write('%s. %s\n' % (
        question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))

  quiz_file.close()
  answer_key_file.close()
