# Time to scuff this shit
file = open("Passwords.txt", "r")
num1 = 0
num2 = 0
count1 = 0
count2 = 0
hyphn = False
mod = False
# I can't be fucked trying to do this better
for i in file:
    line = i.split(':')
    modifier = line[0]
    modifier.strip()
    for x in modifier:
        if x.isdigit():
            if not hyphn:
                if num1 == 0:
                    num1 = int(x)
                elif num1 < 10:
                    num1 = num1 * 10 + int(x)
            elif num2 == 0:
                num2 = int(x)
            elif num2 < 10:
                num2 = num2 * 10 + int(x)
        elif x.isalpha():
            letter = str(x)
            mod = True
            # WHY IS THIS NOT RUNNING
            # oh it works
        else:
            hyphn = True
    if mod:
        password = line[1]
        password.strip()
        co = password.count(letter)
        # This is stupid but it works whatever
        if num1 <= co <= num2:
            count1 = count1 + 1
        # That's part one, part 2 code should be the same thing except weirder now that I have num1 and 2 isolated
        if password[num1] == letter:
            if not password[num2] == letter:
                count2 = count2 + 1
                print("Pw: " + password + " Letter: " + letter + " N1: " + str(num1))
        elif password[num2] == letter:
            count2 = count2 + 1
            print("Pw: " + password + " Letter: " + letter + " N2: " + str(num2))
        else:
            print("Pw: " + password)
        # pain and suffering
        # answer is 711 beautiful
    hyphn = False
    num1 = 0
    num2 = 0
print(count1)
print(count2)
# Count is 515, got it right lfg that's part 1



