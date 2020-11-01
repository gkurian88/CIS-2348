#Githin Kurian
#1580561

class Team:
    def __init__(self):
        self.tmnm = 'none'
        self.tmwn = 0
        self.team_losses = 0

    def set_tmnm(self, team_name):
        self.tmnm = team_name

    def set_team_wins(self, team_wins):
        self.team_wins = team_wins

    def set_team_losses(self, team_losses):
        self.team_losses = team_losses

    def get_win_percentage(self):
        percent = self.team_wins / (self.team_wins + self.team_losses)
        return percent


if __name__ == "__main__":
    
    team = Team()
   
    tmnm = input()
    team_wins = int(input())
    team_losses = int(input())
    
    team.tmnm= tmnm
    team.team_wins = team_wins
    team.team_losses = team_losses
    
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.tmnm,'has a winning average!')
    else:
        print('Team', team.tmnm, 'has a losing average.')
