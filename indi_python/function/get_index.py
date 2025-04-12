def get_body_mass_index(w, h):
    body_index = w/(h/100)**2
    # print(body_index)
    if body_index < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 <= body_index <= 25:
        print('Норма')
    elif body_index > 25:
        print('Избыточная масса тела')

get_body_mass_index(70, 170)
get_body_mass_index(90, 180)
get_body_mass_index(40, 160)