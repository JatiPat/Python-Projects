import random # Importing random function for choosing Computer choice
player_options = ['rock', 'paper', 'scissors'] #list of options for player and computer
Com_options = ['rock', 'paper', 'scissors']
Com = player_options[random.randint(0,2)] #Choose an index option between 0,1, and 2

print("Rock, Paper, Scissors. What do you Choose?")

while True: #infinite loop if the player puts in a wrong choice
  Player = input().lower() #taking in player input and lowercasing just in case
  if Player in player_options: #if the player puts in the correct input, print out the outcome
    print("Player chose " + Player + " and computer chose " + Com + ".")
    break
  else:
    print("Invalid input. Try again!")


def winstate(play,comp): #win state function
  if play == comp: #3-in-one tie option
    print("It's a Tie!") 
    
  elif play == "rock": #Player chose rock and computer didn't choose rock
    if comp == "paper": #Computer chose paper, so they win! else only other option is scissors, so you win!
      print("You lose!")
    else:
      print("You win!")
      
  elif play == "paper": #Repeat but for paper
    if comp == "scissors":
      print("You lose!")
    else:
      print("You win!")
      
  elif play == "scissors": #Repeat but for scissors
    if comp == "rock":
      print("You lose!")
    else:
      print("You win!")


winstate(Player,Com) #call winstate function with player input and comupter's choice
    
