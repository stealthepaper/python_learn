class Hero:
    damage = 100

print(Hero.__dict__)
delattr(Hero, 'damage')
print(Hero.__dict__)