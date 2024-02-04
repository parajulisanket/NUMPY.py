# 14------Search, sort, search sorted, filter functions-----------------

    #----- search function--

# import numpy as np
# a = np.array([1,2,4,6,8,7])
# print(a)

# answer = np.where(a == 4)
# print(answer)


    # -----sort function---

# import numpy as np
# a = np.array([[9,4,5,6],[3,8,7,2]]) # 2-D
# print(np.sort(a))


# import numpy as np
# a = np.array([[9,4,5,6,3,8,7,2]]) # 1-D
# print(np.sort(a))



    #---search sorted function------

# import numpy as np
# a = np.array([1,2,3,4,5,7,8,9]) # 1-D
# print(np.searchsorted(a,6))


    # --filter function-----

# import numpy as np

# a = np. array(['a','b','c','d']) # 1-D
# f = [True, False,True,False]
# print(a[f])


# import numpy as np

# a = np. array([['a','b','e'],['r','c','d']]) # 2-D
# f = [[True, False,False],[True,True,False]]
# print(a[f])


# 15-----------Shuffle, Unique, resize, flatten, revel function-----------

    # shuffle function:

# import numpy as np

# a = np.array([1,2,3,4,5,6,7,8])  #1-D
# np.random.shuffle(a)
# print(a)


    # unique function:

# import numpy as np

# a = np.array([1,2,3,2,5,2,6,2,3,4,4,7,8])
# print(np.unique(a))


    # resize function:
    # > resize can be done upto any dimension of array we want with limited number.

# import numpy as np

# a = np.array([1,2,3,4,5,6,7,8,9])
# answer = np.resize(a,(3,4)) 
# print(answer)
# print(answer.ndim)

    
    # flatten function:
    # revel function:


# 16------------ Insert and delete function ----------------------

    # insert function:

# import numpy as np
# a = np.array([1,2,3,5,6])  # 1-D
# print(np.insert(a,3,4))


# import numpy as np
# a = np.array([[1,2,3],[5,6,7],[1,2,3]])  # 2-D
# answer = np.insert(a, 3 , 4 , axis=1)
# print(answer)


    # delete function:

# import numpy as np

# a = np.array([1,2,3,4])
# print(np.delete(a,1))