import string

with open("CustomsDec.txt", "r") as file:
    treb = ""
    farray = []
    for line in file:
        line = line.strip()
        if line != '':
            treb += line
        else:
            farray.append(treb)
            treb = ""
        treb += ' '
count = 0
print(farray)
for line in farray:
    line = line.strip().replace(" ", "")
    frb = ""
    for ch in line:
        if ch not in frb:
            # print(ch)
            frb += ch
    count += len(frb)
print(count)
count = 0
# p2

for line in farray:
    frb = ""
    line = line.strip()
    dic = {charr:0 for charr in string.ascii_lowercase}
    split = line.split()
    frb = split[0]
    for elem in split:
        elem = elem.strip()
        for ch in elem:
            dic[ch] += 1
    for letter in dic:
        if dic[letter] == len(split):
            count += 1
print(count)
# dictionaries kinda epic though