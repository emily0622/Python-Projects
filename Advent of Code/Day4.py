
#count number of valid passports and "North pole credentials" which have all field except cid
#all 8 fields: byr, iyr, eyr, hgt, hcl, ecl, pid, cid
#going to assume 8 fields doesn't mean the required fields are present
#also going to make sure the fields match

#1) separate variables in processing function
#2) processing calls function to check variables

def processing():
    file_name = "passport_info"
    valid_passport_count = 0
    valid_data_count = 0
    with open(file_name, "r") as f:
        lines = f.readlines()
    elements = ""
    for line in lines:
        if line != '\n':
            #the commented code separates into a list
            # elements = line.replace('\n', " ").split(" ")
            # elements = list(filter(None, elements)) #filter returns an iterator so should be wrapped in a call to list()
            # passport += elements
            elements += line.replace('\n'," ")
        else:
            valid_passport,valid_data = day4q1andq2(elements)
            valid_passport_count += valid_passport
            valid_data_count +=  valid_data
            elements = ""
    return valid_passport_count, valid_data_count


def day4q1andq2(p):
    #checks all field except cid
    valid_fields = p.count('byr') & p.count('iyr') & p.count('eyr') \
             & p.count('hgt') & p.count('hcl') & p.count('ecl') & p.count('pid')
    valid_data = 0
    if valid_fields == 1:
        field_dict = {}
        element_list = p.split(" ")
        element_list = list(filter(None, element_list)) #filter returns an iterator so should be wrapped in a call to list()
        for element in element_list:
            match = element.split(':')
            field_dict[match[0]] = match[1]
        valid_data = 1
        field_1 = ((int(field_dict['byr']) >= 1920) & (int(field_dict['byr']) <= 2002) & (len(field_dict['byr']) == 4))
        if field_1 == 0:
            return [valid_fields, 0]

        field_2 = ((int(field_dict['iyr']) >= 2010) & (int(field_dict['iyr']) <= 2020) & (len(field_dict['iyr']) == 4))
        if field_2 == 0:
            return [valid_fields, 0]

        field_3 = ((int(field_dict['eyr']) >= 2020) & (int(field_dict['eyr']) <= 2030) & (len(field_dict['eyr']) == 4))
        if field_3 == 0:
            return [valid_fields, 0]

        unit = field_dict['hgt'][-2:]
        num = field_dict['hgt'][:-2]
        field_4 = 0
        if num.isdigit():
            if unit == 'cm':
                if (((int(num)>=150)) & (int(num)<=193)):
                    field_4 = 1
            if unit == 'in':
                if ((int(num)>=59) & (int(num)<=76)):
                    field_4 = 1
        if field_4 == 0:
            return [valid_fields, 0]

        code = field_dict['hcl']
        field_5 = 0
        if ((code[0] == '#') & (len(code) == 7)):
            for i in code[1:]:
                print("i", i)
                print('ord', ord(i))
                if (((ord(i) >= 97) & (ord(i) <= 102)) | ((ord(i)>=48) & (ord(i) <= 57))): # is this 0-9
                    field_5 = 1
                else:
                    field_5 = 0
                    break

        print(field_dict['hcl'])
        print(field_5)
        if field_5 == 0:
            return [valid_fields, 0]

        valid_colour = 'amb blu brn gry grn hzl oth'.count(field_dict['ecl'])
        field_6 = (valid_colour & 1) #to ensure it is only one colour
        if field_6 == 0:
            return [valid_fields, 0]

        valid_num = 1
        for x in field_dict['pid']:
            if ((ord(x) < 48) & (ord(x) > 57)):
                valid_num = 0
                break
        field_7 = (((len(field_dict['pid'])) == 9) & valid_num)
        if field_7 == 0:
            return [valid_fields, 0]

        #valid_data = field_1 & field_2 & field_3 & field_4 & field_5 & field_6 & field_7
    return [valid_fields, valid_data]


if __name__ == '__main__':
    print(processing())