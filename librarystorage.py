from abc import ABC, abstractmethod
import jsonpickle

class LibraryStorage(ABC):
    
    @abstractmethod
    def save(self, library):
        pass

    @abstractmethod
    def read(self):
        pass

class LibraryJSON(LibraryStorage):

    def __init__(self):
        super().__init__()
        self.__fileLocation = 'test.json'

    def save(self, library):
        with open(self.__fileLocation, 'w') as dbfile:
            result = jsonpickle.encode(library)
            dbfile.write(result)

    def read(self):
        with open(self.__fileLocation, 'r') as dbfile:
            lines = dbfile.readlines()
            rawJson = ''
            for line in lines:
                rawJson += line
            result = jsonpickle.decode(rawJson)
        return result

class LibraryDB(LibraryStorage):

    def save(self, library):
        pass

    def read(self):
        pass