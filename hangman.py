#Step 1 
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import hangman_word
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import hangman_art 

print(hangman_art.logo)

chosen_word = random.choice(hangman_word.word_list)
print(chosen_word)
#TODO-6: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

 #TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.       

display = []
for letter in chosen_word:
    display += "_"

print (display)
gameOn = True

#TODO-5: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


while gameOn:
    
   
    if "_" not in display:
        gameOn = False
        print("You win!")
    else:
        guess = input("guess a letter").lower()
         #TODO-8: - If the user has entered a letter they've already guessed, print the letter and let them know.
        

        if guess in display:
            print("you already used this letter")
        
    
        for letterPosition in range(len(chosen_word)):
            letter = chosen_word[letterPosition]
            if guess == letter:
                display[letterPosition] = letter
            

    #TODO-7: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    
        if guess not in chosen_word:
            lives-=1
        #TODO-9: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print("letter not in word")
            if lives == 0:
                gameOn = False
                print("you lose")
   
            
    print(stages[lives])
    print(display)