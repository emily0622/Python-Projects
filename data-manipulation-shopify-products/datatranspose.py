import pandas as pd

df = pd.read_csv(r"C:\\Users\\User\\Desktop\\Python-Projects\\Fetching-Stores.csv", encoding= 'unicode_escape')
print(df)

# for meep in df['product-name']:
#     print(meep)

# # I MIGHT NEED THIS LATER...?
# new_product_name = []
# for item in df['product-name']:
#     new_item = ""
#     # print(item)
#     for i in range(len(item)):
#         if item[i] == " " or "(" or ")" or "/" or "\"" or "&":
#             new_item += "-"
#         else:
#             new_item += item[i]
#     new_product_name.append(new_item)

# print(new_product_name)


#if size configuration = TRUE then skkip x lines




vendor = []
vendorInput = ['U of T Engineering Stores']
published = []
publishedInput = []
option1Name = []
option1NameInput = ['size']
option1Value = []
option1ValueInput = ['XS','S','M','L','XL','2XL']
variantInventory = []
variantInventoryHeadings = ['inventory_count_xs','inventory_count_s','inventory_count_m','inventory_count_l','inventory_count_xl','inventory_count_2xl']
productPrice = []
for num in range(len(df['size_configuration'])):
    if df['size_configuration'][num] == True:
        if df['inventory_count'][num] == 0:
            published.append('False')
        elif df['inventory_count'][num] != 0:
            published.append('True')
        else:
            published.append('error')

        price = df['product_price'][num]

        for sizes in range(6):
            vendor.append(vendorInput[sizes])
            variantInventory.append(df[variantInventoryHeadings][sizes][num])
            productPrice.append(price)


        vendor.append(vendorInput)
        option1Name.append(option1NameInput)
        for emptyString in range(len(5)):
            vendor.append('')
            option1Name.append('')
        
        # if size config = TRUE and inventory_count != 0

    for i in range(len(item)):
        if item[i] == " " or "(" or ")" or "/" or "\"" or "&":
            new_item += "-"
        else:
            new_item += item[i]
    new_product_name.append(new_item)


# DataFrameName.insert(loc, column, value, allow_duplicates = False)

