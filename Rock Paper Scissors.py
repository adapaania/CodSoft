print("Let's play Rock, Paper, Scissors!!!")
print()

possible_moves=['rock','paper','scissors']

player=0
computer=0
def point():
    global player, computer

    if move==random_move:
        print("Same move! Tie!!")
        print()
    elif (move=="paper" and random_move=="rock") or (move=="rock" and random_move=="scissors") or (move=="scissors" and random_move=="paper"):
        player+=1
        print("You get a point!!")
        print()
    elif (random_move=="paper" and move=="rock") or (random_move=="rock" and move=="scissors") or (random_move=="scissors" and move=="paper"):
        computer+=1
        print("Oh noo.. Computer gets a point!!")
        print()

    return player,computer

def score():
    import pandas as pd
    print()
    data={"Participants":["Player","Computer"],
          "Points":[player,computer]
          }
    print(pd.DataFrame(data))

def dontinue():
    while True:
        inp=str(input("Do you want to continue playing?(y/n): "))
        if inp=='y':
            score()
            print()
            game()
            
        elif inp=='n':
            score()
            if player>computer:
                print("You Win!!!")
            elif player==computer:
                print("That's a tie!!")
            else:
                print("You Lost!! Better Luck Next Time =)")
                break
            break
        else: print("Enter a Valid Input.")
        
def computer_moves():
    global random_move
    import random
    random_move = random.choice(possible_moves)
    return random_move

def game():
    global move
    for i in range(5):
            move=str(input("Enter your move:(rock/paper/scissors): "))
            print()
            print("Your move: ",move)
            computer_moves()
            print("Computer's move: ",random_move)
            print()
            point()
    dontinue()
        
    


    


    
game()   
        
    
    
    
