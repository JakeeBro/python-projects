class User:
    def __init__(self, email):
        self.email = email

    @staticmethod
    def sign_in():
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')

    @staticmethod
    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows, email):
        Archer.__init__(self, name, num_arrows, email)
        Wizard.__init__(self, name, power, email)


wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
archer1 = Archer('Robin', 30, 'robin@gmail.com')
hb1 = HybridBorg('Borg', 45, 50, 'borgie@gmail.com')


# def player_attack(character):
#     character.attack()


print(hb1.attack())
