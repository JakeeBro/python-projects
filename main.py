class PlayerCharacter:
    """
    Player Character Class
    Holds Character Name and Age
    """
    membership = True

    def __init__(self, name, age):
        if age > 18:
            self._name = name
            self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name}, and I am {self._age} years old')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


def display_character(character_name):
    print(f'Player \'{character_name}\' has joined the game')


player1 = PlayerCharacter('Jake', 21)
display_character(player1.name)
