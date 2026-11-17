class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(self.name, "does a basic attack")


class Warrior(Character):
    def attack(self):
        print(self.name, "attacks with sword")


class Mage(Character):
    def attack(self):
        print(self.name, "casts a fireball")


class Archer(Character):
    def attack(self):
        print(self.name, "shoots an arrow")


w = Warrior("Warrior", 100)
m = Mage("Mage", 80)
a = Archer("Archer", 90)

w.attack()
m.attack()
a.attack()
