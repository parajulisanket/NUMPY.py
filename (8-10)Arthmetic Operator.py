# 8 ---------NumPy arithmetic operators and functions-----------------

        #----- Arithmetic operators----------

# import numpy as np

# first = np.array([[1,2,3],[1,2,3]])
# second = np.array([[3,7,9],[1,2,3]])

# a = np.add(first,second)
# print(a)

# b = np.subtract(first,second)
# print(b)

# c = np.multiply(first,second)
# print(c)

# d = np.divide(first,second)
# print(d)

# e = np.mod(first,second)
# print(e)

# f = np.power(first,second)
# print(f)

# g = np.reciprocal(first,second)
# print(g)

        # --------Arithmetic functions------------

# import numpy as np

# x = np.array([1,2,3,4,5,6,38,4])
# print(np.max(x),np.argmax(x)) # max gives the maximum number present in array and argmax gives position of it.
# print(np.min(x),np.argmin(x)) # min gives the minimum number present in array and argmin gives position of it.



# import numpy as np

# x = np.array([1,2,3,4])
# print(np.sqrt(x)) # .sqrt gives the square root of the number present in the array.
# print(np.cumsum(x)) # .cumsum adds the number of array with one another.


# import numpy as np

# x = np.array([1,2,3,4,5])
# print(np.sin(x)) # .sin() gives the value of sin.
# print(np.cos(x)) # .cos() gives the value of cos.



# 9 ------------Broadcasting numpy arrays------------------------

# import numpy as np

# a = np.array([1,2,3,4])
# # b = np.array([[1],[2],[3],[4],[5],[2]])
# c = np.array([[[[1],[2],[3],[4],[5],[2],[3],[5]]]])

# answer = np.add(a,c)
# print(answer)



# 10 ------------Indexing and Slicing in Numpy arrays-----------------------

        # -----Indexing------:

# Indexing for 1-D,2-D, 3-D arrays:

# import numpy as np
# a = np.array([1,2,3,4])
# b = np.array([[1,2,3],[2,4,6],[3,8,90],[4,2,1],[5,2,56],[2,0,5]])
# c = np.array([[[1,2,3],[2,7,6]],[[3,80,12],[4,34,56]],[[9,87,90],[2,23,44]],[[34,455,3],[45,15,87]]])

# print(a)
# print(a[3])
# print(b)
# print(b[2,2])
# print(c)
# print(c[3,1,1])


# Indexing for 3-D array:

# import numpy as np
# a = np.array([[[1,2,3,4],[1,0,9,4]],[[1,2,4,6],[9,6,7,2]],[[1,0,89,34],[39,49,28,54]]]) 
# print(a)
# print(a[2,1,1])


        # -----Slicing-----:

# sllicing for 1-D array:

# import numpy as np
# a = np.array([1,2,3,4,5,6,7,8,9])
# print(a)
# print(a[0:4])
# print(a[0:9:2])
# print(a[::3])


# slicing in 2-D array:
# import numpy as np
# a = np.array([[1,2,3,4,5,6],[45,55,94,60,73,99]])
# print(a)
# print(a[0,1:5])
# print(a[1,2:])
# print(a[1,::3])


# slicing in 3-D array:
# import numpy as np
# a = np.array([[[1,2,3,4,5,6],[45,55,94,60,73,99]],[[2,45,65,78,97,35],[23,43,56,64,73,23]]])
# print(a)
# print(a[0,1,2:5])
# print(a[1,0,:])


