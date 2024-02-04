# 11-----------Iterating in arrays--------------

    # Iteration in 1-D array:

# import numpy as np

# a = np.array([1,2,3,4,5])
# print(a)
# for i in np.nditer(a):
#     print(i)
# print()
# print(a.ndim)
# print(a.dtype)


    # Iteration in 2-D array:

# import numpy as np

# a = np.array([[1,2,3,4],[4,5,6,7]])
# print(a)
# print()
# for i in np.nditer(a):
#     print(i)




#     Iteration in 3-D array:

# import numpy as np

# a = np.array([[[1,2,3,4],[4,5,6,7]],[[1,2,3,4],[4,5,6,7]]])
# print(a)
# print()
# for i in np.nditer(a):
#     print(i)
# print()
# print(a.ndim)

# ------------ Using np.ndenumerate() function----------------

# import numpy as np

# a = np.array([1,2,3,4,5])
# print(a)
# for i in np.ndenumerate(a):
#     print(i)
# print()
# print(a.ndim)
# print(a.dtype)



# import numpy as np

# a = np.array([[1,2,3,4],[4,5,6,7]])
# print(a)
# print()
# for i in np.ndenumerate(a):
#     print(i)



# 12------Difference between copy and view----------

    # copy --(It changes the oriiginal element/data, but doesn't change the copies element/data. )

# import numpy as np

# a = np.array([1,2,3,4,5])
# b = a.copy()
# a[2]=50
# print(a)
# print(b)


    # View --(It changes both the original as well as viewed data/elements.)

# import numpy as np

# a = np.array([1,9,5,3,4])
# b = a.view()

# a[3] = 40
# print(a)
# print(b)



# 13--------------Join and Split Function---------------------
# > join array: Joining means putting contents of two or more arrays in a single array.

    # joining 1-D arrays:

# import numpy as np

# a = np.array([1,2,3,4])
# b = np.array([7,7,8,0])

# answer = np.concatenate((a,b))
# print(answer)


    # joining 2-D arrays:

# import numpy as np

# a = np.array([[1,2,3,4],[2,4,6,3]])
# b = np.array([[7,7,8,0],[1,5,7,2]])

# answer = np.concatenate((a,b), axis=1)
# print(answer)



# > Split array: splitting breaks one array into multiple.

    # Splitting in 1-D array:

# import numpy as np
# a = np.array([1,2,3,4,5,6])
# answer = np.array_split(a,10)
# print(a)
# print(answer)


    # splitting in 2-D array:

# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# answer = np.array_split(a,10)
# print(a)
# print(answer)


# import numpy as np
# a = np.array([[1,2,3],[3,4,5]])
# print(a)
# print(np.array_split(a,4))