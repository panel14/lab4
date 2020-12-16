from Creature import Creature


class Demon(Creature):
    demon_class = 1
    armor_coef = 0.08
    threshould = demon_class * 100 * 0.2

    def __init__(self, health_points, armor_points, agility, demon_class, demon_name):
        self.health_points = health_points
        self.armor_points = armor_points
        self.agility = agility
        self.demon_class = demon_class
        self.demon_name = demon_name

    def attack(self, doomguy):
        attack_damage = self.demon_class * 15
        total_damage = attack_damage * (1 - doomguy.agility) - self.armor_coef * doomguy.armor_points
        doomguy.health_points -= round(total_damage)
        doomguy.armor_points -= self.armor_coef * doomguy.armor_points
        print(f'Ouf, demons damage DoomGay, at {round(total_damage)} HP!')
        return doomguy

    def is_dead(self):
        if self.health_points <= self.threshould:
            return True
        else:
            return False

    def try_find(self):
        print(f'Demons always see you...')

    def __str__(self):
        return f'Demon {self.demon_name}:\n' \
               f'HP - {self.health_points}\n' \
               f'Armor - {self.armor_points}\n' \
               f'Agility - {self.agility}\n' \
               f'Demon class - {self.demon_class}'
