# 1 -----------What is NumPy? ----------------------------------
# > NumPy is the fundamental package for scientific computing in Python.
# > NumPy is a Python library that provides a multidimensional array objects, various derived objects. 

# Advantage of NumPy:
# > Faster than python List, consumes less memory, convenient to use. 

# Types of Arrays:
# > 1-D Arrays
# > 2-D Arrays
# > 3-D Arrays
# > Higher Dimensional Arrays

# 3 ---------------------------------Arrays creation----------------------------------------------
    # -------------creating numpy 1-D arrays----------

# import numpy as np
# a = np.array([1,2,3,4], ndmin=(5))
# print(a)
# print(a.ndim)


# import numpy as np

# l =[]
# for i in range(1,5):
#     int_1 = int(input("enter the number:"))
#     l.append(int_1)
# print(np.array(l))


    # -------------creating numpy 2-D arrays----------

# import numpy as np
# a = np.array([[1,2,3,4],[6,2,3,1],[1,2,3,4]])
# print(a)
# print(a.ndim) # to check the dimension of the array



    # -------------creating numpy 3-D arrays----------

# import numpy as np
# a = np.array([[[1,2,3],[12,34,544],[3,4,6]]])
# print(a)
# print(a.ndim)


    # -------------creating numpy Multi-dimensional arrays-------(it uses (ndmin))---

# import numpy as np

# a = np.array([1,2,3], ndmin= 10)
# print(a)
# print(a.ndim)



# 4 --------------Special Types of Arrays(filled with specific value)-------------

    #---------zeros, ones and empty arrays----------
# import numpy as np

# a = np.zeros((4,3))
# b = np.zeros(7)
# c = np.ones((4,4))
# d = np.ones(3)
# e = np.empty(5)

# print("This is zeros array",a)
# print("This is zeros array",b)
# print("This is one array",c)
# print("This is one array",d)
# print("This is empty array",e)


    #---------arange and diagonal and linspace in arrays----------

# import numpy as np
# a = np.arange(9)
# print(a)

# b = np.eye(2,4)
# c = np.eye(5)
# print(b)
# print(c)

# d = np.linspace(0,20, num=5) # basically, linespace creates value that are spaced evenly.
# print(d)

# 5 ----------NumPy arrays with Random Numbers---------------------------
            
        #---- rand() function------(It gives array between 0 and 1)-----

# import numpy as np

# a = np.random.rand(2) # 1-D
# b = np.random.rand(3,5) # 2-D
# c = np.random.rand(2,4,3) # 3-D
# print(a)
# print(a.ndim)
# print(b)
# print(b.ndim)
# print(c)
# print(c.ndim)


        #---- randn() function--- (It gives array close to zero either positive or negative)--------

# import numpy as np

# a = np.random.randn(2)
# print(a)
# print(a.ndim)
# b = np.random.randn(2,3)
# print(b)
# print(b.ndim)
# c = np.random.randn(3,2,4)
# print(c)
# print(c.ndim)
# d = np.random.randn(4,2,2,4)
# print(d)
# print(d.ndim)


        #---- randf() function--( begin from 0.0 and it is less than 1.0)---------

# import numpy as np

# a = np.random.ranf((3)) # 1-D array 
# print(a)
# print(a.ndim)
# b = np.random.ranf((3,4)) # 2-D array 
# print(b)
# print(b.ndim)
# c = np.random.ranf((4,2,3)) # 3-D array 
# print(c)
# print(c.ndim)


        #---- randint() function--(It gives array according to the range we have created.)---------

# import numpy as np

# a = np.random.randint(1,20, size=(5)) # 1-D array 
# print(a)
# print(a.ndim)
# b= np.random.randint(2,100,size=(5,10)) # 2-D array 
# print(b)
# print(b.ndim)
# c = np.random.randint(20,25, size=(2,2,2,5)) # 4-D array 
# print(c)
# print(c.ndim)

