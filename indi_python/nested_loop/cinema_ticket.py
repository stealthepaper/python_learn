# Программа должна: 
# обрабатывать список забронированных мест booked, в котором хранятся строки в формате "Р.<ряд>, М.<место>";
# Выводить на экран схему рассадки:
# В зале 5 рядов. В каждом ряду 10 мест.
# Если место забронировано, на его позиции должно стоять "X", иначе "O".

# booked = ["Р.1, М.2", "Р.2, М.5", "Р.3, М.1", "Р.4, М.7", "Р.5, М.10"]
# booked = ["Р.1, М.1", "Р.1, М.2", "Р.1, М.3", "Р.2, М.1", "Р.5, М.10"]
booked = []
for i in range(1, 6):
    for j in range(1, 11):
        if f"Р.{i}, М.{j}" in booked:
            print('X', end=' ')
        else:
            print('O', end=' ')
    print()

    
# rows = 5 
# seats = 10  
# theater = [["O" for _ in range(seats)] for _ in range(rows)]
# for item in booked:
#     row, seat = item.split(", ") 
#     row_num = int(row.split(".")[1]) - 1
#     seat_num = int(seat.split(".")[1]) - 1
#     theater[row_num][seat_num] = "X"
# for row in theater:
#     print(" ".join(row)) 