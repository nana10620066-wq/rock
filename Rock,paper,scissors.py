import random
import os

print("Welcome to the Game!!!!!")

ch1=["Rock","Paper","Scissors"]

game_user=input("Choose Rock,Paper,Scissors :")

admin=random.choice(ch1)

x=type(game_user)

print("Your's choice ::",game_user)
print("Admin's choice ::",admin)
print("Type of user data ::",x)

if game_user=="Paper":
    
    if admin=="Paper":
        print("Draw Again!!")
    elif admin=="Rock":
        print("You Win!!")
    else:
        print("You Lose!!")   
        
elif game_user=="Rock":
    
  if admin=="Scissors":
      print("You Win!!")
  elif admin=="Paper":
      print("You Lose!!")
  else:
      print("Draw Again!!")
        
elif game_user=="Paper":
    
    if admin=="Scissors":
        print("You Lose!!")
    elif admin=="Paper":
        print("Draw Again!!")
    else:
        print("You Win!!")
        
else:
    print("Invalid!!!!!")
    
folder_path=r"D:/netw nn"
file_path=os.path.join(folder_path,"Rock,paper,scissors.py")
print("Save to :",folder_path)
