def determinant_cofactor(m : list):
    if len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
  
    neg = 1
    result = 0
    for i, a in enumerate(m[0]):
        tempM = m[1:]  # remove the first row
        tempM = [row[:i] + row[i+1:] for row in tempM]  # remove the i-th column
        result += neg * m[0][i] * determinant_cofactor(tempM)
        neg *= -1
    return result

# M = [[3, -1, 2], [5, 0, 4], [8, 2, -3]]
# print(determinant_cofactor(M))