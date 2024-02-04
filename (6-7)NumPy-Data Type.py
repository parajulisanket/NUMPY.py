# 6 ----------------------Data Type----------(variable.dtype() is used to identify the data type)--------------------------

# import numpy as np

# a = np.array([1,2,3,4])
# print(a)
# print(a.dtype)


        # --------coversion of data type--------

# import numpy as np

# a = np.array([1,2,3,4], dtype='f')
# print(a)
# print(a.dtype)
# b = np.array([1,2,3,4], dtype='S')
# print(b)
# print(b.dtype)
# c = np.array(['s','a','N','K'])
# print(c)
# print(c.dtype)
# d = np.array([1.2, 1.000, 2.333,33.0033], dtype='i')
# print(d)
# print(d.dtype)


        #----------(using astype function to convert)---------------

# import numpy as np

# a = np.array([1,2,3,4])
# b = a.astype(float)
# print(a)
# print(a.dtype)
# print(b)
# print(b.dtype)


# 7 ------------------------Shape and Reshape in Numpy--------------

        #----------shape---(It tells the row and coloumn of the array)--------

# import numpy as np

# a = np.array([2,3,4])
# print(a)
# print(a.ndim)
# print(a.shape)


# import numpy as np

# a = np.array([[2,10,3],[1,2,3]])
# print(a)
# print(a.ndim)
# print(a.shape)


# import numpy as np

# a = np.array([[[2,10,3],[1,2,3],[1,2,3]]])
# print(a)
# print(a.ndim)
# print(a.shape)



        #----------Re-shape---(It converts the dimension of the array)--------

# import numpy as np

# a = np.array([2,3,4,5,6,7])
# print(a)
# print(a.ndim)

# b = a.reshape(3,2)
# print(b)
# print(b.ndim)


        # ----reshaping 1-dimension into 3-dimension array by the help of .rehape()-- 
# import numpy as np

# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print(a.ndim)
# b = a.reshape(2,2,3)
# print(b)
# print(b.ndim)


        # ----reshaping 1-dimension into 4-dimension array by the help of .rehape()-- 
# import numpy as np

# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
# print(a)
# print(a.ndim)
# b = a.reshape(2,2,2,3)
# print(b)
# print(b.ndim)



        # ----reshaping 2-dimension into 4-dimension array by the help of .rehape()-- 
# import numpy as np

# a = np.array([[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24]])
# print(a)
# print(a.ndim)
# b = a.reshape(2,2,2,3)
# print(b)
# print(b.ndim)


                # ----reshaping 3-dimension into 1-dimension array by the help of .rehape()-- 
# import numpy as np

# a = np.array([[[1,2,3],[2,3,4],[3,45,6]]])
# print(a)
# print(a.shape)
# print(a.ndim)
# b = a.reshape(-1)
# print(b)
# print(b.ndim)

                # ----reshaping 4-dimension into 2-dimension array by the help of .rehape()-- 
# import numpy as np

# a = np.array([[[[1,2,3],[2,3,4],[3,45,6],[1,2,3]]]])
# print(a)
# # print(a.shape)
# print(a.ndim)
# b = a.reshape(6,-1)
# print(b)
# print(b.ndim)






