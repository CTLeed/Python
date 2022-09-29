players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
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
    team_list = []

    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age = dictionary["age"]
        self.position = dictionary["position"]
        self.team = dictionary["team"]
        Player.team_list.append(self)

    @classmethod
    def get_team(cls, team_list):
        player_list = []
        for player in team_list:
            player_object = cls(player)
            player_list.append(player_object)
        return player_list


kevin = Player(players[0])
jason = Player(players[1])
kyrie = Player(players[2])

print(kevin.position, jason.age, kyrie.team)


def player_list_builder(list):
    player_list = []
    for player in list:
        player_name = Player(player)
        player_list.append(player_name)
    return player_list


new_list = player_list_builder(players)

print(new_list[0].name)

new_list2 = Player.get_team(players)

print(new_list2[4].team)
