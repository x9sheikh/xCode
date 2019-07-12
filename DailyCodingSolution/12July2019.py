""" Here you can solve the problem right Now"""

class Map:
    _dic = {}
    _replace = False
    _getValue = False
    def set(self, key, value, time):
        if self._dic == {}:
            print("Dict is empty")
            self._dic = {
                key: (value, time)
            }
            print(self._dic)
        else:
            for i in self._dic :
                if i == key and self._dic[i][1] == time:
                    self._dic[i] = (value, time)
                    print(self._dic)
                    print("Successfully repair value")
                    self._replace = True
                    break
            if self._replace == False:
                self._dic[key] = (value, time)
                print("Successfully add the new one")
                print(self._dic)
            #self._replace = False


    def get(self, key, time):
        for i in self._dic:
            if i == key and self._dic[i][1] == time:
                print("The value is "+str(self._dic[i][0]))
                self._getValue = True
                break
        if self._getValue == False:
            print("Null")

d = Map()
d.set(1,2,3)
d.set(10,12,13)
d.set(100,12,103)
d.set(1000,12,1003)
d.set(1,2,30)
d.get(10,13)
d.set(105,2,300)