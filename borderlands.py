import random


class Gun:
    def __init__(self, name, damage, reload_speed, mag_size, rarity):
        self.name = name
        self.damage = damage
        self.reload_speed = reload_speed
        self.mag_size = mag_size
        self.rarity = rarity

    def shoot(self):
        print(f'{self.name} Fired shot dealing {self.damage} damage')


class Pistol(Gun):
    def __init__(self, name, damage, multiplier, reload_speed, mag_size, rarity):
        super().__init__(self, name, damage, reload_speed, mag_size, rarity)
        self.multiplier = multiplier


class SubMachineGun(Gun):
    def __init__(self, name, damage, multiplier, reload_speed, mag_size, rarity):
        super().__init__(self, name, damage, reload_speed, mag_size, rarity)
        self.multiplier = multiplier


class AssaultRifle(Gun):
    def __init__(self, name, damage, multiplier, reload_speed, mag_size, rarity):
        super().__init__(self, name, damage, reload_speed, mag_size, rarity)
        self.multiplier = multiplier


class Shotgun(Gun):
    def __init__(self, name, damage, multiplier, reload_speed, mag_size, rarity):
        super().__init__(self, name, damage, reload_speed, mag_size, rarity)
        self.multiplier = multiplier


class SniperRifle(Gun):
    def __init__(self, name, damage, multiplier, reload_speed, mag_size, rarity):
        super().__init__(self, name, damage, reload_speed, mag_size, rarity)
        self.multiplier = multiplier


class RocketLauncher(Gun):
    def __init__(self, name, damage, multiplier, reload_speed, mag_size, rarity):
        super().__init__(self, name, damage, reload_speed, mag_size, rarity)
        self.multiplier = multiplier


weapon_type_list = (Pistol, SubMachineGun, AssaultRifle, Shotgun, SniperRifle, RocketLauncher)

damage_multiplier_dict = {
    0: 1,
    1: .75,
    2: 1.3,
    3: 3,
    4: 6,
    5: 10
}


def determine_weapon_type():
    weapon_type = random.randint(0, (len(weapon_type_list) - 1))
    return weapon_type


def create_gun():
    weapon_type = determine_weapon_type()

    weapon = None

    if weapon_type == 0:
        weapon = Pistol()

    elif weapon_type == 1:
        weapon = SubMachineGun()

    elif weapon_type == 2:
        weapon = AssaultRifle()

    elif weapon_type == 3:
        weapon = Shotgun()

    elif weapon_type == 4:
        weapon = SniperRifle()

    elif weapon_type == 5:
        weapon = RocketLauncher()


create_gun()
