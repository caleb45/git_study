import numpy as np

# 1-d
np1 = np.array([1,2,3,4,5,6,7,8,9,10])
#for x in np1:
#	print(x)


# 2-d Array
'''
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in np2:
	# Print rows
	#print(x)
	for y in x:
		print(y)
'''

# 3-D Array
np3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
'''
for x in np3:
	#print(x)
	for y in x:
		#print(y)
		for z in y:
			print(z)
'''

# Use np.nditer()
for x in np.nditer(np1):
	print(x)
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


# ------------------------------------------
# ------------------------------------------
# ------------------------------------------
# ------------------------------------------


# Create 1-D Numpy Array and Get Shape
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)
print(np1.shape)

# Create 2-D Array and get Shape, (rows/columns-elements)
#np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
#print(np2)
#print(np2.shape)

# Reshape 2-D
#np3 = np1.reshape(3,4)
#print(np3)
#print(np3.shape)

# Reshape 3-D
np4 = np1.reshape(2,3,2)
print(np4)
print(np4.shape)

# Flatten to 1-D
np5 = np4.reshape(-1)
print(np5)
print(np5.shape)



# ------------------------------------------
# ------------------------------------------
# ------------------------------------------
# ------------------------------------------



# np.sort()  Numerical
np1 = np.array([6,7,4,9,0,2,1])
#print(np1)
#print(np.sort(np1))



# Alphabetical
#np2 = np.array(["John", "Tina", "Aaron", "Zed"])
#print(np2)
#print(np.sort(np2))


# Booleans T/F
#np3 = np.array([True, False, False, True])
#print(np3)
#print(np.sort(np3))



# Return a copy not change the original
#print(np1)
#print(np.sort(np1))
#print(np1)



# 2-d
np4 = np.array([[6,7,1,9],[8,3,5,0]])
print(np4)
print(np.sort(np4))

