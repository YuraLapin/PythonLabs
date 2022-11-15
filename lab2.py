from ftplib import parse150
from array import *
import json


class Weapon:
    def __init__(self, *args):
        if (len(args) == 0):
            self.name = "unknown weapon"
            self.damage = 0
            self.price = 0        
            self.description = "Empty description"
        elif (len(args) == 1):
            self.name = args[0]["name"]
            self.damage = args[0]["damage"]
            self.price = args[0]["price"]
            self.description = args[0]["description"]
        elif (len(args) == 3):
            self.name = args[0]
            self.damage = args[1]
            self.price = args[2] 
            self.description = "Empty description"
        elif (len(args) == 4):
            self.name = args[0]
            self.damage = args[1]
            self.price = args[2]        
            self.description = args[3]  

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def import_file(self, file_name):
        with open(file_name, "r") as the_file:
            raw_weapon = json.load(the_file)
            self.name = raw_weapon["name"]
            self.damage = raw_weapon["damage"]
            self.price = raw_weapon["price"]
            self.description = raw_weapon["description"]

    def export_file(self, file_name):
        with open(file_name, "w") as the_file:
            the_file.write(self.to_json())

class Shield:
    def __init__(self, *args):
        if (len(args) == 0):
            self.name = "unknown shield"
            self.defence = 0
            self.price = 0        
            self.description = "Empty description"
        elif (len(args) == 1):
            self.name = args[0]["name"]
            self.defence = args[0]["defence"]
            self.price = args[0]["price"]
            self.description = args[0]["description"]
        elif (len(args) == 3):
            self.name = args[0]
            self.defence = args[1]
            self.price = args[2]  
            self.description = "Empty description"
        elif (len(args) == 4):
            self.name = args[0]
            self.defence = args[1]
            self.price = args[2]        
            self.description = args[3]  

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def import_file(self, file_name):
        with open(file_name, "r") as the_file:
            raw_shield = json.load(the_file)
            self.name = raw_shield["name"]
            self.defence = raw_shield["defence"]
            self.price = raw_shield["price"]
            self.description = raw_shield["description"]

    def export_file(self, file_name):
        with open(file_name, "w") as the_file:
            the_file.write(self.to_json())

class Armor:
    def __init__(self, *args):
        if (len(args) == 0):
            self.name = "unknown armor"
            self.defence = 0
            self.price = 0        
            self.description = "Empty description"
        elif (len(args) == 1):
            self.name = args[0]["name"]
            self.defence = args[0]["defence"]
            self.price = args[0]["price"]
            self.description = args[0]["description"]
        elif (len(args) == 3):
            self.name = args[0]
            self.defence = args[1]
            self.price = args[2] 
            self.description = "Empty description"
        elif (len(args) == 4):
            self.name = args[0]
            self.defence = args[1]
            self.price = args[2]        
            self.description = args[3]        

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def import_file(self, file_name):
        with open(file_name, "r") as the_file:
            raw_armor = json.load(the_file)
            self.name = raw_armor["name"]
            self.defence = raw_armor["defence"]
            self.price = raw_armor["price"]
            self.description = raw_armor["description"]

    def export_file(self, file_name):
        with open(file_name, "w") as the_file:
            the_file.write(self.to_json())

class Character:
    def __init__(self, *args):
        if len(args) == 0:
            self.name = "unknown character"
            self.health = 100        
            self.weapon = Weapon()
            self.shield = Shield()
            self.armor = Armor() 
        elif (len(args) == 1):
            self.name = args[0]["name"]
            self.health = args[0]["health"]
            self.weapon = Weapon(args[0]["weapon"])
            self.shield = Shield(args[0]["shield"])
            self.armor = Armor(args[0]["armor"])
        elif (len(args) == 5):
            self.name = args[0]
            self.health = args[1]        
            self.weapon = args[2]
            self.shield = args[3]
            self.armor = args[4]          

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

    def import_file(self, file_name):
        with open(file_name, "r") as the_file:
            raw_character = json.load(the_file)
            self.name = raw_character["name"]
            self.health = raw_character["health"]
            self.weapon = Weapon(raw_character["weapon"])
            self.shield = Shield(raw_character["shield"])
            self.armor = Armor(raw_character["armor"])

    def export_file(self, file_name):
        with open(file_name, "w") as the_file:
            the_file.write(self.to_json())

class Party:
    def __init__(self):        
        self.members = []    

    def add_member(self, char):        
        self.members.append(char)

    def delete_member(self, char):
        if (self.memebers.find(char) >= 0):            
            self.members.pop(self.members.find(char))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def print(self):
        for item in self.members:
            item.print()

    def import_file(self, file_name):
        with open(file_name, "r") as the_file:
            raw_party = json.load(the_file)
            self.members = []
            for member in raw_party["members"]:
                self.add_member(Character(member))

    def export_file(self, file_name):
        with open(file_name, "w") as the_file:
            the_file.write(self.to_json())


example_party = Party()
example_party.add_member(Character("example_char1", 90, Weapon("Frostmourne", 100, 1000), Shield("The Door", 10, 2000), Armor("Havel armor", 30, 1500)))
example_party.add_member(Character("example_char2", 80, Weapon("Shadowmourne", 50, 800), Shield("Great Protector", 8, 1000), Armor("Loincloth", 20, 1000)))

print("Party sent to JSON file:")
example_party.print()

example_party.export_file("the_file.json")

imported_party = Party()
imported_party.import_file("the_file.json")
print("\nParty received from JSON file:")
imported_party.print()
