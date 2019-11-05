# er moet een network aangemaakt worden in de main
# ToDo add a way to remove a schutter from the list and te rename a shutter from the list

class network:
    def __init__(self):
        self.shutterlist = list()

    def add_shutter(self, name):
        self.shutterlist.append(name)

    def printlist(self):
        for shutter in self.shutterlist:
            print(shutter.get_name())

    def get_shutter_list(self):
        return self.shutterlist

    def remove_shutter(self, name):
        self.shutterlist.remove(name)