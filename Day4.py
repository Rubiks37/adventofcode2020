# helphelphelphelphelp
with open("PassportBatch.txt", "r") as file:
    greg = ""
    fu_array = []
    for line in file:
        line = line.strip()
        if line != '':
            greg += line
        else:
            fu_array.append(greg)
            greg = ""
        greg += ' '
count = 0
temp_count = 0
gregg = []
valid_pass = []
i_hate = False
boll = False
for passp in fu_array:
    temp_list = passp.split()
    good_list = [gregory.split(":") for gregory in temp_list]
    if len(good_list) == 8:
        valid_pass.append(good_list)
    elif len(good_list) == 7:
        gregg = [gerg[0] for gerg in good_list]
        for letters in gregg:
            if letters == 'cid':
                boll = True
        if not boll:
            valid_pass.append(good_list)
        boll = False
        # pain and suffering why
print(valid_pass)
# ah
for line in valid_pass:
    temp_count = 0
    for elem in line:
        if elem[0] == 'byr':
            if 1920 <= int(elem[1]) <= 2002:
                temp_count += 1
        elif elem[0] == 'iyr':
            if 2010 <= int(elem[1]) <= 2020:
                temp_count += 1
        elif elem[0] == 'eyr':
            if 2020 <= int(elem[1]) <= 2030:
                temp_count += 1
        elif elem[0] == 'hgt':
            if elem[1].endswith('cm'):
                num = int(elem[1][0: -2])
                if 150 <= num <= 193:
                    temp_count += 1
            elif elem[1].endswith('in'):
                num = int(elem[1][0: -2])
                if 59 <= num <= 76:
                    temp_count += 1
        elif elem[0] == 'hcl':
            i_hate = False
            if elem[1][0] == '#':
                for gr in elem[1][1:]:
                    if not gr in "1234567890abcdef":
                        i_hate = True
            else:
                i_hate = True
            if not i_hate:
                temp_count += 1
        elif elem[0] == 'ecl':
            if elem[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                temp_count += 1
        elif elem[0] == 'pid':
            if elem[1].isdigit() and len(elem[1]) == 9:
                temp_count += 1
    if temp_count == 7:
        count += 1



print(count)