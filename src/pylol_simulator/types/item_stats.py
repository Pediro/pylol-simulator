class Item_Stat(object):

    def __init__(self, ability_power, armour, armour_penetration, attack_damage, attack_speed, cooldown_reduction, \
                critical_strike_chance, gold_per_10, heal_and_shield_power, health, health_regen, leathality, \
                lifesteal, magic_penetration, magic_resistance, mana, mana_regen, movespeed, ability_haste, omnivamp, tenacity):
        self.ability_power = ability_power
        self.armour = armour
        self.armour_penetration = armour_penetration 
        self.attack_damage = attack_damage
        self.attack_speed = attack_speed
        self.cooldown_reduction = cooldown_reduction
        self.critical_strike_chance = critical_strike_chance
        self.gold_per_10 = gold_per_10
        self.heal_and_shield_power = heal_and_shield_power
        self.health = health
        self.health_regen = health_regen
        self.leathality = leathality
        self.lifesteal = lifesteal
        self.magic_penetration = magic_penetration
        self.magic_resistance = magic_resistance
        self.mana = mana
        self.mana_regen = mana_regen
        self.movespeed = movespeed
        self.ability_haste = ability_haste
        self.omnivamp = omnivamp
        self.tenacity = tenacity

    def __str__(self) -> str:
        return f"Stats:\n"\
            f"Ability Power: {self.ability_power}\n"\
            f"Armour: {self.armour}\n"\
            f"Armour Penetration: {self.armour_penetration}\n"\
            f"Attack Damage: {self.attack_damage}\n"\
            f"Attack Speed: {self.attack_speed}\n"\
            f"Cooldown Reduction: {self.cooldown_reduction}\n"\
            f"Critical Strike Chance: {self.critical_strike_chance}\n"\
            f"Gold Per 10: {self.gold_per_10}\n"\
            f"Heal and Shield Power: {self.heal_and_shield_power}\n"\
            f"Health: {self.health}\n"\
            f"Health Regen: {self.health_regen}\n"\
            f"Leathality: {self.leathality}\n"\
            f"Lifesteal: {self.lifesteal}\n"\
            f"Magic Penetration: {self.magic_penetration}\n"\
            f"Magic Resistance: {self.magic_resistance}\n"\
            f"Mana: {self.mana}\n"\
            f"Mana Regen: {self.mana_regen}\n"\
            f"Movespeed: {self.movespeed}\n"\
            f"Ability Haste: {self.ability_haste}\n"\
            f"Omnivamp: {self.omnivamp}\n"\
            f"Tenacity: {self.tenacity}\n"\

    def __repr__(self) -> str:
        return str(self)