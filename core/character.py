import AlignmentEnum


class Character:
    __name__: str
    __alignment__: AlignmentEnum

    def setName(self, name: str):
        self.__name__ = name

    def getName(self):
        return self.__name__

    def setAlignment(self, alignment: AlignmentEnum):
        self.__alignment__ = alignment

    def getAlignment(self) -> AlignmentEnum:
        return self.__alignment__
