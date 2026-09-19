# Name: Rebekah Kinghorn
# 

def clear():
    import os
    os.system('cls')


import random
clear()

#initialize things
won_list = []
lost_list = []
win_dict = {
    "Won Against" : won_list,
    "Lost Against" : lost_list
}
wins = 0
losses = 0

#enter home team
home_team = input("Enter the name of your home team: ")

#enter # of games they will play
num_games = int(input(f"Enter the number of games that {home_team} will play: "))

#for each game...
#enter away team
for game in range(1,num_games+1):
    away_team = input(f"Enter the name of the away team for game {game}: ")

    #randomly generate scores for both teams
    #random.seed(2)
    home_score = random.randint(0,3)
    away_score = random.randint(0,3)
    
    #no ties
    while home_score == away_score:
        away_score = random.randint(0,3)
    
    #keep track of wins and losses in dict and counter
    if home_score > away_score:
        won_list.append(away_team)
        win_dict["Won Against"] = won_list
        wins += 1
    
    if home_score < away_score:
        lost_list.append(away_team)
        win_dict["Lost Against"] = lost_list
        losses += 1
        
    #print home and away teams' scores
    print(f"{home_team}'s score: {home_score} - {away_team}'s score: {away_score}")



"""to debug"""
# print(win_dict)
# print(won_list)
# print(lost_list)
# print(wins)
# print(losses)


#printing stuff
#teams won against and lost against
    #win_or_lose is the variable-ish name I created as the looper variable
    #the_lists is the looper variable but for the values in the lists in the dictionary
for win_or_lose, the_lists in win_dict.items():
    #this first time, this will print the teams we won against (first item in the dictionary!)
    print(f"Teams {win_or_lose}")
    #print(win_or_lose)
    #^this prints "Won Against" and "Lost Against" from the dictionary

    for the_list in the_lists:
        #this will print the values associated with the current key
        print(f"\t{the_list}")
    # print(f"Teams won against:\n{win_dict.values()}")
    # print(f"Teams wons against:\n\t{won_list(team_num)}")


#final season record
print(f"Final season record: {wins} - {losses}")


#how did we do?
if wins >= .75*(wins+losses):
    print("Qualified for the NCAA Soccer Tournament")
elif wins >= .5*(wins+losses):
    print("You had a good season.")
else:
    print("Your team needs to practice!")
