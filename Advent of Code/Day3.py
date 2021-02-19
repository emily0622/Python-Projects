#transform into array
#counting function that calls maneuver function
#maneuver function accounts for reaching the boarder

def processing():
    file_name = "map"
    with open(file_name, "r") as f:
        rows = f.readlines()
    map = []
    row_number = 0
    for row in rows:
        map.append([])
        row_number += 1
        for i in range(len(row)-1):
            map[row_number-1].append(row[i])
    return map


def day3q1(right,down):
    map = processing()
    tree_count = 0
    position = [0,0] #starting position (row,column)
    row_max = len(map)
    print("max trees:")
    print(row_max)
    column_max = len(map[0])
    #maneuver is +3 columns, + 1 row
    while (position[0] < (row_max - 1)):
        if (position[1] + right >= column_max):
            position[1] += right - column_max
        else:
            position[1] += right
        position[0] += down
        if map[position[0]][position[1]] == '#':
            tree_count += 1
    return tree_count

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

if __name__ == '__main__':
    print(day3q1(1,1) * day3q1(3,1) * day3q1(5,1) * day3q1(7,1) * day3q1(1,2))