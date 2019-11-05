class shutter:
    def __init__(self, name, position, com):
        self.name = name
        self.position = position
        self.com = com

    def set_name(self, name2):
        self.name = name2

    def set_position(self, position2):
        self.position = position2

    def set_com(self,com2):
        self.com = com2

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_com(self):
        return self.com