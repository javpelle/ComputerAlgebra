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


def eq_degree_splitting(f,q,d):
	'''
	Ver modern computer algebra, algoritmo 14.8. 
	INPUT: polinomio mónico libre de cuadrados f de grado n, q potencia prima impar, 
	d<n t.q. d|n y todos los factores irreducibles de f tienen grado d.
	OUTPUT: g factor mónico propio de f o "failure"
	'''

	R=f.parent()
	a=R.random_element((0,q-1))
	
	#print a

	if (a.degree()<1): return "failure"

	g1=gcd(a,f)
	if (g1!=1): return g1

	qd = fast_exp(q,d)
	b = fast_exp_mod(a, ((qd-1)//2), f)
	
	g2=gcd(b-1,f)  
	if (g2!=1 and g2!=f): return g2
	else: return "failure"
	
def eq_degree_factorization(f,q,d):
	'''
	Ver modern computer algebra, algoritmo 14.10 
	INPUT: polinomio mónico libre de cuadrados f de grado n, q potencia prima impar, 
	d<n t.q. d|n y todos los factores irreducibles de f tienen grado d.
	OUTPUT: Los factores mónicos irreducibles de f 
	'''
	
	if (f.degree()==d): return [f]
	#success=False
	while(True):
		g=eq_degree_splitting(f,q,d)
		if (g!="failure"): break
	return eq_degree_factorization(g,q,d)+eq_degree_factorization(f//g,q,d)

def poly_fact_finite_field(f,q):
	'''
	Ver modern computer algebra, algoritmo 14.13
	INPUT: polinomio f no constante en Fq[x], q potencia prima impar
	OUTPUT: factores mónicos irreducibles de f y sus multiplicidades
	'''
	R=f.parent()
	h=x
	v=f/f.leading_coefficient() #comprobar que esto se escribe así
	i=0
	U=[]
	while (True): #cambiar por do-while que no se como es en Python
		#print "... ",i
		i=i+1
		h=fast_exp_mod(h,q,f)
		g=gcd(h-x,v)
		if (g!=1):
			G=eq_degree_factorization(g,q,i)		 

			for gj in G:
				e=0
				while((v%gj)==0):
					#print "... " , v
					v=v//gj #comprobar que la división se hace así
					e=e+1
				U=U+[(gj,e)]

		if (v==1): break #cutre, intentar cambiar por do-while
	
	return U

R.<x>=PolynomialRing(GF(3))
#f=x^4+x^3+x-1
f=x^8+x^7-x^6+x^5-x^3-x^2-x

print poly_fact_finite_field(f,3) 
#print eq_degree_factorization(f,3,1)
							




