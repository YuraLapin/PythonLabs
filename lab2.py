from ftplib import parse150
from array import *
import json

class Weapon:
    def __init__(self, damage = 0, price = 0, description = "empty description"):
        self.damage = damage
        self.price = price        
        self.description = description

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Armor:
    def __init__(self, defence = 0, price = 0, description = "empty description"):
        self.defence = defence
        self.price = price        
        self.description = description

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Damage_over_time:
    def __init__(self, max_duration = 0, damage = 0, description = "empty_description"):
        self.max_duration = max_duration
        self.cur_duration = max_duration
        self.damage = damage
        self.description = description

    def Tick(self, target):
        if (self.cur_duration > 0):
            self.cur_duration -= 1
            target.Receive_damage(self.damage)
        else:
            del self

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Character:
    def __init__(self, health = 100, right_hand = Weapon(), left_hand = Weapon(), armor = Armor()):
        self.health = health        
        self.right_hand = right_hand
        self.left_hand = left_hand
        self.armor = armor
        self.effect_list = []

    def Die(self, damage = 0):
        print(self.name + " received " + damage + " and died!")
        del self

    def Receive_damage(self, damage = 0):
        if (damage > self.health):
            self.Die(damage)
        else:
            self.health -= damage

    def Attack(self, target):
        target.Receive_damage(self.right_hand.damage + self.right_hand.damage - target.armor.defence)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Party:
    def __init__(self):        
        self.members = []    

    def Add_member(self, char = Character()):        
        self.members.append(char)

    def Delete_member(self, char = Character()):
        if (self.memebers.find(char) >= 0):            
            self.members.pop(self.members.find(char))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

text_file = open("classes.json", "w")
guild = Party()

yura = Character()
frostmourne = Weapon(100, 1000)
yura.right_hand = frostmourne
guild.Add_member(yura)

text_file.write(guild.toJSON())
text_file.close()