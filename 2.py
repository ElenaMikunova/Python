class Road:

    def __init__(self, x, y):
        self._width = x
        self._length = y

    def road_met(self):
        z = 5
        mass = 25
        print(f"Масса асфальта: {z * mass * self._length * self._width / 1000:.0f} тонн")


road_1 = Road(20, 5056)
road_1.road_met()
road_2 = Road(10, 4000)
road_2.road_met()
