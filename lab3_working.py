def rotate_90_degrees(image_array, direction):
    # 1 for clock_wise. -1 for anticlockwise
    num_rows = len(image_array)
    num_columns = len(image_array[0])
    x = 0
    matrix = []
    while x < num_columns:
        x += 1
        matrix.append([])
    for i in range(num_columns):
        for y in range(num_rows):
            matrix[i].append(0)

    for row_index in range(num_rows):
        for column_index in range(num_columns):
            number1 = num_rows - row_index
            number2 = num_columns - column_index
            if direction == 1:
                matrix[column_index][number1 - 1] = image_array[row_index][column_index]
            elif direction == -1:
                matrix[number2 - 1][row_index] = image_array[row_index][column_index]
            else:
                request = 'please specifiy a direction'
                return request
    return matrix

def flip_image(image_array, axis):
    num_rows = len(image_array)
    num_columns = len(image_array[0])
    matrix = []
    for x in range(num_rows):
        matrix.append([])
    for i in range(num_rows):
        for y in range(num_columns):
            matrix[i].append(0)
    if axis == 0:  # flip about y axis
        for row_index in range(num_rows):
            for column_index in range(num_columns):
                number2 = num_columns - 1 - column_index
                matrix[row_index][number2] = image_array[row_index][column_index]
    elif axis == 1: #flip about x axis
        for row_index in range(num_rows):
            for column_index in range(num_columns):
                number1 = num_rows - 1 - row_index
                matrix[number1][column_index] = image_array[row_index][column_index]
    elif axis == -1: #flip about y=x
        for row_index in range(num_rows):
            for column_index in range(num_columns):
                number1 = num_rows - 1 - row_index
                number2 = num_columns - 1 - column_index
                matrix[number2][number1] = image_array[row_index][column_index]
    else:
        matrix = 'please specify a direction'
    return matrix

def invert_grayscale(image_array):
    num_rows = len(image_array)
    num_columns = len(image_array[0])
    matrix = []
    for x in range(num_rows):
        matrix.append([])
    for i in range(num_rows):
        for y in range(num_columns):
            matrix[i].append(0)
    for row_index in range(len(image_array)):
        for column_index in range(len(image_array[0])):
            matrix[row_index][column_index] = (255 - image_array[row_index][column_index])
    return matrix

def crop(image_array, direction, n_pixels):
    #CREATE 0 MATRIX
    #step 1 figure out the number of rows and columns for new 0 matrix
    if direction == 'up' or direction == 'down':
        num_rows = (len(image_array) - n_pixels)
        num_columns = len(image_array[0])
    elif direction == 'right' or direction == 'left':
        num_rows = len(image_array)
        num_columns = (len(image_array[0]) - n_pixels)
    else:
        num_rows = 0
        num_columns = 0
    #step 2 create matrix
    matrix = []
    for x in range(num_rows):
        matrix.append([]) #append the number of rows for cropped image
    for i in range(num_rows):
        for y in range(num_columns):
            matrix[i].append(0) #append the number of columns for cropped image

    #assign matrix values!
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[0])):
            if direction == 'up':
                #goes through matrix in regular order but assign the intended pixel (as in if you are cropping left, index to this pixel
                matrix[row_index][column_index] = image_array[row_index + n_pixels][column_index]
            elif direction == 'down':
                matrix[row_index][column_index] = image_array[row_index][column_index]
            elif direction == 'left':
                matrix[row_index][column_index] = image_array[row_index][column_index + n_pixels]
            elif direction == 'right':
                matrix[row_index][column_index] = image_array[row_index][column_index]
            else:
                matrix = []
    return matrix

def rgb_to_grayscale(rgb_image_array):
    num_rows = len(rgb_image_array)
    num_columns = len(rgb_image_array[0])
    matrix = []
    for x in range(num_rows):
        matrix.append([])
    for i in range(num_rows):
        for y in range(num_columns):
            matrix[i].append(0)
    for row_index in range(len(rgb_image_array)):
        for column_index in range(len(rgb_image_array[0])):
            gray_r = rgb_image_array[row_index][column_index][0] * 0.2989
            print(row_index)
            print(column_index)
            print(rgb_image_array[row_index][column_index][1])
            gray_g = rgb_image_array[row_index][column_index][1] * 0.5870
            gray_b = rgb_image_array[row_index][column_index][2] * 0.1140
            gray = gray_r + gray_g + gray_b
            matrix[row_index][column_index] = gray
    return matrix

def invert_rgb(image_array):
    num_rows = len(image_array)
    num_columns = len(image_array[0])
    matrix = []
    for x in range(num_rows):
        matrix.append([])
    for i in range(num_rows):
        for y in range(num_columns):
            matrix[i].append(0)
    for row_index in range(len(image_array)):
        for column_index in range(len(image_array[0])):
            invert_r = (255 - image_array[row_index][column_index][0])
            invert_g = 255 - image_array[row_index][column_index][1]
            invert_b = 255 - image_array[row_index][column_index][2]

            matrix[row_index][column_index] = [invert_r, invert_g, invert_b]
    return matrix



if __name__ == "__main__":
    colour = [[[25, 80, 233], [23, 235, 4], [1, 1, 1]], [[0, 0, 0], [234,33,66 ], [245, 55, 66]]]
    #[230,175, 22]
    practice_array = [[['1a'],['1b'],['1c'],['1d']],[['2a'],['2b'],['2c'],['2d']],[['3a'],['3b'],['3c'],['3d']],[['4a'],['4b'],['4c'],['4d']]]
    #practice_array = [['a','b','c'],['d','e','f'],['g','h','i']]
    #testing0 = rotate_90_degrees(practice_array, 0)
    #print(testing0)
    #testing1 = flip_image(practice_array, )
    #print(testing1)
    # gray_image = [[0,1,2],[255,254,253]]
    # testing2 = invert_grayscale(gray_image)
    # print(testing2)
    #testing3 = crop(practice_array, 'down', 1)
    #print(testing3)
    #testing4 = rgb_to_grayscale(colour)
    #print(testing4)
    testing5 = invert_rgb(colour)
    print(testing5)



