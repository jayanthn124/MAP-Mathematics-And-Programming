def matrix_multiplication(a, b):
    column_a = len(a[0])
    rows_a = len(a)
    column_b = len(b[0])
    rows_b = len(b)

    result_matrix = [[j for j in range(column_b)] for i in range(rows_a)]

    if column_a == rows_b:
        for x in range(rows_a):
            for y in range(column_b):
                sum = 0
                for k in range(column_a):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y] = sum
        
        return result_matrix

    else:
        print("Amount of Columns of 'a' must match the Amount of Rows of 'b'. ")
        return home