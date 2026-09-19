# Rebekah Kinghorn 
# This is a program that lets you enter soccer teams and then play them against each other. You can view team stats and game stats. It includes inheritance and exception handling.

#Rebekah Kinghorn
#Advanced OOP - Soccer Teams assignment


import random
from datetime import date, timedelta

# random.seed(3)


#define class SoccerTeam
class SoccerTeam():
    def __init__(self, team_number:int, team_name:str) -> None:
        self.team_number = team_number
        self.team_name = team_name
        self.__wins = 0
        self.__losses = 0
        self.goals_scored = 0
        self.goals_allowed = 0
        
    def get_record_percentage(self):
        self.total_games_played = self.__wins + self.__losses
        try:
            season_record = round((self.__wins / self.total_games_played), 2)
            # rounded_season_record = season_record*100
            # rounded_season_record = round(rounded_season_record,2)
            return season_record
        except ZeroDivisionError:
            return 0
        
    def get_team_info(self):
        return f"Team Name: {self.team_name}\nSeason record: {self.__wins} - {self.__losses} ({int(round(self.get_record_percentage()*100,0))}%)\nTotal goals scored: {self.goals_scored} - Total goals allowed: {self.goals_allowed}"
        #returns info on the team and their performance.
    
    def generate_score(self):
        score = random.randint(0,3)
        return score
    
    def get_season_message(self):
        if self.get_record_percentage()*100 >= 75:
            return "Qualified for the NCAA Soccer Tournament!"
        elif self.get_record_percentage()*100 >= 50:
            return "You had a good season."
        else:
            return "Your team needs to practice!"
        #returns a message based on the team’s win rate.
    
    def record_win(self):
        self.__wins += 1

    def record_loss(self):
        self.__losses += 1


#define class SponsoredTeam that inherits from SoccerTeam
class SponsoredTeam(SoccerTeam):
    def __init__(self, team_number: int, team_name: str, sponsor_name:str):
        self.sponsor_name = sponsor_name
        super().__init__(team_number, team_name)
    
    def generate_score(self):
        score = random.randint(1,3)
        return score

    def get_season_message(self):
        if self.get_record_percentage()*100 >= 75:
            sponsor_message = f" {self.sponsor_name} is very happy."
        elif self.get_record_percentage()*100 >= 50:
            sponsor_message = f" {self.sponsor_name} hopes you can do better."
        else:
            sponsor_message = f" You are in danger of {self.sponsor_name} dropping you."
        return super().get_season_message() + sponsor_message
    

#define class Game
class Game():
    def __init__(self, game_number, home_team, away_team) -> None:
        self.game_number = game_number
        self.game_date = date.today() + timedelta(1)
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_score = 0
        self.away_team_score = 0

    def get_game_status(self):
        return f"\nResults of game {game.game_number} on {game.game_date}: Home team {game.home_team.team_name} scored {game.home_team.goals_scored} - Away team {game.away_team.team_name} scored {game.away_team.goals_scored}.\n"
    
    def record_home_win(self):
        self.home_team.record_win()

    def record_home_loss(self):
        self.home_team.record_loss()

    def record_away_win(self):
        self.away_team.record_win()

    def record_away_loss(self):
        self.away_team.record_loss()
    
    def play_game(self):
        #this will automatically go to either a normal team or a sponsored team :D
        home_score = self.home_team.generate_score()
        away_score = self.away_team.generate_score()

        while home_score == away_score:
            away_score = self.away_team.generate_score()
        
        self.home_team_score = home_score
        self.away_team_score = away_score

        self.home_team.goals_scored = home_score
        self.away_team.goals_scored = away_score

        self.home_team.goals_allowed = away_score
        self.away_team.goals_allowed = home_score

        if home_score > away_score:
            self.record_home_win()
            self.record_away_loss()
        else:
            self.record_away_win()
            self.record_home_loss()

        print(self.get_game_status())
    







#gather how many teams there are. includes exception handling
enter_teams_true = True
while enter_teams_true:
    try:
        num_teams = int(input("Enter the number of soccer teams you want to enter (at least 2): ").strip())
        if num_teams < 2:
            raise Exception
        #this is the only way to exit the loop
        enter_teams_true = False

    except ValueError:
        print("Invalid integer! Try again.")

    except Exception as e:
        # print(f"{type(e).__name__}. You must enter an integer of 2 or above. Try again.")
        print("You must enter an integer of 2 or above. Try again.")



#this will have all of the the soccer team objects in it
list_of_teams = []


#make soccer team objects
team_name_counter = 1
while team_name_counter < num_teams +1:
    team_name_input = input(f"Enter a name for team {team_name_counter}: ")
    if_sponsored = input(f"Enter Y if team {team_name_counter} is sponsored, otherwise enter N (or anything else): ").strip().upper()
    if if_sponsored == "Y":
        sponsor_name_input = input("Enter the name of your sponsor: ")
        list_of_teams.append(SponsoredTeam(team_name_counter, team_name_input, sponsor_name_input))
    else:
        list_of_teams.append(SoccerTeam(team_name_counter, team_name_input))
    team_name_counter +=1




