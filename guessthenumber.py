import random 
number = random.randrange(1,10)
guesses = 1

print('\t\t\t\tCan you guess the secret number?')
print('Try to guess the number between 1 and 10 with three trials')

while guesses < 4:
  guess = int(input('\n Enter your guess: '))
  if guess == number:
    print(f'You guessed it on trial {guesses}! Great job!')
    break
  elif guess > number:
    print ("Oh snap! your guess is higher, try again")
  elif guess < number:
    print("Oh no! your guess is lower")
  guesses += 1
else:
  print('\n Game Over! \n\t Run to try again!')

