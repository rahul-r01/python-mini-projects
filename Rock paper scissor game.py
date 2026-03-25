import random 
print("*********ROCK PAPER SCISSOR*********")
print("____________________________________")

def show(user_score,com_score):
    print("______________________")
    print("\nFINAL RESULT: ")
    print(f"YOUR SCORE IS: {user_score}")
    print(f"COMPUTER SCORE IS: {com_score}")
    if user_score==com_score:
        print("\nITS A TIE GAME..!")
    elif user_score>com_score:
        print("\nYOU WON THE GAME..")
    else:
        print("\nYOU LOSE THE GAME..!")
        print("BETTER LUCK NEXT TIME!")
    print("________________________") 
while True:
    rounds=int(input("enter no.of rounds in a game: "))
    print(f"\nTotal {rounds} rounds in a game!")
    game=['Rock','paper','scissor']     
    user_points=0
    computer_points=0
    for i in range(rounds):
        print(f"\nIN ROUND-{i+1}")
        while True:
            try:
               user_choice=int(input("0.ROCK\n1.PAPER\n2.SCISSOR\nENTER YOUR CHOICE: "))
               if user_choice<0 or user_choice>2:
                   print("INVALID CHOICE...Enter only(0/1/2),PLEASE TRY AGAIN!")
               else:
                   break
            except ValueError:
                print("INVALID INPUT..PLEASE ENTER A NUMBER(0/1/2)")
        print(f"\nYOUR CHOICE IS: {game[user_choice]}")
        computer_choice=random.randint(0,2)
        print(f"COMPUTER CHOICE IS: {game[computer_choice]}")
        if user_choice==computer_choice:
            print("\nIt's A TIE ROUND!")
        elif user_choice==0 and computer_choice==2:
            user_points+=1
            print("\nYOU WIN THIS ROUND!")
        elif user_choice==2 and computer_choice==0:
            computer_points+=1
            print("\nCOMPUTER WIN THIS ROUND!")
        elif user_choice>computer_choice:
            user_points+=1
            print("\nYOU WIN THIS ROUND!")
        elif user_choice<computer_choice:
            computer_points+=1
            print("\nCOMPUTER WIN THIS ROUND")
    show(user_points,computer_points)           
    play_again=input("\nDO YOU WANT TO PLAY AGAIN(Y/N): ").lower()
    if play_again!='y':
        print("\nTHANK YOU FOR PLAYING!")
        break