
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    # def __init__(self, name, age, position, team):
    #     self.name = name
    #     self.age = age
    #     self.position = position
    #     self.team = team

# 1 CHANGE THE CONSTRUCTOR SO THAT IT ACCEPTS ONE DICTIONARY WITH A PLAYER'S INFORMATION INSTEAD
    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']

# 3 MAKE AND POPULATE A LIST OF PLAYER INSTANCES FROM A LIST OF DICTIONARIES
# NINJA BONUS

    @classmethod
    def make_team(cls, team_list):
        my_team = []
        for player in team_list:
            # print(Player(player))
            my_team.append(Player(player))
        print(my_team)

Player.make_team(players)

# 2 CREATE INSTANCES USING INDIVIDUAL PLAYER DICTIONARIES.
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

bball_kevin = Player(kevin)
bball_kevin = Player(jason)
bball_kyrie = Player(kyrie)
print(Player(kevin))
print(Player(jason))
print(Player(kyrie))


