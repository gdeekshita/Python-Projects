'''
    observing Tottenham's season
'''

FILENAME = "hotspurs.txt"

def main ():
    min_wins = 50 
    min_season = ""
    most_goals = 10
    most_season = ""
    
    with open(FILENAME, "r") as infile:
        while True:
            wins = 0 
            loses = 0 
            draws = 0 
            one_goal = 0 
            first_ten = 0
            last_ten = 0
            total_goals = 0
            
            goals = infile.readline()
            records = infile.readline()
            if goals == "":
                break
            
            #make strings into lists
            goals = goals.split()
            records = records.split()

            #identify the season
            season = goals[0]
            
            #retrieve only the records 
            records = records[1:]
            
            #convert goals into floats
            goals = [int(goals) for goals in goals[1:]]
            
            #computations for calculating number 
            #of total matches and wins/loses/draws
            total_matches = len(goals)
            for i in range(len(records)):
                if records[i] == "W":
                    wins += 1
                elif records[i] == "L":
                    loses += 1
                else:
                    draws += 1
            
            #computations for wins with only one goal 
            for i in range(len(records)):
                if records[i] == "W" and goals[i] == 1:
                    one_goal += 1
            
            #computations for total goals in first and last 10 games
            first_ten = sum(goals[0:11])
            last_ten = sum(goals[28:])
            
            #problem 3: season with fewest wins 
            if wins < min_wins:
                min_wins = wins
                min_season = season
            
            #problem 3: season with most goals 
            total_goals = sum(goals[0:])
            if total_goals > most_goals:
                most_goals = total_goals
                most_season = season
            
            #display to user each season and analysis
            print("During the", season, "season:")
            print("Tottenham played a total of", total_matches, "matches.")
            print("Wins:", wins)
            print("Loses:", loses)
            print("Draws:", draws)
            print("They won", one_goal, "matche(s) despite scoring only one goal.")
            print("Total goals scored in first 10 games: ", first_ten)
            print("Total goals scored in last 10 games: ", last_ten)
            print()
        print("Season with the fewest wins:", min_season)
        print("Season with the most goals: ", most_season)
                        
main()