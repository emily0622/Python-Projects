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
status = []
option1Name = []
option1Value = []
option1ValueInput = ['XS','S','M','L','XL','2XL']
variantInventory = []
variantInventoryHeadings = ['inventory_count_xs','inventory_count_s','inventory_count_m','inventory_count_l','inventory_count_xl','inventory_count_2xl']
productPrice = []
for num in range(len(df['size_configuration'])):
    if df['inventory_count'][num] == 0:
            published.append(False)
            status.append('active')
    elif df['inventory_count'][num] != 0:
        published.append(True)
        status.append('draft')
    else:
        published.append('error')
        status.append('error')

    price = df['product_price'][num]
    productPrice.append(price)
    vendor.append(vendorInput)


    if df['size_configuration'][num] == True:
        option1Name.append('size')
        for sizes in range(6):
            option1Value.append(option1ValueInput[sizes])
            variantInventory.append(df[variantInventoryHeadings][sizes][num])
                    
        for emptyString in range(len(5)):
            productPrice.append(price)

            vendor.append('')
            option1Name.append('')
        
        # if size config = TRUE and inventory_count != 0




# DataFrameName.insert(loc, column, value, allow_duplicates = False)

