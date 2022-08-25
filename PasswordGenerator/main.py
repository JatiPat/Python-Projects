import string
import random

charOptions = list(string.ascii_letters + string.digits + "!@#$%^&*-_=+,/") ## all possible character options for the password (all letters + all digits + unique characters)

def make_password(length): ## make password function
  password = [] ##empty list 
  for i in range(length): ## given how many character from the input
    password.append(random.choice(charOptions)) ## add that amount of characters in the list
    
  random.shuffle(password) ## shuffle the list so it's not just AAA111!!!
  password = "".join(password) ## join all the elements into one string and print
  print (password)


while True: ## while loop to make more passwords
  make_password(int(input("Length of the Password: "))) ##taking in the input, converting it into a interger, and passing it into the make_password function
  if input("Want another? (Yes/No) \n").lower() != "yes": ##if they don't say yes, end the program (.lower makes it lowercase to compare)
    
    break
  print('\n')
