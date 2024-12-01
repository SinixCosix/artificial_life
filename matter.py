class Matter:
    def __init__(self):
        # Хранение элементов в виде: {Element(): int, }
        self.elements = {}

    def add_element(self, element, amount=1):
        if element not in self.elements:
            self.elements[element] = amount
            return

        self.elements[element] += amount

    def __repr__(self):
        return f"Matter({self.elements})"

    def total_mass(self):
        return sum(element.mass * quantity for element, quantity in self.elements.items())
