#-----------------Numpy matrix---------------------------

# import numpy as np
# a = np.matrix([[1,2,3],[4,5,6]])
# print(a)
# print(type(a))



# import numpy as np
# a = np.matrix([[1,2],[3,4]])
# b = np.matrix([[1,2],[3,4]])
# answer= np.dot(a,b) # dot() function for multiplication in matrix.
# print(answer)
# print(type(answer))



#-----------------Matrix function------------------------

    # Transpose function:

# import numpy as np
# a = np.matrix([[1,2,3],[3,4,5]])
# print(a)
# print(np.transpose(a))


    # Swapaxes function:


    # Inverse function:

# import numpy as np
# a = np.matrix([[1,2,3,4],[1,2,3,4],[1,2,3,4],[5,6,7,8]])
# print(a)
# print(np.linalg.inv(a))


    # Power function:

# import numpy as np
# a = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
# print(np.linalg.matrix_power(a,2)) # if the n of power is positive it gives proper value.
# print(np.linalg.matrix_power(a,0)) # if the n of power is zero it gives identity matrix.
# print(np.linalg.matrix_power(a,-2)) # if the n of power is negative it inverse the value with power.


    # Determinate function:

# import numpy as np
# a = np.matrix([[1,2],[3,4]]) 
# print(np.linalg.det(a)) # this function has its own formula\rule of calculating the matrix.