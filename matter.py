class Matter:
    def __init__(self):
        # Хранение элементов в виде: {"O": 5, "H": 10}
        self.elements = {}

    def add_element(self, element, amount=1):
        if element.symbol in self.elements:
            self.elements[element.symbol] += amount
        else:
            self.elements[element.symbol] = amount

    def __repr__(self):
        return f"Matter({self.elements})"
