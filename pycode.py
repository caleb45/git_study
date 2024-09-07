import numpy as np

list1 = [1,2,3,4,5]
#print(list1)
#print(list1[0])

list2 = ["John Elder", 41, list1, True]
#print(list2)


# Numpy - Numeric Python
# ndarray = n-dimensional array

np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

# Range
np2 = np.arange(10)
print(np2)

# Step
np3 = np.arange(0,10, 2)
print(np3)

# Zeros
np4 = np.zeros(10)
print(np4)

# Multidimensional zeros
np5 = np.zeros((2,10))
print(np5)

# Full
np6 = np.full((10), 6)
print(np6)

# Multidimensional Full
np7 = np.full((2,10), 6)
print(np7)

# Convert Python lists to np
my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8)

print(np8[0])

# ------------------------------------------
# ------------------------------------------
# ------------------------------------------

# Slicing Numpy Arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

# Return 2,3,4,5
print(np1[1:5])

# Return from something till the end of the array?
# 4-9
print(np1[3:])

# Return Negative Slices
# 7, 8
print(np1[-3:-1])

# Steps
print(np1[1:5]) # 2-5
print(np1[1:5:2]) # 2-5 in steps of 2

# Steps on the enitre array
print(np1[::2])
print(np1[::3])

# Slice a 2-d array
np2 = np.array([
	[1,2,3,4,5], 
	[6,7,8,9,10]])
# Pull out a single item
print(np2[1,2])

# Slice a 2-d array 2,3
print(np2[0:1, 1:3])

# Slice from both rows 2,3 and 7,8
print(np2[0:2, 1:3])


# ------------------------------------------
# ------------------------------------------
# ------------------------------------------


# Numpy Universal Function
np1 = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
print(np1)

# Square root of each element 
#print(np.sqrt(np1))

# Absolute Value
#print(np.absolute(np1))

# Exponents
#print(np.exp(np1))

# Min/Max
#print(np.max(np1))
#print(np.min(np1))

# Sign positive or negative
#print(np.sign(np1))

# Trig sin cos log
print(np.log(np1))


# ------------------------------------------
# ------------------------------------------
# ------------------------------------------


# Copy Vs. View
np1 = np.array([0,1,2,3,4,5])

# Create a view
np2 = np1.view()

print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np2[0] = 41

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')


'''
# Create a Copy
np2 = np1.copy()
print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np2[0] = 41

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')
'''

