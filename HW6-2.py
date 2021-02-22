class Road:
    def __init__(self, _length, _width, _volume, _height):
        self.length = _length
        self.width = _width
        self.volume = _volume
        self.height = _height

    def mass(self):
        return f"{self.length * self.width * self.volume * self.height / 1000} тонн"


class MassCount(Road):
    def __init__(self, _length, _width, _volume, _height):
        super().__init__(_length, _width, _volume, _height)
        self.volume = _volume
        self.height = _height


r = MassCount(20, 5000, 25, 5)
print(r.mass())
