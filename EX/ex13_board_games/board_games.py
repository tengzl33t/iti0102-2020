"""See, mida tester tahab."""


class Statistics:
    """Class statistics."""

    def __init__(self, filename):
        """Midagi väga huvitav (ei)."""
        self.filename = filename

    def read_file(self):
        """Midagi väga huvitav (ei)."""
        res_list = []
        with open(self.filename, encoding="utf-8") as file:
            for line in file:
                res_list.append(line.strip())

        return res_list

    def get_set_games(self):
        """Midagi väga huvitav (ei)."""
        games_list = []
        for line in self.read_file():
            splitter = line.split(";")
            game_name = splitter[0]
            game_type = splitter[2]
            players = splitter[1].split(",")
            score = splitter[3].split(",")

            if game_type == "points":
                # convert str points into ints, for right sorting
                # sorting 2 lists together for replacing point to players by right order
                for i, v in enumerate(score):
                    score[i] = int(v)

                # print(score)
                # print(players)
                zipped = zip(score, players)
                # for i in zipped:
                #    print(i)
                # sc, pl = map(list, zip(*sorted(zip(score, players), reverse=True)))
                srt = sorted(zipped, key=lambda x: (-x[0]))
                # print(srt)
                # print(srt)

                score = [i[1] for i in srt]

            g = Game(game_name, game_type, score, players)
            games_list.append(g)

        return games_list

    def get_players_dict(self):
        """Midagi väga huvitav (ei)."""
        players_dict = {}
        for line in self.read_file():
            splitter = line.split(";")
            players = splitter[1].split(",")

            for p in players:
                players_dict[p] = Player(p)

        return players_dict

    def crp_extras(self, games):
        """Midagi väga huvitav (ei)."""
        for g in games:
            for p in g.players:
                p.add_game(g)  # add games to player

                # add losses and wins to player
                if g.type != "winner":
                    if p in g.results[1:]:
                        p.add_lose(g)
                    elif p == g.results[0]:
                        p.add_win(g)
                else:
                    if p != g.results[0]:
                        p.add_lose(g)
                    else:
                        p.add_win(g)

    def compare_replace_players(self):
        """Midagi väga huvitav (ei)."""
        players = self.get_players_dict()
        games = self.get_set_games()
        # replacing str players into player classses
        for i in games:
            # for players of the game
            pl_list = i.players
            for ip, p in enumerate(pl_list):
                for k, v in players.items():
                    if p == k:
                        pl_list[ip] = v

            # for "points" of the game
            pnts_list = i.results
            for ip, p in enumerate(pnts_list):
                for k, v in players.items():
                    if p == k:
                        pnts_list[ip] = v

        self.crp_extras(games)

        return games, players  # return games and players

    # ======================= GET Part ===============================

    def get_games(self, x):  # get names of games (/games)
        """Midagi väga huvitav (ei)."""
        names = list(set([i.name for i in self.get_set_games()]))
        return names

    def get_players(self, x):  # get names of players (/players)
        """Midagi väga huvitav (ei)."""
        names = [i for i in self.get_players_dict().keys()]
        return names

    def get_total(self, x):  # (/total)
        """Midagi väga huvitav (ei)."""
        if not x:  # if not /total/result-type
            return len([i.name for i in self.get_set_games()])
        else:
            counter = 0
            for i in self.get_set_games():
                result_type = i.type
                if result_type == x[0]:
                    counter += 1
            return counter

    def get(self, path):
        """Midagi väga huvitav (ei)."""
        tokens = path[1:].split("/")
        func = getattr(self, "get_" + tokens[0])  # take first part of message and add next parts
        return func(tokens[1:])

    # ======================= GET PLAYER Part ===============================

    def p_amount(self, x):
        """Midagi väga huvitav (ei)."""
        counter = 0
        games = [i.players for i in self.compare_replace_players()[0]]
        for i in games:
            for p in i:
                if x == p.name:
                    counter += 1
        return counter

    def p_fav(self, x):
        """Midagi väga huvitav (ei)."""
        games = self.compare_replace_players()[0]
        player_games_list = []
        for g in games:
            for p in g.players:
                if x == p.name:
                    player_games_list.append(g.name)
        most_fav_game = max(player_games_list, key=player_games_list.count)
        return most_fav_game

    def p_won(self, x):
        """Midagi väga huvitav (ei)."""
        counter = 0
        results = [i.results for i in self.compare_replace_players()[0]]
        for i in results:
            if i[0].name == x:
                counter += 1
        return counter

    def get_player(self, x):
        """Midagi väga huvitav (ei)."""
        if x[1] == "amount":
            return self.p_amount(x[0])

        elif x[1] == "favourite":
            return self.p_fav(x[0])

        elif x[1] == "won":
            return self.p_won(x[0])

    # ======================= GET GAME Part ===============================

    def g_amount(self, x):
        """Midagi väga huvitav (ei)."""
        games = [i.name for i in self.get_set_games()]
        counter = 0
        for i in games:
            if x == i:
                counter += 1
        return counter

    def player_amount(self, x):
        """Midagi väga huvitav (ei)."""
        pl_list = []
        for g in self.get_set_games():
            if g.name == x:
                pl_list.append(len(g.players))
        return max(pl_list, key=pl_list.count)

    def most_wins(self, x):
        """Midagi väga huvitav (ei)."""
        winners = []
        for g in self.get_set_games():
            if g.name == x:
                winners.append(g.results[0])
        return max(winners, key=winners.count)

    def most_losses(self, x):
        """Midagi väga huvitav (ei)."""
        losses = []
        for g in self.get_set_games():
            if g.name == x and (g.type == "points" or g.type == "places"):
                losses.append(g.results[-1])
        return max(losses, key=losses.count)

    def record_holder(self, x):
        """Midagi väga huvitav (ei)."""
        for g in self.get_set_games():
            if g.name == x and (g.type == "points"):
                return g.results[0]

    def most_frequent_winner(self, x):
        """Midagi väga huvitav (ei)."""
        list1 = []
        list2 = []
        for p in self.compare_replace_players()[1].values():
            g = [i.name for i in p.games]  # games of player
            w = [i.name for i in p.wins]  # wins of player
            if x in g:
                res = round((w.count(x) / g.count(x)) * 100)
                list1.append(p.name)
                list2.append(res)
        zipped = zip(list2, list1)
        srt = sorted(zipped, reverse=True)
        return srt[0][1]  # take first element (most frequent), take second element (player name)

    def most_frequent_loser(self, x):
        """Midagi väga huvitav (ei)."""
        list1 = []
        list2 = []
        for p in self.compare_replace_players()[1].values():
            g = [i.name for i in p.games if (i.type == "points" or i.type == "places")]  # games of player
            #  l take last places of player
            lose = [i.name for i in p.games if (i.type == "points" or i.type == "places") and i.results[-1] == p]
            if x in g:
                res = round((lose.count(x) / g.count(x)) * 100)
                list1.append(p.name)
                list2.append(res)
        try:  # check for "winner" type games, they cause index error
            zipped = zip(list2, list1)
            srt = sorted(zipped, reverse=True)
            return srt[0][1]
        except IndexError:
            pass

    def get_game(self, x):
        """Midagi väga huvitav (ei)."""
        if x[1] == "amount":
            return self.g_amount(x[0])
        elif x[1] == "player-amount":
            return self.player_amount(x[0])
        elif x[1] == "most-wins":
            return self.most_wins(x[0])
        elif x[1] == "most-losses":
            return self.most_losses(x[0])
        elif x[1] == "record-holder":
            return self.record_holder(x[0])
        elif x[1] == "most-frequent-winner":
            return self.most_frequent_winner(x[0])
        elif x[1] == "most-frequent-loser":
            return self.most_frequent_loser(x[0])


