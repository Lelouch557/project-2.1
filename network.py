class network:
    def __init__(self):
        self.shutterlist = list()

    def add_shutter(self, name):
        self.shutterlist += name

    def printlist(self):
        print(self.shutterlist)

