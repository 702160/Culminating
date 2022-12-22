#Drew Johnston
#January 20th, 2023
#Culminating Project Hangman
#Show the knowledge I have gained over the course of this class

import time
import TextDelay 
import os
from time import sleep
import random
import turtle
global score 
global high_score 

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("Score: 0 High Score: 0", align="center", font=("times new roman", 20, "normal"))

#Intro to the hangman game and instuctions
print(" ")
remember = TextDelay.delay_print("Welcome to Hangman")
print(" ")
time.sleep(2)

def clear_console_long():
  sleep (3)
  os.system('clear')
  
def clear_console_instant():
  sleep (0.2)
  os.system('clear')

# The parameters we require to execute the game:
  
def ask(question, validList):
  while True:
    answer = input(question)
    if answer in validList:
      break
    else:
      print(" \033[1;31m Sorry, invalid answer, please select from the following")
      print(validList)  
  return answer
  
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

# Initializing all the conditions required for the game:
  
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    global score
    limit = 7
    guess = input("The word is: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

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
          
        elif count == 2:
          turtle.goto(-74, 140)
          turtle.pendown()
          turtle.right(90)
          turtle.circle(15,None,25)
          turtle.penup()
          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

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

        elif count == 5:
          turtle.goto(-74, 100)
          turtle.pendown()
          turtle.left(70)
          turtle.forward(45)
          turtle.right(180)
          turtle.forward(45)
          turtle.penup()
          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

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

        elif count == 7:
          turtle.goto(-74, 70)
          turtle.pendown()
          turtle.right(120)
          turtle.forward(60)
          turtle.penup()
          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
          print("Wrong guess. Game over!\n")
          clear_console_long()
          turtle.clear()
          True 
          
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        clear_console_long()
        turtle.clear()
        
    elif count != limit:
        hangman()
  
while True:
  question = ask("\033[1;35m Would you like to play hangman?(y/n)? ", ['y','yes','Yes','n','no','No'])
  if question in ['y','yes','Yes']:
    main ()
    hangman()
  elif question in ['n','no','No']:
    print("Thanks for playing!")
    break
    