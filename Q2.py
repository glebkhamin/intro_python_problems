# student number: 22107414

# Q2(a)

import numpy as np

def matrix_multiplication(*argv):
  """
    DEFINITION  : This function is multiplying the matrices

    INPUT(argv)
        * argv  : input argument of variable size of numpy array

    OUTPUT(argv )
        * resultMatrix   : a new matrix which is the result of product of two or more matrices

    EXAMPLE USAGE
        res = matrix_multiplication(numpyArray1, numpyArray2)
  """

  # Some local variables used for multiplcation process later in the code
  allMatrices = argv
  totalMatrices = len(argv)
  matrix1 =  allMatrices[0] 

  # To iterate through all the numpy arrays passed as arguments
  for matrixNo in range(1, len(allMatrices)):

    nextMatrix =  allMatrices[matrixNo] 

    matrix1_shape = matrix1.shape
    nextMatrix_shape = nextMatrix.shape

    # Values used for multiplication rule
    matrix1_columns = matrix1_shape[1]
    nextMatrix_rows = nextMatrix_shape[0]

    # Values used for the result matrix dimension rule
    matrix1_rows = matrix1_shape[0]
    nextMatrix_columns = nextMatrix_shape[1]
    resultMatrix = np.zeros((matrix1_rows, nextMatrix_columns)) 
    if (matrix1_columns == nextMatrix_rows):
    
      # Pick each row from the 1st matrix
      for row in range(matrix1_rows):
        selectedRow = matrix1[row,:]

        # Pick each column from the 2nd matrix
        for column in range(nextMatrix_columns):
          selectedColumn = nextMatrix[:,column]
    
          combineMatrix = list(zip(selectedRow,selectedColumn))
          # Do the multiplication and addition to get the final value for the result matrix
          finalValue = 0
          for pair in combineMatrix:
            finalValue += pair[0]*pair[1]
         
          # Place the calculated values in the result matrix
          resultMatrix[row][column] = finalValue
 
    else: 
      print("Matix dimension mismatch....")
    
    return resultMatrix

# Q2(b)

def linear_solver(A,b):
  """
    DEFINITION  : This function finds the solution of the system of linear equations

    INPUT(A,b)
        * A,b   : A is the matrix and b is the column vector 

    OUTPUT(A,b )
        * res   : with or without the solution of the equation as a column vector 

    EXAMPLE USAGE
        res = linear_solver(numpyArray1, numpyArray2 as a column vector)
  """

  # Variables declared to hold the dimensions and final result of the function
  shape_A = A.shape
  shape_b = b.shape
  res = "None"

  # Selection statements are used to check if the unique solution is possible
  # and to execute the appropriate statement
  if (shape_A[0] == shape_A[1]  and 0 not in A ):

    # Multiply test to see that column of the first must be equal to rows of the second
    if (shape_A[1] == b.shape[0]):

      print("Unique Solution!.")
      inverseOfA = np.linalg.inv(A)
      res  = matrix_multiplication(inverseOfA, b)

  elif (shape_A[0] < shape_A[1]):
    print("Underdetermined system: number of equations are lower than the variables")

  elif (shape_A[0] > shape_A[1]):
    print("Overdetermined system: number of equations are higher than the variables")

  else:
    print(" 0 values or other kinds of dimension mismatches")
  
  return res

# Q2(c)

def LLS(A,b):
  """
    DEFINITION  : This function finds the solution of the system of linear equations by using OLS method

    INPUT(A,b)
        * A,b   : A is the matrix and b is the column vector 

    OUTPUT(A,b )
        * res   : with or without the solution of the equation as a column vector 

    EXAMPLE USAGE
        res = linear_solver(numpyArray1, numpyArray2 as a column vector)
  """

  # Finding the transpose matrix A(T)
  transposeMatrix = A.T

  # Finding A(T)*A (multiplying the transpose matrix by the initial matrix)
  transposeMatrix_step_2 = matrix_multiplication(transposeMatrix, A)

  # Finding the inverse of A(T)*A
  inverseMatrix = np.linalg.inv(transposeMatrix_step_2)

  # Multiplying the inverse matrix by A(T)
  a_plus = matrix_multiplication(inverseMatrix, transposeMatrix)
  
  variablesValues =  matrix_multiplication(a_plus, b)

  return variablesValues