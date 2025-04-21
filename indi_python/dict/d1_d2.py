d1 = {'India': 'Delhi',
      'Canada': 'Ottawa',
      'United States': 'Washington D. C.'}

d2 = {'France': 'Paris',
      'Malaysia': 'Kuala Lumpur'}
#{'India': 'Delhi', 'Canada': 'Ottawa', 'United States': 'Washington D. C.', 'France': 'Paris', 'Malaysia': 'Kuala Lumpur'}

#{'Brazil': 'Brasilia', 'Argentina': 'Buenos Aires', 'Peru': 'Lima', 'Chile': 'Santiago'}
# d1 = {"Brazil": "Brasilia", "Argentina": "Buenos Aires", "Peru": "Lima"}     
# d2 = {"Argentina": "Córdoba", "Chile": "Santiago", "Peru": "Cusco"}   
combinated = {**d1, **d2, **d1}
print(combinated)