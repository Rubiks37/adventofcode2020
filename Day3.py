file = open("map.txt", "r")
# this is literally so dumb why id this nesessarcyvtruihg
filearray = []
for g in file:
    filearray.append(g)
# This seems like death, we'll figure it out im sure


def hit(offset):
    across = 0
    count = 0
    for i in filearray:
        i = i.strip()
        if across >= len(i):
            across -= len(i)
        if i[across] == "#":
            count += 1
        across += offset
    return count


def bane_of_existence():
    across = 0
    down = True
    count = 0
    for i in filearray:
        if down:
            i = i.strip()
            if across >= len(i):
                across -= len(i)
            if i[across] == "#":
                count += 1
            across += 1
        down = not down
    return count


print(hit(1))
print(hit(3))
print(hit(5))
print(hit(7))
print(bane_of_existence())
print(hit(1)*hit(3)*hit(5)*hit(7)*bane_of_existence())
file.close()
