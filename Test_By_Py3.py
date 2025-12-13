class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def rname(self):
        return f'{self.name}'
    def rage(self):
        return f'{self.age}'

    def test(self):
        name = self.rname()
        age = self.rage()
        return f'{name}, {age}'

ivan = People("Ваня", 14)

print(ivan.test())