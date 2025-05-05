class Hero:
    pass

batman = Hero()
batman.can_fly = False
batman.damage = 175

superman = Hero()
superman.can_fly = True
superman.damage = 285
superman.alter_ego = 'Кларк Кент'

print(batman.__dict__)
print()
print(superman.__dict__)