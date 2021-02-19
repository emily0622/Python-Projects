
def day1q1():
    file_name = "elfaccounts"
    with open(file_name, "r") as f:
        data_elfaccounts = f.readlines()
   #     length_of_list = len(data_elfaccounts) -1
    x = 0 #goal is for x=2020
    for item_1 in data_elfaccounts:
        item1 = int(item_1.replace('\n',""))
        for item_2 in data_elfaccounts:
            item2 = int(item_2.replace('\n', ""))
            x = item1+item2
            if x == 2020:
                product = item1*item2
                print("item1: " + str(item1) + ", item2: " + str(item2) + ", product: " + str(product))
                return(item1*item2)
    return False

def day1q2():
    file_name = "elfaccounts"
    with open(file_name, "r") as f:
        data_elfaccounts = f.readlines()
   #     length_of_list = len(data_elfaccounts) -1
    x = 0 #goal is for x=2020
    for item_1 in data_elfaccounts:
        item1 = int(item_1.replace('\n',""))
        for item_2 in data_elfaccounts:
            item2 = int(item_2.replace('\n', ""))
            for item_3 in data_elfaccounts:
                item3 = int(item_3.replace('\n', ""))
                x = item1+item2+item3
                if x == 2020:
                    product = item1*item2*item3
                    print("item1: " + str(item1) + ", item2: " + str(item2) + ", item3: " + str(item3) + ", product: " + str(product))
                    return(item1*item2*item3)

if __name__ == '__main__':
    #day1q1()
    day1q2()