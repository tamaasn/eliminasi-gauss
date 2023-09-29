import numpy as np

A = np.array([[1,2,3,5] , [2,5,3,3] , [1,0,8,17]])

print("Matriks Augmented")
print("A =" ,A)

n =len(A)
m = np.zeros((n,n))

for i in range(0,n):
	for j in range(i+1,n):
		m[j][i]=A[j][i]/A[i][i]
		s = m[j][i]
		for k in range(0,n+1):
			A[j][k] = A[j][k]-s*A[i][k]
		
print("Matriks Eselon Baris")
print(A)

x= np.zeros((n,1))
x[n-1][0]=A[n-1][n]/A[n-1][n-1]
for i in range(n-2,-1,-1):
	S=0
	for j in range(i+1,n):
		S = S + A[i][j] * x[j][0]
		x[i][0] = (A[i][n]-S)/A[i][i]

print("Solusi")
print(x)
