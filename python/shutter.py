from python import requestData


class shutter:
    def __init__(self, name, position, com):
        self.name = name
        self.position = position
        self.com = com
        #self.data = requestData.RequestData(self.get_com_data())

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

    def get_com_data(self):
        comp = 'COM' + str(self.com)
        return comp

    def get_temp(self):
        return self.data.temp()

    def get_light(self):
        return self.data.light()

    def get_distance(self):
        return self.data.distance()

    def get_down(self):
        return self.data.down()

    def get_up(self):
        return self.data.up()

    def close_port(self):
        return self.data.close_connection()

# d = shutter('dave', 'left', 5)
#
# print(d.get_com())
# print(d.get_name())
# d.set_name('steve')
# print(d.get_name())
# print(d.get_com_data())
# print(d.get_temp())