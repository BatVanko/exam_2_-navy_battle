def find_submarine_position(matrx):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrx[i][j] == 'S':
                return i, j


def move_positions():
    positi = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }
    return positi


size_field = int(input())
matrix = []
for _ in range(size_field):
    matrix.append([x for x in input()])
naval_mine = '*'
battle_cruiser = 'C'  # marked with '-' (dash) battle cruisers 3
counter_hits_from_naval_mines = 0  # 3d boooom  return last position
counter_hits_battle_cruiser = 0  # 3d win :)
positions = move_positions()
current_row, current_col = find_submarine_position(matrix)
matrix[current_row][current_col] = '-'

while True:
    command = input()
    next_row_idx, next_co_idx = positions[command]
    next_row = current_row + next_row_idx
    next_col = current_col + next_co_idx
    matrix[current_row][current_col] = '-'
    current_place = matrix[next_row][next_col]
    if current_place == naval_mine:
        counter_hits_from_naval_mines +=1
        current_place = '-'
    elif current_place == battle_cruiser:
        counter_hits_battle_cruiser +=1
        current_place = '-'
    if counter_hits_from_naval_mines == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{next_row}, {next_col}]!")
        matrix[next_row][next_col] = 'S'
        break
    if counter_hits_battle_cruiser == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        matrix[next_row][next_col] = 'S'
        break
    current_row, current_col = next_row, next_col
    matrix[current_row][current_col] = 'S'



for row in matrix:
    print(''.join(row))

