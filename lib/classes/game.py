from classes.result import Result

class Game:
    def __init__(self, title):
        if(0<len(title)):
            self._title = title
        else:
            raise Exception ("must be a string with a length greater than 0")
    def get_title(self):
        return self._title
    def set_title(self, title):
        print ("set_title")
        raise Exception ("no fu")
    title = property(get_title, set_title)