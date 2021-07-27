class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Tigger', 7.25)
cat2 = Cat('Baby Kitty', 7.24)
cat3 = Cat('Buddy', 4.55)
cat4 = Cat('Peanut', 4.54)


def get_oldest_cat(*args):
    return max(args)


print(f'The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age, cat4.age)} years old.')
