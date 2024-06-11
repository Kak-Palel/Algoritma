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

def determinant_gauss_jordan(M, stage = 0, swap = -1):
    length = len(M)

    if(stage == length):
        return M, swap
    
    # Find a row with a non-zero element in the same column
    for i in range(stage, length):
        if M[i][stage] != 0:
            M[stage], M[i] = M[i], M[stage]
            swap *= -1
        break
    else:
        raise Exception("Matrix is singular")

    factor = M[stage][stage]

    for i in range(stage + 1, length):
        a = M[i][stage]
        for j in range(stage, length):
            M[i][j] -= a*M[stage][j] / factor

    M, swap = determinant_gauss_jordan(M, stage + 1, swap)
    if stage > 0:
        return M, swap
    
    det = 1
    for i in range(0, length):
        det *= M[i][i]

    return det*swap

# M = [[3, -1,  2],
#      [5,  0,  4],
#      [8,  2, -3]]
# print("real det: ", -32 + 20 - 24 - 15)
# A = determinant_cofactor(M)
# print(A)