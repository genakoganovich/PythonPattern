# Abstraction
class Weapon:
    def __init__(self, name):
        self.name = name
        self.damage = 0
        self.enchantment = None

    def attack(self):
        pass


# Implementation
class Sword:
    def __init__(self):
        self.damage = 10

    def attack(self):
        print("Swinging sword for {} damage".format(self.damage))


class Axe:
    def __init__(self):
        self.damage = 15

    def attack(self):
        print("Chopping axe for {} damage".format(self.damage))


# Bridge
class EnchantedWeapon(Weapon):
    def __init__(self, weapon, enchantment):
        self.weapon = weapon
        self.enchantment = enchantment

    def attack(self):
        self.weapon.attack()
        if self.enchantment:
            print("Applying enchantment: {}".format(self.enchantment))


# Usage
sword = Weapon("Sword")
axe = Weapon("Axe")
sword_weapon = Sword()
enchanted_sword = EnchantedWeapon(sword_weapon, "Fire")
axe_weapon = Axe()
enchanted_axe = EnchantedWeapon(axe_weapon, "Ice")
enchanted_sword.attack()  # Swinging sword for 10 damage, Applying enchantment: Fire
enchanted_axe.attack()  # Chopping axe for 15 damage, Applying enchantment: Ice
