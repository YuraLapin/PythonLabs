from ftplib import parse150
from array import *

class Weapon:
    def __init__(self, damage = 0, price = 0, name = "unknown weapon", description = "empty description"):
        self.damage = damage
        self.price = price
        self.name = name
        self.description = description

class Armor:
    def __init__(self, defence = 0, price = 0, name = "unknown armor", description = "empty description"):
        self.defence = defence
        self.price = price
        self.name = name
        self.description = description

class Character:
    def __init__(self, health = 100, name = "unknown character", right_hand = Weapon(), left_hand = Weapon(), armor = Armor()):
        self.health = health
        self.name = name
        self.right_hand = right_hand
        self.left_hand = left_hand
        self.armor = armor
        self.effect_list = array(Damage_over_time)

    def Die(self, damage = 0):
        print(self.name + " received " + damage + " and died!")
        del self

    def Receive_damage(self, damage = 0):
        if (damage > self.health):
            self.Die(damage)
        else:
            self.health -= damage

    def Attack(self, target = Character()):
        target.Receive_damage(self.right_hand.damage + self.right_hand.damage - target.armor.defence)

class Damage_over_time:
    def __init__(self, max_duration = 0, damage = 0, name = "unknown effect", description = "empty_description"):
        self.max_duration = max_duration
        self.cur_duration = max_duration
        self.damage = damage
        self.name = name
        self.description = description

    def Tick(self, target = Character()):
        if (self.cur_duration > 0):
            self.cur_duration -= 1
            target.Receive_damage(self.damage)
        else:
            del self

class Party:
    def __init__(self, name = "unknown party"):        
        self.name = name
        self.members = array(Character)

    def Rename(self, new_name = "unknown name"):
        self.name = new_name

    def Add_member(self, char = Character()):        
        self.members.append(char)

    def Delete_member(self, char = Character()):
        if (self.memebers.find(char) >= 0):            
            self.members.pop(self.members.find(char))
