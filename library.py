from game import Game

class Library:
    
    def __init__(self):
        self.__games = set()

    @property
    def games(self):
        return self.__games.copy()

    def addGame(self, game : Game):
        self.__games.add(game)

    def removeGame(self, game : Game):
        pass

    def getNbGames(self):
        return len(self.__games)

    def __repr__(self):
        return f'Library has {self.getNbGames()} game(s)'


if __name__ == '__main__':
    lib = Library()
    lib.addGame(Game())