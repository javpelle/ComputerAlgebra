def fast_exp(x, e):
	if e==0: 
		return 1
	elif e==1: 
		return x
	elif e%2==0: 
		return fast_exp(x*x,e//2)
	else: 
		return x*fast_exp(x*x,e//2)

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

def irreducibility_test(f,q):
	'''
	Versión ineficiente tomada del Shoup pag. 463. Intentar mejorar con 
	composición modular y exponenciación rápida
	'''  
	h = (x) % f
	l = f.degree()
	for k in range(1,l//2+1):
		h = fast_exp_mod(h,q,f)
		if gcd(h-x, f) != 1: return False
	return True
	 
R.<x>=PolynomialRing(GF(2))
f = x^21+x^2+1
print "El polinomio ", f, " es irreducible en F2[x]?: ", irreducibility_test(f,2), " ", f.is_irreducible()
g = R.random_element(50)
print "El polinomio ", g, " es irreducible en F2[x]?: ", irreducibility_test(g,2), " ", g.is_irreducible()  	
