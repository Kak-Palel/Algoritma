import numpy as np

def gaussian_elimination(M, stage = 0):
  length = len(M)

  if(stage == length):
    return M
  
  factor = M[stage][stage]
  for i in range(stage, length):
    M[stage][i] /= factor
  
  for i in range(stage + 1, length):
    a = M[i][stage]
    for j in range(stage, length):
      M[i][j] -= a*M[stage][j]

  M = gaussian_elimination(M, stage + 1)
  
  return M