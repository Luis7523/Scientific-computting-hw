#Febrero 16 de 2015
#Luis Miguel Parra Rueda

def minimum (x, y):
	if x<y:
		return x
	else:
		return y

def mcd (x, y):
	m = minimum (x,y)
	for i in range (m, 0,-1):
		if x%i == 0 and y%i ==0:
			return i

def arecoprime (a,b):

	m = mcd (a,b)

	if m==1:
		return 1
	else:
		return 0 

print arecoprime (14,3)
