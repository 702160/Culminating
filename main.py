#Drew Johnston
#January 20th, 2023
#Culminating Project Hangman
#Show the knowledge I have gained over the course of this class

import TextDelay #Allows for the test to appear at different speeds instead of instantly
import os
from time import sleep
import random
import turtle
global record

#Establishes what the table will look like
database = []
record = []
question = ''
DELIMITER = "|"
file = open("test.txt", "r")
score = int(file.read())
file.close()

#Removes empty lines from the database file
def remove_empty_lines():
  try:
    global file
    with open(file, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for line in lines if line.strip())
        f.truncate()
  except IOError:
     print(" \033[1;31m File not accessible")
  except FileNotFoundError:
     print(" \033[1;31m File does not exist")

#Ask function that rejects invalid input
def ask(question, validList):
  while True:
    answer = input(question)
    if answer in validList:
      break
    else:
      print(" \033[1;31m Sorry, invalid answer, please select from the following")
      print(validList)  
  return answer

#Add function that adds 1 to the database file each time the game is won
def add():
  global record
  global score
  score += 1
  file = open("test.txt", "w")
  file.write(str(score))
  file.close()

#Functions used to clear the screen for each new game
def clear_console_long():
  sleep (3)
  os.system('clear') 
def clear_console_instant():
  sleep (0.2)
  os.system('clear')

#Parameters for the game and the words that will be randomly selected every game
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["friends", "journey", "dialect", "healthy", "quickly", "jumping", "quality", "amplify"]
    rand = random.randint(0, len(words_to_guess))
    word = words_to_guess[rand]
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

#The actual hangman game  
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    global score
    limit = 7
    #Shows the empty spaces and asks the user for a guess
    guess = input("The word is: " + display + " Enter your guess: \n")
    guess = guess.strip()
    #Rejects invalid input
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    #Displays letter if it is in the word
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    #Rejects the letter if it has already been guessed correctly
    elif guess in already_guessed:
        print("Try another letter.\n")
      
    #Draws the gallow
    else:
        count += 1
        if count == 1:
          turtle.home()
          turtle.pendown()
          turtle.left(90)
          turtle.forward(175)
          turtle.left(90)
          turtle.forward(74)
          turtle.left(90)
          turtle.forward(35)
          turtle.penup()
          turtle.goto(-135,-35)
          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        #Draws the head  
        elif count == 2:
          turtle.goto(-74, 140)
          turtle.pendown()
          turtle.right(90)
          turtle.circle(15,None,25)
          turtle.penup()
          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        #Draws the body
        elif count == 3:
          turtle.goto(-74, 140)
          turtle.pendown()
          turtle.left(90)
          turtle.penup()
          turtle.forward(30)
          turtle.pendown()
          turtle.forward(40)
          turtle.right(180)
          turtle.forward(30)
          turtle.penup()
          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        #Draws the right arm
        elif count == 4:
          turtle.speed(10)
          turtle.goto(-74, 100)
          turtle.pendown()
          turtle.left(55)
          turtle.forward(45)
          turtle.right(180)
          turtle.forward(45)
          turtle.penup()
          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        #Draws the left arm
        elif count == 5:
          turtle.goto(-74, 100)
          turtle.pendown()
          turtle.left(70)
          turtle.forward(45)
          turtle.right(180)
          turtle.forward(45)
          turtle.penup()
          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        #Draws the right leg
        elif count == 6:
          turtle.goto(-74, 100)
          turtle.pendown()
          turtle.left(55)
          turtle.forward(30)
          turtle.right(30)
          turtle.forward(60)
          turtle.right(180)
          turtle.forward(60)
          turtle.penup()
          print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        #Draws the left leg
        elif count == 7:
          turtle.goto(-74, 70)
          turtle.pendown()
          turtle.right(120)
          turtle.forward(60)
          turtle.penup()
          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
          print(" \033[1;31m Wrong guess. Game over!\n")
          clear_console_long()
          turtle.clear()
          True 
    #If all of the correct letters are guessed     
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        clear_console_long()
        turtle.clear()
        add()
    #If the maximum amount of wrong guesses isn't reached then the game continues 
    elif count != limit:
        hangman()

#Main program loop
while True:
  TextDelay.delay_print("\033[1;34m Welcome to Hangman")
  print("")
  #Asks the user what they would like to do and runs the matching feature
  question = ask("\033[1;34m What would you like to do (1: Play, 2: Display Score, 3: Exit)? ", ['1','2','3'])
  #Runs hangman
  if question == '1':
    main()
    hangman()  
  #Displays the total community score (every win by every user added up)
  elif question == '2':
    TextDelay.delay_print_fast(" Total Community Score: " + str(score))
    print("")
  #Exits the program 
  elif question == '3':
    TextDelay.delay_print_fast(" \033[1;32m Thanks for using!")
    break 
  