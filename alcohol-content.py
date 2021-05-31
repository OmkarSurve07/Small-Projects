'''
Program to calculate alcohol-contain in body .
We create class "bac" and in that class we contain 5 objects to calculate the alcohol capacity .
'''

class bac(object):
    def __init__(self, weight, time, vol, amount, gender):
        self.weight = weight
        self.time = time
        self.vol = vol
        self.amount = amount
        self.gender = gender
        self.std = 0.0068
    
    def standerd_drink(self):
        return round((self.std * self.vol) * self.amount, 2)

    def promille_man(self):
        return round((self.standerd_drink() * 12) / ((self.weight * 1.7) - (0.15 * self.time)), 2)
    
    def promille_woman(self):
        return round((self.standerd_drink() * 12) / ((self.weight * 1.6) - (0.15 * self.time)), 2)

    def result(self):
        if self.gender == 'woman':
            print(f'\nAs a woman who have had {self.amount} cl. of {self.vol}% vol, {self.time} hours ago.')
            print(f'You`ve had {self.standerd_drink()} drinks, which give you a {self.promille_woman()}% bac\n')
        elif self.gender == 'man':
            print(f'\nAs a woman who have had {self.amount} cl. of {self.vol}% vol, {self.time} hours ago.')
            print(f'You`ve had {self.standerd_drink()} drinks, which give you a {self.promille_man()}% bac\n')
        else:
            print('Fault.')

danny = bac(80, 1, 4.6, 33, 'man')
dolly = bac(55, 6, 14, 70, 'woman')

danny.result()
dolly.result()