class Person:
    can_fly = False
    can_walk = True


jim = Person()
jim.can_swim = True
print(jim.__dict__)
print()
peter = Person()
print(peter.__dict__)