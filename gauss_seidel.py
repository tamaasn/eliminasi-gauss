def seidel(a, x ,b):        
    n = len(a)                    
    for j in range(0, n):         
        # temp variable d to store b[j] 
        d = b[j]                   

        # to calculate respective xi, yi, zi 
        for i in range(0, n):
        	if (i != j):
        		d-=a[j][i] * x[i] ;print(d)
        # updating the value of our solution         
        x[j] = d / a[j][j]        
    return x

print("Implementasi gauss seidel\nMuhammad Akmal Sani Pratama\nNIM : 23106050036")
x = [0, 0, 0]                         
a = [[4.0, 1.0, 2.0],[6.0, 5.0, 1.0],[1.0, 1.0, 3.0]] 
b = [4.0,7.0,3.0]
max_iterator = int(input("Masukkan iterator maksimal : "))
for i in range(0 , max_iterator):
	x = seidel(a, x, b)
print("x1, x2, x3 = ",x)
