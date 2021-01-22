import random


class Person:
    def __init__(self, hp, mp, stamina, atk, df, magic, skill):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.stamina = stamina
        self.maxstamina = stamina
        self.atklow = atk - 10
        self.atkhigh = atk + 10
        self.df = df
        self.magic = magic
        self.skill = skill
        self.actions = ["Attack", "Magic", "Skills"]
    

    def generate_dmg(self):
        return random.randrange(self.atklow, self.atkhigh)

    def generate_spell_damage(self, i):
        dmglow = self.magic[i]["dmg"] - 5
        dmghigh = self.magic[i]["dmg"] + 5
        return random.randrange(dmglow, dmghigh)

    def generate_skill_damage(self, i):
        dmglow = self.skill[i]["dmg"] - 15
        dmghigh = self.skill[i]["dmg"] + 15
        return random.randrange(dmglow, dmghigh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def get_stamina(self):
        return self.stamina

    def get_max_stamina(self):
        return self.maxstamina

    def reduce_mp(self, cost):
        self.mp -= cost
    
    def reduce_stamina(self, cost):
        self.stamina -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def get_skill_name(self, i):
        return self.skill[i]["name"]

    def get_skill_cost(self, i):
        return self.skill[i]["cost"]

    def choose_action(self):
        i = 1
        print("What will you do?")
        for items in self.actions:
            print(str(i) + ":", items)
            i += 1

    def choose_magic(self):
        i = 1
        print("\nYour spells:")
        for spells in self.magic:
            print(str(i) + ":", spells["name"], "(cost:", str(spells["cost"]), ")")
            i += 1

    def choose_skills(self):
        i = 1
        print("\nYour skills:")
        for skills in self.skill:
            print(str(i) + ":", skills["name"], "(cost:", str(skills["cost"]), ")")
            i += 1
