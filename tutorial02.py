import numpy as np 


# ---------------------------------
# Universal Functions 
# : np.array 의 elementwise 연산을 빠르게 수행해주는 함수 
# : 자체적으로 만든 함수도 가능함(frompyfunc() 함수) 
# ---------------------------------

print(f'Universal Functions : np.array의 elementwise 연산을 빠르게 수행해 주는 함수')

np0 = np.array([1, 2, 3, 4, 5])
np1 = np.array([-2,-1,0,1,2])
np2 = np.array([10, 20, 30, 40, 50])
print(f'np0 : {np0}')
print(f'np1 : {np1}')
print(f'np2 : {np2}')
print()


print(f'Addition : np.add(np0, np2)')
print(f'np.add(np0, np2) : {np.add(np0, np2)}')  
print()


print(f'Subtraction : np.subtract(np0, np2)')
print(f'np.subtract(np0, np2) : {np.subtract(np0, np2)}')
print()


print(f'Multiplication, np.multiply(np0, np2)')
print(f'np.multiply(np0, np2) : {np.multiply(np0, np2)}') 
print()

print(f'Division : np.divide(np0, np2)')
print(f'np.divide(np0, np2) : {np.divide(np0, np2)}')
print() 


print('Power : np.power(np0, np2)')
print(f'np.power(np0, np2) : {np.power(np0, np2)}')
print()


print('Remainder : np.mod(np2, np0)')
print(f'np.mod(np2, np0) : {np.mod(np2, np0)}')
print(f'np.remainer(np2, np0) : {np.remainder(np2, np0)}')
print()


print(f'Absolute Value')
print(f'np.absolute(np1) : {np.absolute(np1)}')
print()


print(f'Square Root of Each Element')
print(f'np.sqrt(np0) : {np.sqrt(np0)}')
print()


print(f'Exponents')
print(f'np.exp(np1) : {np.exp(np1)}')
print()


print(f'Min/Max')
print(f'np.max(np1) : {np.max(np1)}')
print(f'np.min(np1) : {np.min(np1)}')
print()


print(f'Sign Positive or Negative')
print(f'np.sign(np1) : {np.sign(np1)}')
print()


print(f'Log')
print(f'np.log(np0) : {np.log(np0)}')
print()


print('Truncate 소수이하 자리를 모두 0으로 제거한 후 return : np.trunc(nparay)')
print(f'np.trunc(np.array([-3.1666, 3.6667]) : {np.trunc(np.array([-3.1666, 3.6667]))}')
print()


print('around() 지정한 소수점 다음 자릿수에서 반올림해서 return : np.around(nparray, 소숫점 자리수)')
print(f'np.around(np.array([1.3456, 2.3456, 3.3456]), 0) : {np.around(np.array([1.3456, 2.3456, 3.3456]), 0)}')
print(f'np.around(np.array([1.3456, 2.3456, 3.3456]), 1) : {np.around(np.array([1.3456, 2.3456, 3.3456]), 1)}')
print(f'np.around(np.array([1.3456, 2.3456, 3.3456]), 2) : {np.around(np.array([1.3456, 2.3456, 3.3456]), 2)}')
print(f'np.around(np.array([1.3456, 2.3456, 3.3456]), 3) : {np.around(np.array([1.3456, 2.3456, 3.3456]), 3)}')
print()



print('floor() 소수점 자리 이하는 모두 내림하여  return : np.floor(nparray)')
print(f'np.floor(np.array([1.3456, 2.5678])) : {np.floor(np.array([1.3456, 2.5678]))}')
print(f'np.floor([1.3456, 2.5678]) : {np.floor([1.3456, 2.5678])}')
print(f'np.floor([-1.3456, -2.5678]) : {np.floor([-1.3456, -2.5678])}')
print()


