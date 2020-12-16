from Demon import Demon
from DoomGuy import DoomGuy
from Weapons import Shotgun, Feast, Gausse_gun, Minigun
import random


class World:
    mainHero = DoomGuy(100, 50, 0.5)
    cyber_demon = Demon(4000, 200, 0.1, 5, "Cyber Demon")
    demon_list = []
    weapon_list = [Shotgun(100), Minigun(250), Gausse_gun(150)]
    is_created = False

    def __init__(self):
        print(f'Empty world is create')

    def create(self):
        for i in range(1):
            self.demon_list.append(Demon(200, 50, 0.5, 1, "Imp"))
        for i in range(4):
            self.demon_list.append(Demon(450, 70, 0, 3, "Knight of Hell"))
        for i in range(3):
            self.demon_list.append(Demon(300, 50, 0.2, 2, "Kako-Demon"))
        self.is_created = True
        print(f'World is not empty now... Are you ready?')

    def start(self):
        if self.is_created:
            self.mainHero.weapons.append(Feast())
            for i in range(2):
                self.weapon_list = self.mainHero.try_find(self.weapon_list)
            print(f'Demons is here...')
            self.pvp_fight()
            if self.mainHero.is_dead():
                print(f'Oh, dear... Demons win.')
            else:
                print(f"Let's start the REAL MASSACRE!")
                for i in range(3):
                    self.weapon_list = self.mainHero.try_find(self.weapon_list)
                self.pva_fight()
                if self.mainHero.is_dead():
                    print(f'It was close, but we miss them...')
                else:
                    print(f'The gates of hell is open now. Doom Slayer, your last battle is coming.')
                    for i in range(2):
                        self.mainHero.try_find(self.weapon_list)
                    if self.boss_fight():
                        print(f'Doom Slayer ended. HELL IS DESTROYED BY THEM!!!')
                    else:
                        print(f'Doom Slayer is dead...\n{self.cyber_demon.demon_name} - '
                              f'{self.cyber_demon.health_points} HP')
        else:
            print('World is not created!')

    def pvp_fight(self):
        target = self.choise_target()
        while not self.mainHero.is_dead():
            self.mainHero.attack(self.mainHero.weapons, target)
            if self.mainHero.special_finish(target, self.demon_list):
                break
            target.attack(self.mainHero)

    def pva_fight(self):
        while len(self.demon_list) > 1 and not self.mainHero.is_dead():
            self.demon_list = self.mainHero.aoe_attack(self.demon_list)
            target = self.choise_target()
            if not target.is_dead():
                self.mainHero = target.attack(self.mainHero)

    def boss_fight(self):
        while not self.mainHero.is_dead():
            self.mainHero.boss_attack(self.cyber_demon)
            if self.mainHero.special_finish_boss(self.cyber_demon):
                return True
            self.cyber_demon.attack(self.mainHero)
        return False

    def choise_target(self):
        return self.demon_list[random.randint(0, len(self.demon_list) - 1)]
