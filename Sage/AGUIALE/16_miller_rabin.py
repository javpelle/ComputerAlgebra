
'''
Algoritmo de primalidad de Miller-Rabin. En primer lugar, probamos a dividir con
primos pequeños (hasta 100). Si falla con todos ellos, empezamos a hacer rondas
de Miller-Rabin
'''

def fast_exp_mod(b,e,m):
	'''
	Devuelve b^e mod m. Tomado de Wikipedia
	'''	
	r = 1
	b = b%m
	while e>0:
		if e%2 == 1:
			r = (r*b)%m
		e = e//2
		b  = (b*b)%m
	return r




small_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,
83,89,97]


'''
Función que hace pasar al número k rondas del test de primalidad
'''
def probably_prime(n,k):
	if n<2: return False
	for p in small_primes:
		if n < p * p: return True
		if n % p == 0: return False
	d = n-1
	s=0

	#Escribimos n-1 de la forma (2^s)*d
	while d%2==0:
		s=s+1
		d=d//2
		
	for _ in range(k):
		a=ZZ.random_element(2,n-2)
		x=fast_exp_mod(a,d,n)
		if x==1 or x==n-1: continue
		
		composite=True
		for _ in range(s-1):
			x = (x*x)%n
			if x==1: return False
			if x==n-1:
				composite=False	
				break  
		if composite: return False
	return True


print probably_prime(633910111,3) #Es primo
print probably_prime(961748941,3) #Es primo
print probably_prime(609662377943442451,3) #No es primo (producto de los dos anteriores)

print probably_prime(651693055693681,3) #Número de Carmichael 72931*87517*102103
										#Con 1 prueba, falla 12% de las veces
										#Con 2, un 1.5%
										#Con 3, un 0.2%
