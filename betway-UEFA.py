# Author: Ronald Ekoly

# Title: Betway to R2Millions
print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to BetWay UEFA Champions League. \n")
print("Your mission is to place a winning bet that will give you R2,000,000.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

option1 = input("You're about to place a bet on BetWay. It's the knockout stage of the UEFA Champions League. Type 'rmadrid' or ' barca '").lower()
print()
if option1 == "rmadrid":
    #Place another bet for the quarter final.
    option2 = input("You're bet is won thanks to Real Madrid. Now in the quater final, Real Madrid faces PSG. Who do favor to win on you bet? Type ' rmadrid ' or ' psg'. ").lower()

    if option2 == "rmadrid":
        #Place another bet for the semi-final
        option3 = input("You have four strong teams in the semi-final. Who'd you trust to go all the way to win in the whole thing. Type 'rmadrid', 'bayern', 'mancity' and 'liverpool' ").lower()
        print()
        if option3 == "bayern":
            print("Oops! Sorry, but Bayern Munich had luck in the second leg. They didn't have Lewandoski due to injury. They were out in the semi-final.")
            print()
        elif option3 == "rmadrid":
            print("Congratulations to the Kings of Europe (Real Madrid), they have done it again. You have won a bet of R2,000,000. Hala Madrid.")
            print()
        elif option3 == "mancity":
            print("Fuck this useless team, Manchester City seems to fuck up everytime when it comes to winning the Champions League. How do you lose 1-0 to Real Madrid.")
            print()
        else:
            print("You've lost your mind? you real thought Liverpool would win the cup? LOL they didn't even make it to the final, thanks to Manchester City.")
            print()
    else:
        print("Damn! PSG, I thought they'd win easily. PSG messed up the ticket I should have blocked them. ")
        print()



else:
    print("You lose the bet. Try again next time.")