import random

class planGames():

    A = []
    has_play_with = {}

    def __init__(self, nb_games, nb_teams):
        self.nb_games = nb_games
        self.nb_teams = nb_teams
        self.reset()

    def reset(self):
        self.A = [[(-1, -1) for i in range(self.nb_games)] for j in range(int(self.nb_teams / 2))]
        for i in range(self.nb_teams):
            self.has_play_with[i] = []

    def rand_range(self, n):
        ar = []
        r_ar = []
        for i in range(n):
            ar.append(i)
        for i in range(n):
            r_ar.append(ar.pop(random.randrange(n - i)))
        return r_ar

    def can_add_pair(self, a, b, line, col):
        if a == b:
            return False
        if (a in self.has_play_with[b]):
            return False
        if (b in self.has_play_with[a]):
            return False
        for i in range(line):
            if (a in self.A[i][col] or b in self.A[i][col]):
                return False
        for j in range(col):
            if (a in self.A[line][j] or b in self.A[line][j]):
                return False
        return True

    def add(self, a, b, i, j):
        self.A[i][j] = (a, b)
        self.has_play_with[a].append(b)
        self.has_play_with[b].append(a)
        return (a, b)

    def try_one_time(self):
        for i in range(int(self.nb_teams / 2)):
            for j in range(self.nb_games):
                first_teams = self.rand_range(self.nb_teams)
                second_teams = self.rand_range(self.nb_teams)
                found = False
                ii = 0
                jj = 0
                while ii < len(first_teams) and found == False:
                    while jj < len(second_teams) and found == False:
                        if self.can_add_pair(first_teams[ii], second_teams[jj], i, j):
                            self.add(first_teams[ii], second_teams[jj], i, j)
                            found = True
                        jj = jj + 1
                    jj = 0
                    ii = ii + 1

                if found == False:
                    return False
        return True

    def pprint(self):
        for i in range(int(self.nb_teams / 2)):
            print(self.A[i])

    def generate_n_plans(self, n=2000):
        iii = 0
        trouve = False
        while iii < n and trouve == False:
            self.reset()
            r = self.try_one_time()
            if r:
                self.pprint()
                print('TROUVE ! ')
                print(iii)
                print(self.has_play_with)
                trouve = True

            if iii % 100 == 0:
                print(' ')
                print(iii)
                print(' ')

            iii = iii + 1


planGames(5, 10).generate_n_plans()