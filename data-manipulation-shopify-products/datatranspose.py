import pandas as pd
import csv

# CSV files may lose data when exported for excel, so it is better to use .xlsx
df = pd.read_excel(r"C:\\Users\\User\\Desktop\\Python-Projects\\Fetching-Stores.xlsx")
print(df)

# for meep in df['product_name']:
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

productWeightDict = {
440: ['Industrial Quarter Zip (Grey)','Industrial Quarter Zip (Navy)','Navy Blue SkuleTM 1/4-Zip','SkuleTM 1/4-Zip',"Eng S'mores Fall 1/4-Zip - Graphite",'Eng Smores Fall 1/4-Zip - Dark Grey','Eng Smores Fall 1/4-Zip - Graphite',"Eng S'mores Fall 1/4-Zip - Dark Grey"], 
187:['"Lean Mean Indy Machine" T-Shirt (White)','"Lean Mean Indy Machine" T-Shirt (Black)','Lean Mean Indy Machine T-Shirt (White)','Lean Mean Indy Machine T-Shirt (Black)','UofMeg x Stores "Utility Green"','UofMeg x Stores "The Godiva"','UofMeg The Godiva'],
460: ['Burgundy SkuleTM Hoodie','SkuleTM Retro Hoodie (White)','SkuleTM Retro Hoodie (Grey)','SkuleTM Retro Hoodie (Navy)'], 280: ['SkuleTM Retro Sweats (Grey)','SkuleTM Retro Sweats (Navy Blue)'],
46: ['Eng Socks','EngSoc Ties','EngSoc Tie'], 80: ['Iron Dragon Toque','MSE Toque','Navy Blue Toque','Retro White Toque'], 86: ['Grey Toque w/Pompom'],77: ['Skule Baseball Hat'],88: ['Bucket Hat','SkuleTM Bucket Hat'],
160: ['UofT Eng Shirt (Red)','UofT Eng Shirt (Black)','UofT Eng Shirt (Grey)','Movember Skule Shirt','Skule Shirt (Red)','Skule Shirt (Pink)','Skule Shirt (Black)','Skule Shirt (Grey)',
'Skule Shirt (Navy Blue)','Skule Shirt (Purple)','Skule Shirt (Orange)','Skule Shirt (Baby Blue)','UofMeg x Stores "Purple Dye Explosion"','UofMeg Purple Dye Explosion','UofMeg x Stores Tie-Dye T-Shirt - Red','Lady Godiva Memorial Band T-shirt Black','BNAD/LGMB Shirt (Blue)','BNAD/LGMB Shirt (Black)',
'Lady Godiva Memorial Band Jersey','Skule Cannon Shirt (Black)','Skule Cannon Black T-shirt','Toike Oike Shirt (Black)','Toike Oike Black T-shirt "No One Cares About My Degree"','Toike Oike White T-shirt','Toike Oike Shirt (White)','SKULE Kup T-shirt','"Hug Me I\'m User friendly " Shirt (Black)','Hug Me I\m User Friendly T-Shirt (Red)',
'Blue and Gold Baseball Tee','"Hug Me I\'m User friendly " Shirt (Red)','HRP Black Shirt','Black SUDS Shirt','Concrete Toboggan Grey Shirt','Keep Calm and optimize'],
213: ['Hi-Skule Baseball Tee','Red Cannon Polo'], 360: ['Engineering Crewneck (Grey)','Engineering Crewneck (Green)'], 300: ['SkuleTM Retro Windbreaker'],381: ['Mech Eng "Friends" Crewneck (Grey)','Mech Eng Friends Crewneck (Grey)','Mech Eng Friends Crewneck (Black)','Civil Eng Crewneck (Navy)','Civil Eng Hoodies (Red)','Civil Eng Hoodie (Red)'],
280: ['Industrial Eng Crewneck (Navy)','Industrial Eng Crewneck (Grey)'],353: ['Wb Element 1/4 Zip'],120: ['Mech Eng Shirt, "Super Mech"','Mech Eng Shirt, Super Mech'],
130: ['I Love Mechanical Engineering Shirt','Straight Outta Mech Shirt','Track One 2019 Shirt (Coloured Balls)','Track One Shirt (Black)','ECE Shirt','Material Science Engineering Shirt','Engineering Science  Shirt',
'Civil Shirt (Red)','Civil Eng Shirt (White)','Civil Eng Shirt (Navy)','Civil Eng Shirt (Navy Blue)','SKULE Coveralls','Coveralls','"In Skule We Truss" Shirt'],400: ['CheMech Scrabble Sweater Black','CheMech Scrabble Sweater Carolina Blue']
}



