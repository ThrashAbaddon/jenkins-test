class Car(object):

    def __init__(self, doors, horsepower):
        self._doors = doors
        self._horsepower = horsepower
        super(Car, self).__init__()


    @property
    def doors(self):
        return self._doors

    @property
    def horsepower(self):
        return self._horsepower