print(f'ceil() 소수점 자리는 모두 큰 인티저로 올림 : np.ceil(nparray)')
print(f'np.ceil(np.array([1.3456, 2.5678])) : {np.ceil(np.array([1.3456, 2.5678]))}')
print(f'np.ceil([1.3456, 2.5678]) : {np.ceil([1.3456, 2.5678])}')
print(f'np.ceil([-1.3456, -2.5678]) : {np.ceil([-1.3456, -2.5678])}')
print()


print(f'np.sum() Summation of nparray1 and nparray2 : np.sum([nparray1, nparray2])')
print(f'np.sum([np.array([1, 2, 3]), np.array([4, 5, 6])]) : {np.sum([np.array([1,2,3]), np.array([4, 5, 6])])}')
print(f'np.sum([[1, 2, 3], [4, 5, 6]]) : {np.sum([[1,2,3], [4, 5, 6]])}')
print()


print(f'np.sum() Summation of nparray1 and nparray2 with axis = 1: np.sum([nparray1, nparray2], axis=1)')
print(f'np.sum([np.array([1, 2, 3]), np.array([4, 5, 6])], axis=1) : {np.sum([np.array([1,2,3]), np.array([4, 5, 6])], axis=1)}')
print(f'np.sum([[1, 2, 3], [4, 5, 6]], axis=1) : {np.sum([[1,2,3], [4, 5, 6]], axis=1)}')
print()


print(f'np.sum() Summation of nparray1 and nparray2 with axis = 0: np.sum([nparray1, nparray2], axis=0)')
print(f'np.sum([np.array([1, 2, 3]), np.array([4, 5, 6])], axis=0) : {np.sum([np.array([1,2,3]), np.array([4, 5, 6])], axis=0)}')
print(f'np.sum([[1, 2, 3], [4, 5, 6]], axis=0) : {np.sum([[1,2,3], [4, 5, 6]], axis=0)}')
print()


print(f'Cumulative Summation of the given nparray : np.cumsum(np.array)')
print(f'np.cumsum(np.array([1, 2, 3, 4])) : {np.cumsum(np.array([1, 2, 3, 4]))}')
print()


print(f'Products of the elements in an array, np.prod(nparray)')
print(f'np.prod(np.array([1, 2, 3, 4]) : {np.prod(np.array([1, 2, 3, 4]))}')
print()



print(f'Products of the elements in two arrays, np.prod([nparray1, nparray2])')
np1 = np.array([1, 2, 3, 4])
np2 = np.array([5, 6, 7, 8])
print(f'np1 : {np1}')
print(f'np2 : {np2}')
print(f'np.prod([np1, np2]) : {np.prod([np1, np2])}')
print()


print(f'Products of the elements in two arrays with axis = 1, np.prod([nparray1, nparray2], axis=1)')
print(f'axis=1 means the column is collapsed.')
np1 = np.array([1, 2, 3, 4])
np2 = np.array([5, 6, 7, 8])
print(f'np1 : {np1}')
print(f'np2 : {np2}')
print(f'np.prod([np1, np2], axis=1) : {np.prod([np1, np2], axis=1)}')
print()


print(f'Products of the elements in two arrays with axis = 0, np.prod([nparray1, nparray2], axis=0)')
print(f'axis=0 means the row is collapsed.')
np1 = np.array([1, 2, 3, 4])
np2 = np.array([5, 6, 7, 8])
print(f'np1 : {np1}')
print(f'np2 : {np2}')
print(f'np.prod([np1, np2], axis=0) : {np.prod([np1, np2], axis=0)}')
print()


print(f'Cumulative products of all elements of the given nparray : np.cumprod(nparray)') 
np1 = np.array([1, 2, 3, 4])
np2 = np.array([5, 6, 7, 8])
print(f'np1 : {np1}')
print(f'np.cumprod(np1) : {np.cumprod(np1)}')
print()


print(f'Differences function subtract two successive elements : np.diff(nparray)')
print(f'e.g. For np.diff([1, 2, 3, 4]), it would be [2-1, 3-2, 4-3]=[1, 1, 1]')
np1 = np.array([10, 15, 25, 5])
print(f'np1 : {np1}')
print(f'np.diff(np1) : {np.diff(np1)}') 
print()


