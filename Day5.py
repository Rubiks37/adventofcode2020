with open("BoardingPasses.txt", "r") as file:
    ido = 0
    id_list = []
    for line in file:
        lower_row = 0
        upper_row = 128
        lower_col = 0
        upper_col = 8
        for char in line:
            if char == 'F':
                upper_row = (upper_row + lower_row)/2
            elif char == 'B':
                lower_row = (upper_row + lower_row)/2
            elif char == "R":
                lower_col = (upper_col + lower_col)/2
            elif char == 'L':
                upper_col = (upper_col + lower_col)/2
        fr = ((lower_row*8)+lower_col)
        id_list.append(fr)
        if fr > ido:
            ido = fr
print(ido)
# Part one done, slightly easier than I imagined, part 2 should be painful as always
id_list.sort()
print(id_list)
num = 78
for elem in id_list:
    if elem != num:
        print(elem-1)
        num+=1
    num += 1