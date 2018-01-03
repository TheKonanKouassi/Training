person = {'name': 'Jenn', 'age': 23}

tag = 'h1'

text = 'This is a headline'

# sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(person)

# print(sentence)

#
# Part 2
#

sentence = ['The value is {:08,.2f}'.format(i) for i in range(1000, 1010)]

print(sentence)

#
# Part 3
#

from datetime import datetime

my_date = datetime(2016, 9, 24, 12, 30, 45)

print(my_date)