print(f'Differences function repeats n times when the parameter n is given : np.diff(nparray, n=2)')
print(f'e.g. For np.diff([1, 2, 3, 4], n=2), it would be [2-1, 3-2, 4-3]=[1, 1, 1]. Then it repeats again. So [1-1, 1-1] = [0, 0]')
np1 = np.array([10, 15, 25, 5])
print(f'np1 : {np1}')
print(f'np.diff(np1, n=2) : {np.diff(np1, n=2)}') 
print()


print(f'------------------------')
print(f'SET Operation in numpy')
print(f'------------------------')
print(f'Create Set : np.unique(nparray)')
np1 = np.array([1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 1])
print(f'np1 : {np1}')
print(f'np.unique(np1) : {np.unique(np1)}') 
print()


print(f'Finding Union  : np.union1d(arr1, arr2)')
np1 = np.array([1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 1])
np2 = np.array([4, 4, 5, 6, 6, 7, 8, 8])
print(f'np1 : {np1}')
print(f'np2 : {np2}')
print(f'np.union1d(np1, np2) : {np.union1d(np1, np2)}') 
print()



print(f'Finding Intersection  : np.intersect1d(arr1, arr2)')
np1 = np.array([1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 1])
np2 = np.array([4, 4, 5, 6, 6, 7, 8, 8])
print(f'np1 : {np1}')
print(f'np2 : {np2}')
print(f'np.intersect1d(np1, np2) : {np.intersect1d(np1, np2)}') 
print(f'To Faster computation, you can use assume_unique=True parameter after arrays are applied to unique() operation')
print()


print(f'Finding Difference(A-B)  : np.setdiff1d(arr1, arr2)')
np1 = np.array([1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 1])
np2 = np.array([4, 4, 5, 6, 6, 7, 8, 8])
print(f'np1 : {np1}')
print(f'np2 : {np2}')
print(f'np.setdiff1d(np1, np2) : {np.setdiff1d(np1, np2)}') 
print(f'To Faster computation, you can use assume_unique=True parameter after arrays are applied to unique() operation')
print()
print()


print(f'Finding Symmetric Difference  : np.setxor1d(arr1, arr2)')
np1 = np.array([1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 1])
np2 = np.array([4, 4, 5, 6, 6, 7, 8, 8])
print(f'np1 : {np1}')
print(f'np2 : {np2}')
print(f'np.setxor1d(np1, np2) : {np.setxor1d(np1, np2)}') 
print(f'To Faster computation, you can use assume_unique=True parameter after arrays are applied to unique() operation')
print()
print()





print(f'------------------------')
print(f'Copy vs View')
print(f'------------------------')
print()
print(f'Copy is a deep copy while View is a shallow copy.')
print()

# Create a Copy
np1 = np.array([0, 1, 2, 3, 4, 5])
np2 = np1.copy()
print(f'Original NP1 {np1}')
print(f'np2 = np1.copy()')
print(f'NP2 created with copy() : {np2}')

np2[0] = 55
print(f'np2[0] = 55')
print(f'NP1 has not been changed. :  {np1}')
print(f'NP2 has been changed:  {np2}')
print()

# Create a view
np2 = np1.view()

print(f'Original NP1 {np1}')
print(f'np2 = np1.view()')
print(f'NP2 created with view() : {np2}')

np2[0] = 55
print(f'np2[0] = 55')
print(f'NP1 has been changed. :  {np1}')
print(f'NP2 has been changed. :  {np2}')
print()



print()
print(f'----------------------------')
print(f'shape, reshape() & flatten()')
print(f'----------------------------')
print()
print(f'shape : 맨 오른쪽에 있는 값이 어레이 맨 안쪽의 element 갯수임')
print(f'(m, n) : n 칼럼의 갯수, m 행의 갯수')
print(f'(l, m, n ) : 맨 안쪽 어레이 갯수 n, 두번째 어레이 갯수 m, 맨 바깥쪽 어레이 갯수 : l') 
print()

