# er moet een network aangemaakt worden in de main
# ToDo add a way to remove a schutter from the list and te rename a shutter from the list
import shutter


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



# test network
# n = network()
# n.add_shutter(shutter.shutter('a', 'b', 5))
# n.add_shutter(shutter.shutter('b', 'b', 5))
# n.printlist()
# for shutter in n.get_shutter_list():
#     if shutter.get_name() == 'a':
#         n.remove_shutter(shutter)
#
# n.printlist()