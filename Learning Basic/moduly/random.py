import random

#members = ['John', 'Merry', ' Kayle', ' Endriu']
# print(random.choice(members))


class Dice:

    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y


dice = Dice()
print(dice.roll())
