from ftplib import parse150
from array import *
import json


class Weapon:
    def __init__(self, name = "unknown weapon", damage = 0, price = 0, description = "Empty description"):
        self.name = name
        self.damage = damage
        self.price = price        
        self.description = description

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

class Shield:
    def __init__(self, name = "unknown shield", defence = 0, price = 0, description = "Empty_description"):
        self.name = name
        self.defence = defence
        self.price = price
        self.description = description

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

class Armor:
    def __init__(self, name = "unknown armor", defence = 0, price = 0, description = "Empty description"):
        self.name = name
        self.defence = defence
        self.price = price        
        self.description = description

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

class Character:
    def __init__(self, name = "unknown character", health = 100, weapon = Weapon(), shield = Shield(), armor = Armor()):
        self.name = name
        self.health = health        
        self.weapon = weapon
        self.shield = shield
        self.armor = armor        

    def die(self, damage = 0):
        print(self.name + " received " + damage + " and died!")
        del self

    def receive_damage(self, damage = 0):
        if (damage > self.health):
            self.die(damage)
        else:
            self.health -= damage

    def attack(self, target):
        dmg = self.weapon.damage - target.armor.defence - target.left_hand.defence
        if dmg < 0:
            dmg = 0
        target.Receive_damage(dmg)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def print(self):
        print(self.name + ": hp = " + str(self.health) + ", weapon_dmg = " + str(self.weapon.damage) + ", shield_defence = " + str(self.shield.defence) + ", armor_defence = " + str(self.armor.defence))

class Party:
    def __init__(self):        
        self.members = []    

    def add_member(self, char = Character()):        
        self.members.append(char)

    def delete_member(self, char = Character()):
        if (self.memebers.find(char) >= 0):            
            self.members.pop(self.members.find(char))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def print(self):
        for item in self.members:
            item.print()

def import_party(file_name):
    with open(file_name, "r") as the_file:
        raw_party = json.load(the_file)
        new_party = Party()
        for member in raw_party["members"]:
            new_character = Character()
            new_character.name = member["name"]
            new_character.health = member["health"]
            new_character.weapon = Weapon(member["weapon"]["name"], member["weapon"]["damage"], member["weapon"]["price"], member["weapon"]["description"])
            new_character.shield = Shield(member["shield"]["name"], member["shield"]["defence"], member["shield"]["price"], member["shield"]["description"])
            new_character.armor = Armor(member["armor"]["name"], member["armor"]["defence"], member["armor"]["price"], member["armor"]["description"])
            new_party.add_member(new_character)
    return new_party

def export_party(file_name, party):
    with open(file_name, "w") as the_file:
        the_file.write(party.to_json())


example_party = Party()
example_party.add_member(Character("example_char1", 90, Weapon("Frostmourne", 100, 1000), Shield("The Door", 10, 2000), Armor("Havel armor", 30, 1500)))
example_party.add_member(Character("example_char2", 80, Weapon("Shadowmourne", 50, 800), Shield("Great Protector", 8, 1000), Armor("Loincloth", 20, 1000)))

print("Party sent to JSON file:")
example_party.print()

export_party("the_file.json", example_party)

imported_party = import_party("the_file.json")
print("\nParty received from JSON file:")
imported_party.print()