print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island /n Your mission is to find the treasure")
direction = input('You\'re at the cross-road. Where do you want to go? Type "left" or "right"\n')
dir = direction.lower()
if dir == "right":
  print("Fall into a hole, Game Over!")
else:
  next_dec = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat, type "swim" to swim across\n')
  next_decision = next_dec.lower()
  if next_decision == "swim":
    print("Attacked by trout, Game Over")
  else:
    color = input("You arrived at the island unharmed. There is a house of three doors. One red, one yellow and one blue, which color do you choose?\n")
    color = color.lower()
    if color =="yellow":
      print("You Win")
    elif color == "red":
      print("Burned by fire, Game Over!!!!")
    elif color == "blue":
      print("Eaten by beast, game over!!!")
    else:
      print("Game Over!!!")