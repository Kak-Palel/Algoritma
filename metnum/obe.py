def gaussian_elimination(M, stage = 0):
  length = len(M)

  if(stage == length):
    return M
  
  # Find a row with a non-zero element in the same column
  for i in range(stage, length):
    if M[i][stage] != 0:
      M[stage], M[i] = M[i], M[stage]
      break
  else:
    raise Exception("Matrix is singular")

  factor = M[stage][stage]
  for i in range(stage, length):
    M[stage][i] /= factor
  
  for i in range(stage + 1, length):
    a = M[i][stage]
    for j in range(stage, length):
      M[i][j] -= a*M[stage][j]

  M = gaussian_elimination(M, stage + 1)
  
  return M