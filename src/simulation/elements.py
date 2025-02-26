class Element:
    def __init__(self, symbol=None, mass=0, color=(255, 255, 255)):
        self.symbol = symbol
        self.mass = mass
        self.color = color

    def __repr__(self):
        return f"Element({self.symbol}, mass={self.mass})"

    def __eq__(self, other):
        return self.symbol == other.symbol

    def __hash__(self):
        return hash(self.symbol)


class Oxygen(Element):
    def __init__(self):
        super().__init__("O", 16, (0, 0, 255))


class Hydrogen(Element):
    def __init__(self):
        super().__init__("H", 1, (255, 255, 255))


class Carbon(Element):
    def __init__(self):
        super().__init__("C", 12, (100, 100, 100))


class Iron(Element):
    def __init__(self):
        super().__init__("Fe", 56, (255, 0, 0))


class Silicon(Element):
    def __init__(self):
        super().__init__("Si", 28, (255, 165, 0))  # Оранжевый цвет


class Calcium(Element):
    def __init__(self):
        super().__init__("Ca", 40, (173, 216, 230))  # Голубой цвет


ELEMENTS = {
    "O": Oxygen(),
    "H": Hydrogen(),
    "C": Carbon(),
    "Fe": Iron(),
    "Si": Silicon(),
    "Ca": Calcium()
}
