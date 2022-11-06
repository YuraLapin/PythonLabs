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

class Damage_over_time:
    def __init__(self, max_duration = 0, damage = 0, name = "unknown effect", description = "empty_description"):
        self.max_duration = max_duration
        self.cur_duration = max_duration
        self.damage = damage
        self.name = name
        self.description = description    

class Party:
    def __init__(self, name = "unknown party"):        
        self.name = name
        self.members = array(Character)    
