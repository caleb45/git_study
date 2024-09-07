import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
#import torch 



# ----------------------------------------
# https://www.youtube.com/watch?v=gnKbAAVUzro&list=PLCC34OHNcOtpalASMlX2HHdsLNipyyhbK&index=1
# https://github.com/flatplanet/numpy_youtube/tree/main
# ----------------------------------------


'''
Python List Exmapel : 

list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1[0])
list2 = ['John Elder', 42, list1, True]
print(list2)
'''

# -------------------------------
# Numpy 
# ndarray : n-dimensital array 
# -------------------------------
print('-'*30)
print(f'np.array(list)')
print()
np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1)
print()
print(f'shape : np1.shape {np1.shape}')
ans = np1.shape
print(f'Type : {type(ans)}')

#------------------------
# arange
# arange(start, end) : start inclusive, end exclusive
#------------------------
print('-'*30)
print(f'arange(start, end) : start inclusive, end exclusive')
print(f'arange(end) : start can be deleted, end exclusive')
print()
np3 = np.arange(1, 10)
print(f'np.arange(1, 10) : {np3}')
np2 = np.arange(10)
print(f'np.arange(10) : {np2}')

#------------------------
# step 
# arange(start, end, step) : start inclusive, end exclusive
#------------------------
print('-'*30)
print(f'np.arange(start, end, step) : start inclusive, end exclusvie')
print()
np3 = np.arange(0, 10, 2) 
print(f'STEP example np.arange(0, 10, 2) : {np3}')


#--------------------------
# zeros 
#--------------------------
print('-'*30)
print(f'np.zeros(shape)')
print()
np4 = np.zeros(10)
print(f'np.zeros(10) : ')
print(np4)

np5 = np.zeros((2, 3))
print(f'np.zeros 2x3 Matrix : np.zeros((2,3))') 
print(np.zeros((2,3)))

#----------------------------
# full
# full((shape), n) : fill n to a shape 
#----------------------------
print('-'*30)
print(f'np.full((shape), n)')
print()

np6 = np.full((3), 5)
print(f'np.full((3), 5)')
print(np6)

np7 = np.full((2, 3), 5)
print('np.full((2, 3), 5) :')
print(np7)


#-----------------------------
# Convert 'List' to np array
#-----------------------------
print('-'*30)
my_list = [1, 2, 3, 4, 5]
np8 = np.array(my_list)
print(type(np8))
print(np8)
print(np8[0])



#---------------------------------
# SLICING
#---------------------------------
print()
print('-'*30)
print('SLICING')
print('-'*30)
print('nparray[start:end] : start inclusive, end exclusive and both can be deleted')
np1 = np.arange(1, 11)
print(f'np1 : {np1}')
print()

print(f'np1[0] Index starts with 0 : {np1[0]}')
print(f'np1[3] : {np1[3]}')
print(f'np1[9] : {np1[9]}')
print(f'np1[3:9] : {np1[3:9]}')
print(f'np1[3:-1] : {np1[3:-1]}')
print(f'np1[3:] : {np1[3:]}')
print(f'np1[-3:-1] : {np1[-3:-1]}')
print()
print()

#----------------------------------
# SLICING with STEPS
#----------------------------------
print('Slicing with Steps')
print(f'np1[1:5] : index 1, 2, 3, 4')
print(f'{np1[1:5]}')
print(f'np1[1:5:2] : index 1, 3')
print(f'{np1[1:5:2]}')
print(f'np1[5:1:-2] : index 5, 3')
print(f'{np1[5:1:-2]}')
print()
print('Steps on the entire array')
print(f'np1[::2] : index 0, 2, 4, 6, 8')
print(f'{np1[::2]}') # 0, 2, 4, 6, 8
print(f'np1[::3] : index 0, 3, 6, 9')
print(f'{np1[::3]}') # 0, 3, 6, 9
print()
print()


#----------------------------------
# Slicing of 2D Array
#----------------------------------
print('Slicing of 2D Array')
np2 = np.array(
	[
	 [1, 2, 3, 4, 5], 
	 [6, 7, 8, 9, 10], 
	])
print(f'np2 :')
print(np2)
print(f'np2.shape : {np2.shape}')
print()

print('Index a Single Item')
print(f'np2[1, 2] : index(1,2)', end='  ')
print(f'{np2[1, 2]}')
print()

print('Slicing a 2D Array')
print(f'np2[0:1, 1:3] : {np2[0:1, 1:3]}')
print(f'np2[:2, 1:3] :')
print(f'{np2[:2, 1:3]}')

