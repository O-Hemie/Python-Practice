# DONT TOUCH THE CODE IN THIS SECTION 👇
import random

rps = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
# END OF SECTION 👆

# WRITE YOUR CODE BELOW THIS LINE 👇
#print(rps[2])

#introduction
print('How good are you in a game of Rock Paper Scissors? If you said very good try beating the computer. If you have not played it before, try it out I\'m sure you will enjoy it. All you have to do is pick a guess from rock, paper or scissors.')
print('\nGAME RULE: \n\t "rock smashes scissors-rock wins" \n\t "scissors cuts paper- scissors wins" \n\t "paper covers rocks- paper wins"')

scissors = rps[2]
paper = rps[1]
rock = rps[0]
choices = ['rock', 'paper', 'scissors']
again = ['y', 'n']
print("\n\n\t\t ARE YOU READY TO PLAY?")
print(f'\nYour choices are: {choices}')
while True:
  computer_selection = random.choice(choices)
  user_choice= input("\n\nENTER YOUR CHOICE, you can choose to quit too: ").lower()
  if user_choice not in choices and user_choice != 'quit':
    print('INVALID CHOICE!')
  elif user_choice == 'quit':
    print('GAME OVER!')
    break

#reassigning user_choice string to variable
  if user_choice == 'rock':
    user_choice = rock
  elif user_choice == 'paper':
    user_choice = paper
  elif user_choice == 'scissors':
    user_choice = scissors
    
  #reassigning computer_selection string to variable
  if computer_selection == 'rock':
    computer_selection = rock
  elif computer_selection== 'paper':
    computer_selection= paper
  elif computer_selection == 'scissors':
    computer_selection = scissors
    
    
  #GAME RULE
  if user_choice == rock and computer_selection == scissors:
    print('\n YOU WIN🎉!')
    print(f"\nYou chose {user_choice} \n'V/S' \n and Computer chose {computer_selection}")
  elif user_choice == scissors and computer_selection == rock:
    print('\nCOMPUTER WON🎈!')
    print(f"\nYou chose {user_choice} \n'V/S' \n and Computer chose {computer_selection}")
  elif user_choice == scissors and computer_selection == paper:
    print('\n YOU WIN🎉!')
    print(f"You chose {user_choice} \n'V/S' \n and Computer chose {computer_selection}")
  elif user_choice == paper and computer_selection == scissors:
    print('\nCOMPUTER WON🎈!')
    print(f"\nYou chose {user_choice} \n'V/S' \n and Computer chose {computer_selection}")
  elif user_choice == paper and computer_selection == rock:
    print('\n YOU WIN🎉!')
    print(f"\nYou chose {user_choice} \n'V/S' \n and Computer chose {computer_selection}")
  elif user_choice == rock and computer_selection == paper:
    print('\nCOMPUTER WON🎈!')
    print(f"\nYou chose {user_choice} \n'V/S' \n and Computer chose {computer_selection}")
  elif user_choice == computer_selection: 
    print('\n IT\'S A DRAW👏!')
    print(f"\nYou chose {user_choice} \n'V/S' \n and Computer chose {computer_selection}")




  
   





  
