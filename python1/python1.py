''' The game by python'''

import random

raint = random.randint(1 , 10)

counts = 5

while counts > 0:
    export = input("Guess the number of procedures performed:")
    answer = int(export)
    
    if answer == raint:
        print("Yes , you're right!")
        break
    else:
        if answer > raint:
            print("No , wrong answer!")
            print("Big")
        if answer < raint:
            print("No , wrong answer")
            print("Small")

        counts = counts - 1

print("Game over!")
