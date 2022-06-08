import random

myOption = ["R", "P", "S"]

p1Choice = random.choice(myOption)
p2Choice = input ("Enter your choice...")
print ("Computer " + "(" + p1Choice + ")" , ": ", "You " + "(" + p2Choice + ")")

while p1Choice == p2Choice:
    print ("Tie... Replay!!!")
    p1Choice = random.choice(myOption)
    p2Choice = input ("Enter your choice...")
    print ("Computer " + "(" + p1Choice + ")" , ": ", "You " + "(" + p2Choice + ")")
    continue
if p1Choice == "R" and p2Choice == "S": print ("Computer wins!!!")
elif p2Choice == "R" and p1Choice == "S": print ("You win!!!")
elif p1Choice == "P" and p2Choice == "R": print("Computer wins!!!")
elif p2Choice == "P" and p1Choice == "R": print ("You win!!!")
elif p1Choice == "S" and p2Choice == "P": print("Computer wins!!!")
elif p2Choice == "S" and p1Choice == "P": print ("You win!!!")
elif p2Choice or p1Choice not in myOption: print ("Not valid... Game Over!!!")
