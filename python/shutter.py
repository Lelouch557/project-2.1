from time import sleep

import requestData
#updated

class shutter:
    def __init__(self, name, position, com):
        self.name = name
        self.position = position
        self.com = com
        self.data = 'COM' + str(self.com)
        self.d = requestData.RequestData(self.data)
        self.temp_data = []
        self.light_data = []

    def check(self, string):
        temp = string.decode()[:-4:]
        if temp == '':
            return False
        else:
            return True

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

    def get_temp_array(self):
        return self.temp_data

    def get_temp(self):
        temp = self.d.temp()
        if(self.check(temp)):
            temp = temp.decode()
            return temp[:-4:]
        else:
            return self.get_temp()

    def get_light(self):
        temp = self.d.light()
        if(self.check(temp)):
            temp = temp.decode()
            return temp[:-4:]
        else:
            return self.get_light()

    def get_light_array(self):
        return self.light_data

    def get_distance(self):
        return self.d.distance()

    def get_down(self):
        temp = self.d.down()
        sleep(1.5) # sleep needs to be the same amount of time as arduino needs to get down + 0.5 sec
        return temp

    def get_up(self):
        temp = self.d.up()
        sleep(1.5) # sleep needs to be the same amount of time as arduino needs to get down + 0.5 sec
        return temp

    def close_port(self):
        return self.d.close_connection()

    def step(self):
        t = self.get_temp()
        self.temp_data.append(int(t))
        t = int(self.get_light())
        t = t/10
        print(t)
        self.light_data.append(t)

#
# d = shutter('dave', 'left', 6)
# print(d.get_com())
# print(d.get_name())
# d.set_name('steve')
# print(d.get_name())
# print(d.get_com_data())
# temp = d.get_temp()
# print(temp[:-4:])
# temp = d.get_light()
# print(temp[:-4:])
# d.close_port()