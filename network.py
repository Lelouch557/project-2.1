# er moet een network aangemaakt worden in de main
# ToDo add a way to remove a schutter from the list and te rename a shutter from the list

class network:
    def __init__(self):
        self.shutterlist = list()

    def add_shutter(self, name):
        self.shutterlist += name

    def printlist(self):
        print(self.shutterlist)

