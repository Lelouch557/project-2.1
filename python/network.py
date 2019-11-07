# er moet een network aangemaakt worden in de main


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

    def get_shutter_com_list(self):
        com_list = []
        for shut in self.shutterlist:
            com_list.append(shut.get_com())
        return com_list

    def get_shutter_name_list(self):
        name_list = []
        for shut in self.shutterlist:
            name_list.append(shut.get_name())
        return name_list

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