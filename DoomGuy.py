from Creature import Creature
from Weapons import Shotgun, Minigun, Gausse_gun, Feast
import random


class DoomGuy(Creature):
    weapons = []

    def __init__(self, health_points, armor_points, agility):
        self.health_points = health_points
        self.armor_points = armor_points
        self.agility = agility

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        print(f"Oh, God, DoomGuy find {weapon.name}! It is time to kick some demon, aren't it?")

    def attack(self, weapon_list, demon):
        weapon = self.choise_weapon(weapon_list, demon)
        damage_counter = 0
        if isinstance(weapon, Shotgun) or isinstance(weapon, Feast):
            count = round(demon.demon_class * 1.5)
        elif isinstance(weapon, Minigun):
            count = demon.demon_class * 10
        elif isinstance(weapon, Gausse_gun):
            count = 1
        for i in range(count):
            if demon.is_dead():
                break
            demon.health_points -= weapon.shot(demon)
            if weapon.shot(demon) == 0:
                print(f'No ammo on {weapon.name}. It is time to change a toy')
                weapon = self.choise_weapon(weapon_list, demon)
            damage_counter += weapon.shot(demon)
        print(f'DoomGuy attack {demon.demon_name}. -{damage_counter}HP! ')
        return demon

    def aoe_attack(self, demon_list):
        target = demon_list[random.randint(0, len(demon_list) - 1)]
        weapon = self.choise_weapon(self.weapons, target)

        if isinstance(weapon, Gausse_gun) or isinstance(weapon, Shotgun):
            demon_list = weapon.special_attack(demon_list)
            for demon in demon_list:
                self.special_finish(demon, demon_list)
        elif isinstance(weapon, Minigun):
            damage_counter = 0
            for i in range(len(demon_list)):
                demon_list[i].health_points -= weapon.special_attack(demon_list[i])
                damage_counter += weapon.special_attack(demon_list[i])
            for demon in demon_list:
                self.special_finish(demon, demon_list)
            print(f'Demons take {damage_counter} damage!')
        elif isinstance(weapon, Feast):
            demon_list[random.randint(0, len(demon_list) - 1)].health_points -= weapon.special_attack()
            for demon in demon_list:
                self.special_finish(demon, demon_list)
            print(f'Some Demon get {weapon.special_attack()} damage! That was great punch')

        return demon_list

    def boss_attack(self, boss):
        for i in range(3):
            weapon = self.choise_weapon(self.weapons, boss)
            damage = 0
            if isinstance(weapon, Feast):
                for j in range(5):
                    boss.health_points -= weapon.special_attack()
                    damage += weapon.special_attack()
                print(f'{boss.demon_name} get 10 punches from Doom Slayer! -{damage}HP!')
            elif isinstance(weapon, Gausse_gun) or isinstance(weapon, Shotgun):
                while weapon.ammunition >= weapon.spend_for_sshot:
                    boss.health_points -= weapon.special_attack_f1(boss)
            else:
                while weapon.ammunition > weapon.spend_for_sshot:
                    boss.health_points -= weapon.special_attack(boss)
                    damage += weapon.special_attack(boss)
                print(f'{boss.demon_name} get {damage} damage!')
            if damage == 0:
                while weapon.ammunition > weapon.spend_for_shot:
                    damage = weapon.shot(boss)
                    boss.health_points -= damage
                    print(f'{boss.demon_name} get {damage} damage!')

    def is_dead(self):
        if self.health_points <= 0:
            return True
        else:
            return False

    def try_find(self, weapon_list):
        if len(weapon_list) > 0:
            num = random.randint(0, len(weapon_list) - 1)
            if weapon_list[num] not in self.weapons:
                self.weapons.append(weapon_list[num])
            print(f"Oh, God, DoomGuy find {weapon_list[num].name}! It is time to kick some demon, aren't it?")
            weapon_list.pop(num)
        for weapon in self.weapons:
            weapon.ammunition += 50
        print(f'DoomGuy find some bullets')

        return weapon_list

    def special_finish(self, demon, world_list):
        threshold = demon.demon_class * 100 * 0.2
        if demon.health_points <= threshold:
            world_list.remove(demon)
            print(demon.demon_name + " has been TOTALY DESTROED!")
            return True
        else:
            return False

    def special_finish_boss(self, boss):
        threshold = boss.demon_class * 100 * 0.2
        if boss.health_points <= threshold:
            print(boss.demon_name + " has been TOTALY DESTROED! RAAAAAMPAAAAAGE!")
            return True
        else:
            return False

    def choise_weapon(self, weapon_list, demon):
        cur_weapon = Feast()
        coin = 0
        biggest_coin = 0
        for weapon in weapon_list:
            if weapon.ammunition > weapon.spend_for_shot:
                coin += 1
            coin -= abs(demon.demon_class - weapon.weapon_lvl)/10
            if coin > biggest_coin:
                cur_weapon = weapon
                biggest_coin = coin
            coin = 0
        print(f'It will be {cur_weapon.name}')
        return cur_weapon

    def __str__(self):
        return f'DoomGuy (Doom Slayer):\n' \
               f'HP - {self.health_points}\n' \
               f'Armor - {self.armor_points}\n' \
               f'Agility - {self.agility}\n'