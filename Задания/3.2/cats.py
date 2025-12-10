
class Cat:
    def __init__(self, name):
        self.name = name  # self сохраняет имя для этого котика
        self.murka = "Мурка"
    def meow(self):
        return f"{self.name} говорит: Мяу-мяу!"  # self.name обращается к имени конкретного объекта
# Создаем двух котиков

barsik = Cat("Барсик")

print(murka.meow())   # Мурка говорит: Мяу-мяу!
print(barsik.meow())  # Барсик говорит: Мяу-мяу!
