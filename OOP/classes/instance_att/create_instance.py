class Config:     
    pass

def create_instance(n: int) -> Config:
    obj = Config()
    for value in range(1, n+1):
        setattr(obj, f'attribute{value}', f'value{value}')
    return obj

config_2 = create_instance(2)
print(config_2.__dict__)

config_4 = create_instance(4)
config_3 = create_instance(3)
config_2 = create_instance(2)
print(config_4.__dict__)
print(config_3.__dict__)
print(config_2.__dict__)