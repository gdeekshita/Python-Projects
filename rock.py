"""
Description: rock/paper/scissors stimulation
    
"""

import random
import matplotlib.pyplot as plt 

def main ():
    game = 0
    Strange_win = 0
    Rachlin_win = 0
    ties = 0 
    
    #randomize Rachlin's first move
    possible_choices = ["rock", "paper", "scissors"]
    Rachlin_before = random.choice(possible_choices)
    
    #randomize what strange's move will be 
    random_num = random.randint(1,10)
    
    #identifying Strange's move based on the randomization
    if random_num == 1:
        Strange_move = str("scissors")
    elif random_num == 2 or random_num == 3:
        Strange_move = str("paper")
    elif random_num == 4 or random_num == 5 or random_num == 6 or random_num == 7 or random_num == 8 or random_num == 9 or random_num == 10:
        Strange_move = str("rock")
    
    #calculating number of ties
    if Rachlin_before == "scissors" and Strange_move == "scissors":
        ties += 1
    elif Rachlin_before == "paper" and Strange_move == "paper":
        ties += 1
    elif Rachlin_before == "rock" and Strange_move == "rock":
        ties += 1
    
    #calculating number of Rachelin wins
    if Rachlin_before == "scissors" and Strange_move == "paper":
        Rachlin_win += 1 
    elif Rachlin_before == "paper" and Strange_move == "rock":
        Rachlin_win += 1
    elif Rachlin_before == "rock" and Strange_move == "scissors":
        Rachlin_win += 1

    #calculating number of Strange wins
    if Strange_move == "scissors" and Rachlin_before == "paper":
        Strange_win += 1 
    elif Strange_move == "paper" and Rachlin_before == "rock":
        Strange_win += 1
    elif Strange_move == "rock" and Rachlin_before == "scissors":
        Strange_win += 1
    game += 1
    while game >= 1:
        #identifying Rachlin's move based on Strange's previous move
        if Strange_move == "scissors":
            Rachlin_move = "rock"
        elif Strange_move == "rock":
            Rachlin_move = "paper"
        elif Strange_move == "paper":
            Rachlin_move = "scissors"
        
        #randomize what strange's move will be 
        random_num = random.randint(1,10)
        
        #identifying Strange's move based on the randomization
        if random_num == 1:
            Strange_move = str("scissors")
        elif random_num == 2 or random_num == 3:
            Strange_move = str("paper")
        elif random_num == 4 or random_num == 5 or random_num == 6 or random_num == 7 or random_num == 8 or random_num == 9 or random_num == 10:
            Strange_move = str("rock")
        
        #calculating number of ties
        if Rachlin_move == "scissors" and Strange_move == "scissors":
            ties += 1
            game += 1
        elif Rachlin_move == "paper" and Strange_move == "paper":
            ties += 1
            game += 1
        elif Rachlin_move == "rock" and Strange_move == "rock":
            ties += 1
            game += 1
        
        #calculating number of Rachelin wins
        if Rachlin_move == "scissors" and Strange_move == "paper":
            Rachlin_win += 1 
            game += 1 
        elif Rachlin_move == "paper" and Strange_move == "rock":
            Rachlin_win += 1
            game += 1
        elif Rachlin_move == "rock" and Strange_move == "scissors":
            Rachlin_win += 1
            game += 1

        #calculating number of Strange wins
        if Strange_move == "scissors" and Rachlin_move == "paper":
            Strange_win += 1 
            game += 1
        elif Strange_move == "paper" and Rachlin_move == "rock":
            Strange_win += 1
            game += 1
        elif Strange_move == "rock" and Rachlin_move == "scissors":
            Strange_win += 1
            game += 1
            
        if Strange_win == 10000 or Rachlin_win == 10000:
            break
    
    print("# of Ties:", ties)
    print("# of wins by Rachlin:", Rachlin_win)
    print("# of wins by Strange:", Strange_win)
    print("If the Rachlin/Strange battle happens, Rachlin is likely to get the coffee.")
    
    #make a bar chart displaying the number of wins and ties from the simulation 
    plt.bar("Ties", ties, color = "blue", label = "Ties")
    plt.bar("Rachlin", Rachlin_win, color = "green", label = "Number of Rachlin Wins")
    plt.bar("Strange", Strange_win, color = "purple", label = "Number of Strange Wins")
    plt.legend ()
    plt.xlabel("People Playing")
    plt.ylabel("Number of Wins") 
    plt.title("Rachlin wins, Strange wins, and ties")

    
main ()    