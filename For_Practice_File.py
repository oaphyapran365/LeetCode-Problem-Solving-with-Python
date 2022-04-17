
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

#A[:] = zip(*A[::-1])


# a = 'abc'

# b = 'bbb'

# #a[:] = b

# print(a[::-1])



A = [[1,2,3],[4,5,6],[7,8,9]]
A[:] = zip(*A[::-1])


#A[:] = list(zip(A[::-1]))
print(A)
#print(list(A))

# print(*A[::-1])



