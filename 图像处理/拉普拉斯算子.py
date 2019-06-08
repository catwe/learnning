import math
import numpy as np
I = np.array([[2,1,7,5,8,9,1,3],[3,5,1,2,1,10,1,1],[1,6,5,6,5,1,1,7],[7,1,5,1,5,1,8,1],[9,1,1,5,2,5,2,3],[1,2,6,3,1,1,8,1],
              [3,6,1,8,12,5,1,9],[7,8,3,9,1,7,8,1]])
otherArry = np.ones([8,8])

first = I
for i in range(1,7):
	for x in range(1,7):
		K = I[i][x]
		I[i][x] = round((I[i][x+1] + I[i][x-1] +I[i+1][x] + I[i-1][x]-4*I[i][x]))
		# print(I)
		otherArry[i][x]=I[i][x]
		I[i][x] = K

for x in range(8):
	otherArry[0][x]=first[0][x]
	otherArry[x][0]=first[x][0]
	otherArry[7][x]=first[7][x]
	otherArry[x][7] = first[x][7]
print(otherArry)


