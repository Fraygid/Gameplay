class Monster:
    def __init__(self, name = "Неизвестная тварь", hp = 100, dmg = 10):
        self.name = name
        self.hp = hp
        self.dmg = dmg

        print(f'Монстр:{self.name}')
        print(f'HP:{self.hp}')
        print(f'DMG:{self.dmg}')
        print()


line1 = input('Введите имя, хп, и урон монстра: ').split()
line2 = input('Введите имя, хп, и урон монстра: ').split()

dracula = Monster(line1[0], int(line1[1]), int(line1[2]))
lycan = Monster(line2[0], int(line2[1]), int(line2[2]))
