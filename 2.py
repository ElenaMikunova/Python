from abc import ABC, abstractmethod
a = []


class Clothes(ABC):
    @abstractmethod
    def item_mat(self):
        pass


class Suit(Clothes):

    def __init__(self, high):
        self.high = high

    @property
    def my_high(self):
        return self.high

    def item_mat(self):
        a.append((self.my_high * 2 + 30) / 100)
        return f"На пошив костюма потребуется {(self.my_high * 2 + 30) / 100} м ткани.\n"


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def my_size(self):
        return self.size

    def item_mat(self):
        a.append(round(self.my_size / 6.5 + 0.5, 2))
        return f"На пошив пальто потребуется {round(self.my_size / 6.5 + 0.5, 2)} м ткани.\n"


suit_1 = Suit(170)
suit_2 = Suit(180)
suit_3 = Suit(160)
print(suit_1.item_mat())
print(suit_2.item_mat())
print(suit_3.item_mat())

coat_1 = Coat(46)
coat_2 = Coat(50)
print(coat_1.item_mat())
print(coat_2.item_mat())

print(f"Общее количество необходимой ткани: {round(sum(a), 2)} м.")
