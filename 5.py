class Stationary:
    def __init__(self, x):
        self.title = x

    def draw(self):
        print(f"{self.title.capitalize()}: запуск отрисовки.")


class Pencil(Stationary):
    def draw(self):
        print(f"{self.title.capitalize()}: запуск отрисовки с помощью карандаша.")


class Pen(Stationary):
    def draw(self):
        print(f"{self.title.capitalize()}: запуск отрисовки с помощью ручки.")


class Handle(Stationary):
    def draw(self):
        print(f"{self.title.capitalize()}: запуск отрисовки с помощью маркера.")


st_1 = Stationary("pencil")
st_1.draw()

st_2 = Pen("ручка")
st_2.draw()

st_3 = Pencil("карандаш")
st_3.draw()

st_4 = Handle("маркер")
st_4.draw()
