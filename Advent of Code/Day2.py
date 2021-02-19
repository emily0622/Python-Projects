def processing():
    file_name = "elfpasswords"
    with open(file_name, "r") as f:
        passwords = f.readlines()
    num_of_correct_passwords = 0
    for password in passwords:
        password = password.replace('\n',"")
        password = password.replace(':', "")
        range, letter, check = password.split(" ")
        minimum, maximum = range.split("-")
        num_of_correct_passwords += day2q2(minimum, maximum, letter, check)
    return num_of_correct_passwords



def day2q1(minimum, maximum, letter, check):
   #time to check
    actual = check.count(letter)
    if ((actual <= int(maximum)) & (actual >= int(minimum))):
        return 1
    else:
        return 0


def day2q2(minimum, maximum, letter, check):
    if check[int(minimum) - 1] == letter:
        minimum = True
    else:
        minimum = False
    if check[int(maximum) - 1] == letter:
        maximum = True
    else:
        maximum = False
    return minimum ^ maximum


if __name__ == '__main__':
    print(processing())
    #print(day2q2(1,2,'a','aac'))