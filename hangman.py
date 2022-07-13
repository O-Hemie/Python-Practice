# Hangman Ascii art
import random
import words_bank
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print('To play the hangman game, the computer will choose a word at random; you will try to guess what the word is one letter at a time. If the letter you guess occurs in the word, the computer fills in the blanks with that letter in the right places. \n\n\t\tHINT: THE WORDS ARE NAMES OF ANIMALS. \n\nREADY TO PLAY?')

def thinkword():
  words = words_bank.words
  
#random word and random word list
  comp_choice = random.choice(words)
  comp_choice_list = list(comp_choice)
 
  
# creating blank line
  blank_list = ['_'] * len(comp_choice)
  print(' '.join(blank_list))
  
  lives = 0
  
# creating game in a loop
  while True:
    # check if user has run out of lives
    if lives == len(HANGMANPICS):
      print('Game Over! You have run out of guesses')
      break
      
# asking for user guess
    user_input = input('Guess a letter: ')
  
# check if the  guessed letter is a part of the random word
    for word in range(len(comp_choice)):
      if user_input == comp_choice_list[word]:
        blank_list[word] = user_input
    if '_' not in blank_list:
      print('You are awesome!')
  
# if user guess is wrong
    if user_input not in comp_choice_list:
      print(HANGMANPICS[lives])
      lives += 1
  
# checking if the user gets all words
    if '_' not in blank_list:
      print('Hooray! You win! 🏆')
      break
    print(' '.join(blank_list))
  thinkword()

thinkword()
