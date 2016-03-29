#Problemas que mando carlos
#Luis Miguel Parra Rueda

def isprime (k):
	for i in range (2,k):
		if k % i == 0:
			return 0
	return 1

def GB(N):
	for p in range(N):	
		for q in range(N):
			if isprime (q) == 1:
				if isprime (p) == 1:


		