#do this entire thing until they end the soccer season
hit_exit = False
game_counter = 1
list_of_games = []
while hit_exit == False:

    #choose home and away teams
    choosing_home_team = True
    choosing_away_team = True
    while (choosing_home_team == True or choosing_away_team == True) :
        #print out list of teams
        for i,team in enumerate(list_of_teams):
            print(f"{i+1}: {team.team_name}")

        try:
            choose_home_team = input(f"Enter the team number of the HOME team or enter \"exit\" to end the season: ").strip()
            if choose_home_team.lower() == "exit":
                # print("The soccer season is over!")
                break
                
            if (int(choose_home_team) > len(list_of_teams)) or (int(choose_home_team) <= 0):
                print("Invalid team number! Try again.") 
                continue
            else:
                choosing_home_team = False

            choose_away_team = input(f"Enter the team number of the AWAY team or enter \"exit\" to end the season: ").strip()
            if choose_away_team.lower() == "exit":
                # print("The soccer season is over!")
                break

            if (int(choose_away_team) > len(list_of_teams)) or (int(choose_away_team) <= 0):
                print("Invalid team number! Try again.")
                continue
            elif (choose_away_team == choose_home_team):
                print("You can't choose the same team as the home and away team! Try again.")
                continue
            else:
                choosing_away_team = False
        
        except:
            print("Invalid team number! Try again.")
    
    
    #this will exit the loop again so it doesn't try to make another game. best way? idk
    if choose_home_team.lower() == "exit":
        print("\nThe soccer season is over!")
        break
    
    #make game from the two teams we just chose (put in the whole team object)
    game = Game(game_counter, list_of_teams[int(choose_home_team)-1], list_of_teams[int(choose_away_team)-1],)
    game.game_date = date.today() + timedelta(game_counter)

    game.play_game()

    game_counter += 1
    list_of_games.append(game)

    # print("made and added a game! this is just a comment")
    # print(f"home score: {game.home_team_score} \naway score: {game.away_team_score}")





#continue this loop until they exit the program
post_season_go = True
while post_season_go:
    #print postseason menu
    print("Postseason Menu:")
    print("1: Go to Team Info Menu")
    print("2: Go to Game Info Menu")
    print("exit: End the program")
    post_season_choice = input("\nEnter an option: ").strip()
    
    try:
        #check if it's "exit"
        if post_season_choice.lower().strip() == "exit":
            print("Exiting the program.")
            post_season_go = False
            break
        #if they entered a number but it's not 1 or 2 (this won't work if they didn't enter a number, and we already confirmed it's not "exit")
        elif (int(post_season_choice) > 2) or (int(post_season_choice) <= 0):
            print("Invalid choice! Try again.")
            print(int(post_season_choice))
            continue
    except:
        print("Invalid choice! Try again.")
        continue
    

    #we only got to this point if they entered 1 or 2, so we can make their choice an integer 
    post_season_choice = int(post_season_choice)
    

    #if they entered 1, go to the Team Info Menu
    team_info_choice = ""
    if post_season_choice == 1:
        
        team_info_get_int = True
        while team_info_get_int:
            print("\nTeam Info Menu:")
            for i,team in enumerate(list_of_teams):
                print(f"{i+1}: {team.team_name}")
            
            team_info_choice = input("Enter a team number to see their info, or enter \"exit\" to go back to the Postseason Menu: ").strip().lower()
        
            if team_info_choice == "exit":
                #exit back up to the postseason menu
                team_info_get_int = False
                continue
            try:
                if (int(team_info_choice) > len(list_of_teams)) or (int(team_info_choice) <= 0):
                    print("Invalid team number! Try again.")
                else:
                    team_info_choice = int(team_info_choice)
                    print(list_of_teams[team_info_choice-1].get_team_info())
                    print(list_of_teams[team_info_choice-1].get_season_message())
                    continue
            except:
                print("Invalid team number! Try again.")
        
            # team_info_go = True
            # while team_info_go:
            #     pass
    
    if team_info_choice == "exit":
        continue



    #if they entered 2, go to the Game Info Menu
    game_info_choice = ""
    if post_season_choice == 2:
        
        game_info_get_int = True
        while game_info_get_int:
            print("\nGame Info Menu:")
            for j,individual_game in enumerate(list_of_games):
                print(f"Game {j+1}")
            
            game_info_choice = input("Enter a game number to see its info, or enter \"exit\" to go back to the Postseason Menu:").strip().lower()
        
            if game_info_choice == "exit":
                #exit back up to the postseason menu
                game_info_get_int = False
                continue
            try:
                if (int(game_info_choice) > len(list_of_games)) or (int(game_info_choice) <= 0):
                    print("Invalid game number! Try again.")
                else:
                    game_info_choice = int(game_info_choice)
                    print(list_of_games[game_info_choice-1].get_game_status())
                    continue
            except:
                print("Invalid game number! Try again.")

    if game_info_choice == "exit":
        continue


"""finish get team info to add goals allowed and such """



    

