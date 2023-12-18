class Game:
    
    def __init__(self, name, image):
        self.__name = name
        self.__image = image
        self.__tags = set()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value    

    @property
    def tags(self):
        return self.__tags.copy()

    def addTag(self, tag):
        self.__tags.add(tag)

    def __repr__(self):
        return f'{self.__name}: {self.__image}'

    def __hash__(self):
        return hash(self.__name)

    def __eq__(self, other):
        return self.__name == other.__name


if __name__ == '__main__':
    g1 = Game('game1', '/path/to/image/1.jpg')
    g2 = Game('game1', '/path/to/image/2.jpg')
    g3 = Game('game1', '/path/to/image/1.jpg')
    myset = set()
    myset.add(g1)
    print(myset)
    myset.add(g2)
    print(myset)
    myset.add(g1)
    print(myset)
    myset.add(g3)
    print(myset)
