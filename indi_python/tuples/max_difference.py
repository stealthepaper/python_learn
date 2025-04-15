players = [("Alice", 10), ("Bob", 15), ("Charlie", 20), ("Dave", 25)]
max_difference = 6
for i in range(len(players)):
    print(players[i])
    for j in range(i+1, len(players)):
        print(f' j = {players[j]}')
        if j > i:
            print()