np1 = np.array(range(1, 13))
print(f'np1 : {np1}')
print(f'np1.shape : {np1.shape}')
print()

np2 = np.array([
		[1, 2, 3, 4, 5, 6], 
		[7, 8, 9, 10, 11, 12], 
	       ])
print(f'2D array np2 :')
print(f'{np2}')
print(f'np2.shape : {np2.shape}')
print()


np3 = np1.reshape(3, 4)
print(f'np3 = np1.reshape(3, 4) :')
print(f'{np3}')
print(f'np3.shape : {np3.shape}')
print()


np4 = np1.reshape(2, 3, 2)
print(f'np4 = np1.reshape(2, 3, 2) :')
print(f'{np4}')
print(f'np4.shape : {np4.shape}')
print()




print(f'-1 is the unknown dimension in reshape') 
print(f'You do not have to specify an exact number for one of the dimensions in the reshape method. Pass -1 as the value, and NumPy will calculate this number for you.')
np5 = np4.reshape(-1) 
print(f'np4.reshape(-1) : ')
print(f'{np5}')
print(f'np5.shape : {np5.shape}')
print()

np6 = np4.flatten()
print(f'np4.flatten() : ')
print(f'{np6}')
print(f'np6.shape : {np6.shape}')
print(f'flatten() is the same as reshape(-1)')
print()
print()


np7 = np4.reshape(3, 2, -1)
print(f'np4.reshape(3, 2, -1)')
print(f'{np7}')
print(f'np4.reshape(3, 2, -1).shape : {np4.reshape(3, 2, -1).shape}')
print()

np8 = np4.reshape(-1, 3, 1)
print(f'np4.reshape(-1, 3, 1) :')
print(f'{np8}')
print(f'np4.reshape(-1, 3, 1).shape : {np4.reshape(-1, 3, 1).shape}')
print()
print()







print()
print(f'----------------------------')
print(f'Iteration')
print(f'----------------------------')
print(f'The function nditer() is a helping function that can be used from very basic to very advanced iterations.')
print(f'In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.')

np1 = np.array(range(1, 13))
np1 = np1.reshape(2, 2, 3)
print(f'np1 : ')
print(f'{np1}')

for x in np.nditer(np1) : 
	print(x)
print()


np2 = np1.reshape(4, 3)
print(f'double for loop')
for x in np2 :
    print('Print a Row', end=': ') 
    print(x)
    for y in x : 
        print(y)

print()
print()
print(f'Print numpy as a string with nditer()')
print(f'We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.')
print(f'NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=[''buffered'']')

np1 = np.array([1, 2, 3])
print(f'np1 : {np1}')
for x in np.nditer(np1, flags=['buffered'], op_dtypes=['S']):
    print(x)
print()


print(f'enumerate in Numpy using np.ndenumerat() -----------------')
np1 = np.array([1, 2, 3])
print(f'np1 : {np1}')
for idx, x in np.ndenumerate(np1):
    print(idx, x)

np2 = np.array(range(1, 13))
np2 = np2.reshape(4, 3)
print(f'np2 : ')
print(f'{np2}')
for idx, x in np.ndenumerate(np2):
    print(idx, x)



print()
print(f'----------------------------')
print(f'Join two nparrays')
print(f'----------------------------')
print()
print()

print(f'------')
print('concatenate((nparray1, nparray2)) is to horizontal stack.')
print('concatenate((nparray1, nparray2), axis=0)')
print(f'axis=0 can be ignored.')
print(f'concatenate() is equal to horizontal stack')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(f'arr1 : {arr1}')
print(f'arr2 : {arr2}')
arr = np.concatenate((arr1, arr2))
print(f'np.concatenate((arr1, arr2)) :')
print(arr)
print()


