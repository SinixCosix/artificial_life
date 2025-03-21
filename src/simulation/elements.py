from enum import Enum
from dataclasses import dataclass


class Elements(Enum):
    H = 1
    He = 2

    Li = 3
    Be = 4   
    B = 5    
    C = 6    
    N = 7    
    O = 8    
    F = 9    
    Ne = 10 

    Na = 11  
    Mg = 12  
    Al = 13  
    Si = 14  
    P = 15   
    S = 16   
    Cl = 17  
    Ar = 18  


@dataclass
class Atom:
    number: Elements
    mass: float
    electron_gativity: float
    valence: int
    radius: float

    def __repr__(self):
        return f"Element({self.number}, mass={self.mass})"

    def __eq__(self, other: 'Elements'):
        return self.number == other.number

    def __hash__(self):
        return hash(self.number)

Atoms = [
    Atom(Elements.H,  mass=1.008,  electron_gativity=2.20, valence=1, radius=25),
    Atom(Elements.He, mass=4.0026, electron_gativity=0.00, valence=0, radius=31),
    
    Atom(Elements.Li, mass=6.94,   electron_gativity=0.98, valence=1, radius=145),
    Atom(Elements.Be, mass=9.0122, electron_gativity=1.57, valence=2, radius=112),
    Atom(Elements.B,  mass=10.81,  electron_gativity=2.04, valence=3, radius=85),
    Atom(Elements.C,  mass=12.011, electron_gativity=2.55, valence=4, radius=70),
    Atom(Elements.N,  mass=14.007, electron_gativity=3.04, valence=3, radius=65),
    Atom(Elements.O,  mass=15.999, electron_gativity=3.44, valence=2, radius=60),
    Atom(Elements.F,  mass=18.998, electron_gativity=3.98, valence=1, radius=50),
    Atom(Elements.Ne, mass=20.180, electron_gativity=0.00, valence=0, radius=38),
    
    Atom(Elements.Na, mass=22.990, electron_gativity=0.93, valence=1, radius=180),
    Atom(Elements.Mg, mass=24.305, electron_gativity=1.31, valence=2, radius=150),
    Atom(Elements.Al, mass=26.982, electron_gativity=1.61, valence=3, radius=125),
    Atom(Elements.Si, mass=28.085, electron_gativity=1.90, valence=4, radius=110),
    Atom(Elements.P,  mass=30.974, electron_gativity=2.19, valence=3, radius=100),
    Atom(Elements.S,  mass=32.06,  electron_gativity=2.58, valence=2, radius=100),
    Atom(Elements.Cl, mass=35.45,  electron_gativity=3.16, valence=1, radius=100),
    Atom(Elements.Ar, mass=39.948, electron_gativity=0.00, valence=0, radius=71),
]
