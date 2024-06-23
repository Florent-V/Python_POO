class Bird:
    """Un oiseau. 🐦"""

    # ici on utilise deux attributs de classe.
    names = ("mouette", "pigeon", "moineau", "hirrondelle")
    positions = {}

    def __init__(self, name, position=(1, 2)):
        """Les attributs définis ici sont des attributs d'instance."""
        self.position = position
        self.name = name
        
        # On accède à l'attribut de classe "positions" avec self (c'est possible).
        self.positions[self.position] = self.name

    @classmethod
    def find_bird(cls, position):
        """Retrouve un oiseau selon la position donnée."""
        if position in cls.positions:
            return f"On a trouvé un {cls.positions[position]} !"

        return "On a rien trouvé..."


# On peut accéder aux variables de classe sans instanciation.
print(Bird.names)
print(Bird.positions)
print(Bird.find_bird((2, 5)))

# On instancie un oiseau
bird = Bird("mouette")
print(Bird.names)
print(Bird.positions)

bird = Bird("pigeon", (2, 5))
print(Bird.names)
print(Bird.positions)

# On le retrouve avec la méthode find_bird.
#print(Bird.find_bird((1, 2)))