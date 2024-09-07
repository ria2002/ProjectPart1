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
*******************************************************************************
''')
print("Welcome to the Treasure Island\nYour mission to find the treasure")
choice1 = input('You\'re a cross road, where do you want go?, Type "left" or "right"').lower()

if choice1== "left":
     choice2 = input("You have come to a lake. type 'wait' or 'swim'").lower()
     if choice2 == "wait":
         choice3 = input("You have arrived at island unharmed. There are three doors. Which one do you want to chose 'red' , 'yellow' and 'blue'").lower()

         if choice3 == "red":
            print("It is a room full of fire. Game is over!")

         elif choice3 == "yellow":
            print("You enter a room of beasts. Game is over!")

         elif choice3 == "blue":
            print(" You have found the Treasure. You win!")


     else:
        print("you have attacked by angry trout. Game is over!")

else:
 print("You fall in a hole.Game is over!")





