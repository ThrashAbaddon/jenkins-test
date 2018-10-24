class Car(object):
    def __init__(self, doors, horsepower, engine):
        assert isinstance(engine, Engine), 'Has to be Engine type.'
        self._doors = doors
        self._horsepower = horsepower
        self._engine = engine
        super(Car, self).__init__()

    @property
    def doors(self):
        return self._doors

    @property
    def horsepower(self):
        return self.engine.horsepower

    @property
    def engine(self):
        return self._engine


class Engine(object):
    def __init__(self, horsepower, consumption):
        self._horsepower = horsepower
        self._consumption = consumption
        super(Engine, self).__init__()

    @property
    def horsepower(self):
        return self._horsepower

    @property
    def consumption(self):
        return self._consumption
