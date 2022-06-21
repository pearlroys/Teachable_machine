import random
from enum import IntEnum

# insted of using string inputs the enumerat eallows us to iterate through a sequence 
# but it keeps track of both the index and the element
score = 0
class items(IntEnum):
    Rock =  0
    Paper = 1
    Scissors = 2

#to get the computer choice
def get_computer_choice():
    choice = random.randint(0, len(items) - 1)
    choice_item = items(choice)
    return choice_item

# to get the users choice
def get_user_choice():
    user_choices = int(input("Pick an item: Rock[0], Paper[1], Scissors[2]: "))
    choice_item = items(user_choices)
    return choice_item
#methdo to choice the winner, note this function was changed a bit in the camera version
#  because nested if statments could prove a difficult sometimess
def get_winner(computer_choice, user_choice):
    global score
 
    if computer_choice == user_choice:
        print("It's a tie!")
    elif user_choice == items.Rock:
        if computer_choice == items.Scissors:
            score += 1
            print("Rock eviscerates Scissors, You win!")
        else:
            print("Paper snuffs rock, you Lose!")
    elif user_choice == items.Paper:
        if computer_choice == items.Rock:
            score += 1
            print("Paper snuffs rock, you Win!")
        else:
            print("Scissors shreds Paper, you Lose!")
    elif user_choice == items.Scissors:
        if computer_choice == items.Paper:
            score += 1
            print("Scissors shreds Paper, you Win!")
        else:
            print("Rock destroys Scissors, you Lose")
        #return score 
        
        
       
#funtion logic                  
def play():
    while 1 and score != 3:
        try:
            user_choice = get_user_choice()
        except ValueError as e:
            allowed_items = range(0, len(items) - 1)
            print(f"Invalid entry, enter a value from: {allowed_items}")
            continue
        computer_choice = get_computer_choice()
        get_winner(computer_choice, user_choice)
    
        

#calling main

if __name__ == "__main__":
    play()     

        
