from librarystorage import LibraryStorage, LibraryJSON, LibraryDB
from library import Library
from game import Game

class Application:
    
    def __init__(self, libraryStorage : LibraryStorage):
        self.__libraryStorage = libraryStorage
        self.__library = Library()
        self.__actions = {
            'n': self.createGame,
            'd': self.removeGame,
            'g': self.displayGame,
            's': self.saveLibrary,
            'l': self.listLibrary,
            'r': self.reloadLibrary,
            'change storage': self.changeStorage,
        }

    def run(self):
        action = ''
        while action != 'q':
            action = input('Choose your action: ')
            print(f'Action chosen: {action}')
            if action in self.__actions.keys():
                self.__actions[action]()

    def listLibrary(self):
        for game in self.__library.games:
            print(game)

    def createGame(self):
        name = input('Name: ')
        image = input('Image: ')
        game = Game(name, image)
        self.__library.addGame(game)
    
    def removeGame(self):
        gameToRemove = input('Name to remove: ')
        self.__library.removeGame(gameToRemove)

    def displayGame(self):
        name = input('Name: ')
        games = [item for item in self.__library.games if item.name == name][:1]
        print(games)

    def saveLibrary(self):
        self.__libraryStorage.save(self.__library)

    def reloadLibrary(self):
        self.__library = self.__libraryStorage.read()

    def changeStorage(self):
        storageMode = input('Storage mode: ')
        if storageMode == 'json':
            self.__libraryStorage = LibraryJSON()
        if storageMode == 'sqlite3':
            self.__libraryStorage = LibraryDB()

if __name__ == '__main__':
    app = Application(LibraryJSON())
    app.run()