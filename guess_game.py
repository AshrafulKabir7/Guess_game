import random
#============================================================================================================================
# The below function is a game where computer will choose a number between your given range and you have to guess that number.
def computer_choose_you_guess(range):
    computer_choose=random.randint(1,range)
    user_guess=0
    attempts=0
    while user_guess!=computer_choose:
        user_guess=int(input(f"provide a number between 1 and {range}= "))
        if user_guess>computer_choose and user_guess<=range:
            print("You have guessed a high value. Try to choose a lower value")
        elif user_guess<computer_choose:
            print("You have guessed a lower value. Try to choose a high value")
        elif user_guess>range:
            print(f"You have choosen a value greater than you given range {range}. Try to choose within the range")
        attempts=attempts+1
    print(f"congratulation!! you have guessed the number {user_guess}. you took exactly {attempts} attemps to guess the number")
#============================================================================================================================

#============================================================================================================================
#The below function is a game where you will choose a number between your given range and computer have to guess that number.
def you_choose_computer_guess(range):
    low=1
    high=range
    feedback=""
    attemps=0
    while feedback!="c":
        computer_guess=random.randint(low,high)
        print(f"The computer gussed= {computer_guess}")
        feedback=str(input("enter c if computer guess is correct or enter l if computer guess is a low number otherwise enter h if computer chooses a higher value= ")) 
        if feedback=="l":
            low=computer_guess+1
        else:
            high=computer_guess-1
        attemps=attemps+1
    print(f"Congratulation to you Computer. You have guessed the number {computer_guess} and you took exactly {attemps} attemps to guess the number.")
#============================================================================================================================

#choose you want to guess or you want computer to guess the number.
Choose_game=str(input("write you or computer= "))
if Choose_game=="you":
    range=int(input("First, provide a number range sothat computer can choose a number from that range= "))
    computer_choose_you_guess(range)
else:
    range=int(input("First, provide a number range sothat computer can guess a number from that range= "))
    you_choose_computer_guess(range)
     




        