vendor = []
published = []
status = []
option1Name = []
option1Value = []
option1ValueInput = ['XS','S','M','L','XL','2XL']
variantInventory = []
variantInventoryHeadings = ['inventory_count_xs','inventory_count_s','inventory_count_m','inventory_count_l','inventory_count_xl','inventory_count_2xl']
productPrice = []
productName = []
productDescription = []
productType = []
productTypeDict = {}
productTags = []
productWeight = []
imageSrc = []
imageRank = []
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
    vendor.append('U of T Engineering Stores')
    name = df['product_name'][num]
    productName.append(name)
    desc = df['product_desc'][num]
    productDescription.append(desc)
    ptype = df['product_type'][num]
    productType.append(ptype)
    tag = name + ' ' + desc + ' ' + str(ptype)
    productTags.append(tag)
    imageSrc.append(df['image'][num])
    imageRank.append(1)
    
    pweight = 0
    for weight, article in productWeightDict.items():
        for item in article:
     
            if item == name:
                pweight = weight
                pass

    productWeight.append(pweight)


    if df['size_configuration'][num] == True:
        option1Name.append('size')
        for sizes in range(6):
            option1Value.append(option1ValueInput[sizes])
            variantSizeString = variantInventoryHeadings[sizes]
            variantInventory.append(df[variantSizeString][num])
                    
        for emptyString in range(5):
            productPrice.append(price)
            vendor.append('')
            option1Name.append('')
            published.append('')
            status.append('')
            productName.append('')
            productDescription.append('')
            productType.append('')
            productTags.append('')
            productWeight.append('')
            imageSrc.append('')
            imageRank.append('')
    else:
        variantInventory.append(df['inventory_count'][num])
        option1Name.append('')
        option1Value.append('')
        
        # if size config = TRUE and inventory_count != 0


# for i in range(len(productWeight)):
#     print(productName[i])
#     print(productWeight[i])


# for i in range(len(productWeight)):
#     if productName[i].find('atch') == -1:
#         if productWeight[i] == 0:
#             print(productName[i])




exportingData = pd.DataFrame({'Title': productName, 'Body (HTML)' : productDescription, 'Vendor': vendor, 'Type': productType, 'Tags': productTags, 'Published': published,'Option1 Name': option1Name,
'Option1 Value': option1Value, 'Variant Grams': productWeight, 'Variant Inventory': variantInventory, 'Variant Price': productPrice, 'Image Src': imageSrc, 'Image Position': imageRank})

exportingData.to_csv("exportedData.csv")

# find coversion for product type

# Handle	Title	Body (HTML)	Vendor	Type	Tags	Published	
# Option1 Name	Option1 Value	Option2 Name	Option2 Value	
# Option3 Name	Option3 Value	Variant SKU	Variant Grams	
# Variant Inventory Tracker	Variant Inventory Qty	Variant Inventory
#  Policy	Variant Fulfillment Service	Variant Price	Variant Compare 
#  At Price	Variant Requires Shipping	Variant Taxable	Variant 
#  Barcode	Image Src	Image Position	Image Alt Text	Gift Card	
#  SEO Title	SEO Description	Google Shopping / Google Product Category
# Google Shopping / Gender	
# Google Shopping / Age Group	Google Shopping / MPN	
# Google Shopping / AdWords Grouping	Google Shopping / AdWords Labels	
# Google Shopping / Condition	
# Google Shopping / Custom Product	
# Google Shopping / Custom Label 0	
# Google Shopping / Custom Label 1	
# Google Shopping / Custom Label 2	
# Google Shopping / Custom Label 3	
# Google Shopping / Custom Label 4	
# Variant Image	Variant Weight Unit  Variant Tax Code	
# Cost per item	Status