print(f'concatenate((array1, array2), axis=1) is to vertical stack.')
print('concatenate((nparray1, nparray2), axis=1)')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(f'arr1 : {arr1}')
print(f'arr2 : {arr2}')
print(f'np.concatenate((arr1, arr2), axis=1) :')
print(f'When array is 1-D, ''axis=1'' generates error.')
print()


print(f'------')
print('concatenate((nparray1, nparray2), axis=0)')
print('When concatenate() with axis = 0 applied to 2D array, it means vertical stack')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print('arr1 : ')
print(arr1)
print('arr2 : ')
print(arr2)
arr = np.concatenate((arr1, arr2), axis=0)
print(f'np.concatenate((arr1, arr2), axis=0) : ')
print(arr)


print()
print('concatenate((nparray1, nparray2), axis=1)')
print('When concatenate() with axis = 1 applied to 2D array, it means horizontal stack')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print('arr1 : ')
print(arr1)
print('arr2 : ')
print(arr2)
arr = np.concatenate((arr1, arr2), axis=1)
print(f'np.concatenate((arr1, arr2), axis=1) : ')
print(arr)
print()
print()



print(f'------')
print('stack((nparray1, nparray2), axis=1) to 1D array is to horizontal stack.')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)
print('WORKING HERE')
print('****************')
print('****************')
print('****************')
print('****************')
print('****************')





# To Do : Stacking with axis, vstack, hstack, 
# https://www.w3schools.com/python/numpy/numpy_array_join.asp
# 여기서 스터디 할 것 확인하고 아래 진행  


# To Do : From 7_s.py 
# 참고 : https://www.w3schools.com/python/numpy/numpy_ufunc_differences.asp




# ---------------------------------------
# 7_sorting
# ---------------------------------------
print(f'------------------------------')
print(f'Sorting')
print(f'------------------------------')


np1 = np.array([6, 7, 4, 9, 0, 2, 1])
print(f'np1 : {np1}')
print(f'np.sort(np1) : {np.sort(np1)}')
print()
print('Alphabetical Sorting')
np2 = np.array(['John', 'Tina', 'Aaron', 'Zed'])
print(f'np2 : {np2}')
print(f'np.sort(np2) : {np.sort(np2)}')
print(f'np2 : {np2}')
print(f'np.sort() returns a copy of the origina and does not change of the original')
print()

np3 = np.array([ [6, 7, 1, 9], 
                 [8, 3, 5, 0]])

print(f'np3 :')
print(np3)
print(f'np.sort(np3) : ')
print(f'{np.sort(np3)}')
print('\n\n')
# -----------------
# 8_searcher.py
# -----------------
print(f'------------------------------')
print(f'Search : np.where()')
print(f'------------------------------')

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3])
print(f'np1 : {np1}')

x = np.where(np1 ==3)
print(f'x = np.where(np1==3) : {x}')
print(x)
print(f'type(x[0]) : {type(x[0])}')
print(f'len(x) : {len(x)}')


print(f'x[0] : {x[0]}')
print(f'np1[x[0]] : {np1[x[0]]}')
print()


print(f'Return Even Elements')
y = np.where(np1 % 2 == 0)
print(f'np1 : {np1}')
print(f'y = np.where(np1 % 2 == 0) : {y}')
print(f'y[0] : {y[0]}')
print(f'np1[y[0]] : {np1[y[0]]}')
print()
print()


#------------------------------------
# 9_filtering.py
#------------------------------------
print(f'-----------------------------')
print(f'Filtering with boolean index')
print(f'------------------------------')

np1 = np.array(range(1, 11))
print(f'np1 : {np1}')

# It is faster than brutal search using for loop)
print(f'It is faster than brutal search using for loop')
print()
filtered = np1 > 5 
print(f'filtered = np1 > 5 : {filtered}')
print(f'filtered : {filtered}')
print(f'np1[filtered] : {np1[filtered]}')
print()
print()















