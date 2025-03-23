from simulation.elements import Atoms, Elements

class Matter:
    def __init__(self):
        self.elements = []

    def add_element(self, element: Elements):
        self.elements.append(element)

    def total_mass(self):
        return sum(Atoms[element].mass for element in self.elements)

    def total_energy(self):
        return sum(Atoms[element].valence * 10 for element in self.elements)