class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f"{self.name} стартует"

    def stop(self):
        return f"{self.name} останавливается"

    def turn_right(self):
        return f"{self.name} поворачивает направо"

    def turn_left(self):
        return f"{self.name} поворачивает налево"

    def show_speed(self):
        return f"Скорость {self.name} = {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость городского авто {self.name} = {self.speed}")

        if self.speed > 60:
            return f"Скорость {self.name} выше допустимой для городского авто"
        else:
            return f"Скорость {self.name} допустима для городского авто"

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость спортивного авто {self.name} = {self.speed}")

        if self.speed > 180:
            return f"Камикадзе за рулем {self.name}"
        else:
            return f"Трезвомыслящий водитель {self.name}"


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость служебного авто {self.name} = {self.speed}")

        # if self.speed > 60:
        #     return f'Speed of {self.name} is higher than allow for work car'

        if self.speed > 40:
            return f"Скорость {self.name} выше допустимой для служебного авто"
        # else:
        #     return f"Скорость {self.name} допустима для служебного авто"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} полицеское авто"
        else:
            return f"{self.name} не полицеское авто"


Mercedes = SportCar(200, "синий", "Mercedes", False)
BMW = PoliceCar(150, "красный",  "BMW", True)
Lada = WorkCar(70, "чёрный", "Lada", False)
Toyota = TownCar(50, "белый", "Toyota", False)
print(Lada.turn_left())
print(f"Когда {Toyota.turn_right()}, то {Mercedes.stop()}")
print(f"{Lada.name} имеет цвет {Lada.color}")
print(f"{BMW.name} полицеское авто? {BMW.is_police}")
print(Mercedes.show_speed())
print(Toyota.show_speed())
print(Lada.show_speed())
print(BMW.police())
print(BMW.show_speed())
