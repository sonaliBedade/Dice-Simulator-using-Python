import random      #library for choosing a random number
print("Welcome to dice simulator!")
user = input("Press y to roll the dice.")  #user input

if user == "y" or user == "Y":    #if user inputs a y
  while user == "y" or user == "Y":   #condition for looping
    theNum = random.randint(1,6)      #selecting a random integer in the range of 1 to 6
    if theNum == 1:
      print("-------------")
      print("|           |")
      print("|     0     |")
      print("|           |")
      print("-------------")
    elif theNum == 2:
      print("-------------")
      print("|           |")
      print("|   0   0   |")
      print("|           |")
      print("-------------")
    elif theNum == 3:
      print("-------------")
      print("|           |")
      print("| 0   0   0 |")
      print("|           |")
      print("-------------")
    elif theNum == 4:
      print("-------------")
      print("|   0    0  |")
      print("|           |")
      print("|   0    0  |")
      print("-------------")
    elif theNum == 5:
      print("-------------")
      print("|   0    0  |")
      print("|      0    |")
      print("|   0    0  |")
      print("-------------")
    else:
      print("-------------")
      print("|   0    0  |")
      print("|   0    0  |")
      print("|   0    0  |")
      print("-------------")
    user = input("Press y to roll again or n to stop")  
if user == "n" or user == "N":  #if user inputs a n
  print("Thankyou.")