class Player:
    """Player init."""

    def __init__(self, name):
        """Player init."""
        self.name = name
        self.games = []
        self.wins = []
        self.lose = []

    def add_game(self, game):
        """Midagi väga huvitav (ei)."""
        self.games.append(game)

    def add_win(self, game):
        """Midagi väga huvitav (ei)."""
        self.wins.append(game)

    def add_lose(self, game):
        """Midagi väga huvitav (ei)."""
        self.lose.append(game)


class Game:
    """Game init."""

    def __init__(self, name, type, results, players):
        """Game init."""
        self.name = name
        self.type = type
        self.results = results
        self.players = players


#
if __name__ == '__main__':
    statistics = Statistics("andmed.txt")
    # print(statistics.get("/game/game of thrones/amount"))
    # print(statistics.get("/game/terraforming mars/player-amount"))
    # print(statistics.get("/game/game of thrones/most-wins"))
    # print(statistics.get("/game/terraforming mars/most-losses"))
    # print(statistics.get("/game/terraforming mars/record-holder"))
    print(statistics.get("/game/game of thrones/most-frequent-winner"))

# players = [i for i in statistics.compare_replace_players()[1].values()]
# for p in players:
#     print(f"name: {p.name}, games: {[i.name for i in p.games]}, loses: {[i.name for i in p.lose]}, "
#           f"wins: {[i.name for i in p.wins]}")

# test_get_amount_of_players_most_often_played_with_simple
# AssertionError: assert amount_given in player_amounts

# print(statistics.get_games())
# print([i.players for i in statistics.get_games()])
# print([i.results for i in statistics.get_games()])

# print(statistics.get("/player/joosep/amount"))
# print(statistics.get("/player/kristjan/won")) # 0
# print(statistics.get("/player/jaak/won")) # 1
# print(statistics.get("/player/riho/won")) # 1
# print(statistics.get("/player/kristjan/favourite"))

# ready
# print(statistics.get("/games"))
# print(statistics.compare_replace_players())
# print(statistics.get("/total"))
# print(statistics.get("/total/winner"))
