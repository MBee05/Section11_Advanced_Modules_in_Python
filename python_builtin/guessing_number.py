'''import random

number = random.randint(1,10)

guess = 0

while guess != number:
    
    guess = int(input('Enter guess:'))
    if (guess < number):
        print ('Guess higher!')
    elif (guess > number):
        print('Guess lower!')
    else:
        print('you won!')'''
        
        
        
#answer
'''from random import randint
#generate a numb 1 to 10
answer = randint(1,10)

# input from user?
#guess = input('guess a number 1 to 10: ')


#check that input is a nuber 1 to 10
while True:
    try:
        guess = int(input('guess a number 1 to 10: '))
        #print(answer) _ to check if its working
        if  0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('try again!')
    except ValueError:
        print('please enter a number')
        continue

# check if the number is the right guess. Otherwise ask again.'''





from random import randint
import sys 
#generate a numb 1 to 10
answer = randint(int(sys.argv[1], int(sys.argv[10])))

# input from user?
#guess = input('guess a number 1 to 10: ')


#check that input is a nuber 1 to 10
while True:
    try:
        guess = int(input('guess a number 1 to 10: '))
        #print(answer) _ to check if its working
        if  0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('try again!')
    except ValueError:
        print('please enter a number')
        continue