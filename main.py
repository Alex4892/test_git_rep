class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    def __str__(self):
        return f"{self.name} {self.galaxy}"
sun = Star("Солнце", "Млечный Путь")
print(sun)
print(isinstance(sun, Star))