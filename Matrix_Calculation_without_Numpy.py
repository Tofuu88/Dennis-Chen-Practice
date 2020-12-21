def array_transform(array):
    new_array = []
    while True:
        if len(array[-1]) == 0:
            break  
        temp = []
        for i in array:
            if len(i) == 0:
                break
            else:
                temp.append(i[0])
                del(i[0])  # this deletes the object from the container so container is still there but empty (used to contain object)
        new_array.append(temp)

    return new_array

def dot_value(row_1, row_2):
    sum = 0
    for i in zip(row_1, row_2):
        sum = sum + i[0] * i[1]
    return sum

def dot_product(a_1, a_2):
    a_3 = array_transform(a_2)
    result = []
    for i in a_1:
        temp = []
        for j in a_3:
            temp.append(dot_value(i, j))
        result.append(temp)
    return result

def row_column():
    m_1_row, m_1_col = [int(x) for x in input().split()]
    return m_1_row, m_1_col

def array_create(row, column):
    array = []
    r = 0
    while r < row:
        array.append([float(x) for x in input().split()])
        r += 1
    return array

def add_array(a_1, a_2):
    c = []
    for a_sublist, b_sublist in zip(a_1, a_2):
        c.append([a_sublist_item + b_sublist_item for a_sublist_item, b_sublist_item in zip(a_sublist, b_sublist)])
        # zip(a_1, a_2) gives us a new nested list - each new sub-list contains elements to be added.    zip(a_1, a_2)[0] = first row
        # zip(a_sublist, b_sublist) gives each element of each row sublist, and add sublist together
        # sub_list_item is the item of the row list of the total row
        # row list comes from zip(a_1, a_2), item of the row_list are elements of the matrix to be added
    return c

def multiply_constant(array, c):
    total_list = []
    for i in array:  # this is each row of the matrix
        row_list = []
        for j in i:  # this is each element of the row
            row_list.append(j * c)
        total_list.append(row_list)
    return total_list

def main_diagonal(array):
    new_array = []
    while True:
        if len(array[-1]) == 0:
            break  
        temp = []
        for i in array:
            if len(i) == 0:
                break
            else:
                temp.append(i[0])
                del(i[0])
        new_array.append(temp)
    return new_array

def side_diagonal(array):
    new_array = []
    temp = []
    for i in range(-1, -len(array) - 1, -1):
        reverse_array = list(reversed(array[i]))
        temp.append(reverse_array)
    while True:
        if len(temp[-1]) == 0:
            break
        temp_2 = []
        for j in temp:
            if len(j) == 0:
                break
            else:
                temp_2.append(j[0])
                del(j[0])
        new_array.append(temp_2)

    return new_array

def vertical_trans(array):
    new_array = []
    for i in range(len(array)):
        reverse_array = list(reversed(array[i]))
        new_array.append(reverse_array)
    return new_array

def horizonal_trans(array):
    new_array = list(reversed(array))
    return new_array

def determinant_recursive(A, total=0):
    # Section 1: store indices in list for row referencing
    indices = list(range(len(A)))
     
    # Section 2: when at 2x2 submatrices recursive calls end
    if len(A) == 1:
        return A[0][0]

    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
 
    # Section 3: define submatrix for focus column and 
    #      call this function
    for fc in indices: # A) for each focus column, ...
        # find the submatrix ...
        As = A # B) make a copy, and ...
        As = As[1:] # ... C) remove the first row
        height = len(As) # D) 
 
        for i in range(height): 
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2) # F) 
        # G) pass submatrix recursively
        sub_det = determinant_recursive(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det 
 
    return total

# below here is copied 
def transposeMatrix(m):
    return list(map(list,zip(*m)))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

# above here is copied

def main():
    while True:
        print("""1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit""")
        inp = input("Your choice:", )
        
        if inp == "1":  
            
            print("Enter size of first matrix:")
            row, col = row_column()
            print("Enter first matrix:")
            array_1 = array_create(row, col)
            print("Enter size of second matrix:")
            row_1, col_1 = row_column()
            print("Enter second matrix:")
            array_2 = array_create(row_1, col_1)
            
            print("The result is:")
            if row == row_1 and col == col_1:
                result = add_array(array_1, array_2)
                for i in result:
                    j = list(map(str, i))
                    print(" ".join(j))
            else:
                print("The operation cannot be performed.")

        elif inp == "2":
            
            print("Enter size of first matrix:")
            row, col = row_column()
            print("Enter first matrix:")
            array_1 = array_create(row, col)

            c = float(input("Enter constant:", ))
            
            print("The result is:")
            
            result = multiply_constant(array_1, c)
            for i in result:
                j = list(map(str, i))
                print(" ".join(j))

        elif inp == "3":
            
            print("Enter size of first matrix:")
            row, col = row_column()
            print("Enter first matrix:")
            array_1 = array_create(row, col)
            print("Enter size of second matrix:")
            row_1, col_1 = row_column()
            print("Enter second matrix:")
            array_2 = array_create(row_1, col_1)
            
            print("The result is:")
            
            result = dot_product(array_1, array_2)
            for i in result:
                j = list(map(str, i))
                print(" ".join(j))
        
        elif inp == "4":
            print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")

            chc = input("Your choice:", )

            print("Enter size of first matrix:")
            row, col = row_column()
            print("Enter first matrix:")
            array_1 = array_create(row, col)

            print("The result is:")
            if chc == "1":
                result = main_diagonal(array_1)
            elif chc == "2":
                result = side_diagonal(array_1)
            elif chc == "3":
                result = vertical_trans(array_1)
            elif chc == "4":
                result = horizonal_trans(array_1)
            for i in result:
                j = list(map(str, i))
                print(" ".join(j))
        
        elif inp == "5":
            print("Enter size of first matrix:")
            row, col = row_column()
            print("Enter first matrix:")
            array_1 = array_create(row, col)

            print("The result is:")
            result = determinant_recursive(array_1)
            print(result)
        
        elif inp == "6":
            print("Enter size of first matrix:")
            row, col = row_column()
            print("Enter first matrix:")
            array_1 = array_create(row, col)
            
            result = getMatrixInverse(array_1)
            for i in result:
                j = list(map(str, i))
                print(" ".join(j))

        elif inp == "0":
            break

if __name__ == "__main__":
    main()
