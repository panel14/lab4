from abc import ABC, abstractmethod
import random


class Weapons(ABC):
    damage = 0
    spend_for_shot = 0
    ammunition = 0
    armor_coef = 0.08
    name = "weapon"
    weapon_lvl = 0

    def shot(self, demon):
        if self.ammunition >= self.spend_for_shot:
            self.ammunition -= self.spend_for_shot
            total_damage = self.damage * (1 - demon.agility) - demon.armor_points * self.armor_coef
            return total_damage
        else:
            return 0

    def __str__(self):
        return f'Weapon {self.name}:\n' \
               f'Ammunition - {self.ammunition}'

    @abstractmethod
    def special_attack(self):
        pass


class Shotgun(Weapons, ABC):
    damage = 80
    spend_for_shot = 10
    spend_for_sshot = 50
    ammunition = 0
    name = "Shotgun"
    weapon_lvl = 1

    def __init__(self, ammunition):
        self.ammunition = ammunition

    def special_attack(self, demons_list):
        if self.ammunition >= self.spend_for_sshot:
            for demon in demons_list:
                demon.health_points -= self.damage * 3.5
            self.ammunition -= self.spend_for_sshot
            print(f'Shotgun grenades damage enemys for {self.damage * 3.5} HP!')
        return demons_list

    def special_attack_f1(self, demon):
        if self.ammunition >= self.spend_for_sshot:
            self.ammunition -= self.spend_for_sshot
            print(f'Shotgun grenades damage {demon.demon_name} for {self.damage * 3.5} HP!')
            return self.damage * 3.5
        else:
            return 0




class Feast(Weapons):
    damage = 25
    name = "Feast"
    weapon_lvl = -1
    spend_for_shot = 0

    def __init__(self):
        pass

    def get_damage(self):
        return self.damage

    def special_attack(self):
        return self.damage * round(random.uniform(1, 2))


class Minigun(Weapons):
    damage = 30
    spend_for_shot = 5
    spend_for_sshot = 15
    ammunition = 0
    name = "Minigun"
    armor_coef = 0.08
    weapon_lvl = 2

    def __init__(self, ammunition):
        self.ammunition = ammunition

    def special_attack(self, demon):
        if self.ammunition >= self.spend_for_sshot:
            total_damage = self.damage * 2 * (1 - demon.agility) - demon.armor_points * self.armor_coef
            self.ammunition -= self.spend_for_sshot
            return total_damage
        else:
            return 0


class Gausse_gun(Weapons):
    damage = 200
    spend_for_shot = 50
    spend_for_sshot = 150
    ammunition = 0
    name = "Gausse gun"
    weapon_lvl = 3

    def __init__(self, ammunition):
        self.ammunition = ammunition

    def special_attack(self, demons_list):
        if self.ammunition >= self.spend_for_sshot:
            for demon in demons_list:
                demon.health_points -= self.damage * 2.5
            self.ammunition -= self.spend_for_sshot
            print(f'All Demons get {self.damage * 2.5} DAMAGE!!!')
        return demons_list

    def special_attack_f1(self, demon):
        if self.ammunition >= self.spend_for_sshot:
            self.ammunition -= self.spend_for_sshot
            print(f'{demon.demon_name} get {self.damage * 2.5} DAMAGE!!!')
            return self.damage*2.5
        else:
            return 0
