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

def nullspace_basis(M,n):

	R=M.base_ring()
	for k in range(n):
		#buscar pivote
		#print M
		#print
		i=k
		while i<n and M[k,i]==0: i=i+1
		
		if i<n:
			pivot=M[k,i]
			inv_pivot=pivot^-1
			M.set_col_to_multiple_of_col(i,i,inv_pivot) #No me convence, pero no encuentro otra forma
			'''			
			for j in range(n):
				M[j,i]=M[j,i]//pivot #normalizamos la columna
				
			'''

			if i!=k: 
				M.swap_columns(i,k)
				'''
				for j in range(n): #la cambiamos a la posición k				
					aux=M[j,i] 
					M[j,i]=M[j,k]
					M[j,k]=aux
				'''
			#anulamos el resto de la fila k
			for j in range(n): #para cada columna que no sea la j
				aux=-M[k,j]
				if k!=j: 
					M.add_multiple_of_column(j,k,aux)				
				
				'''				
				if k!=j:
					for l in range(n): #para cada elemento de esa columna
						M[l,j]=M[l,j]-M[k,j]
				'''

	#Hacemos M=I-M (como sabemos la forma de M, 
	# aseguramos que (1,0,...,0) esté en la base)
	for i in range(n):
		for j in range(n):
			if i==j: M[i,j]=1-M[i,j]
			else: M[i,j]=-M[i,j]

	#print M
	#Leemos las filas no nulas de M-I	
	v=[]
	for i in range(n):
		nonzero=False
		for j in range(n):
			if M[i,j]!=0: 
				nonzero=True

		if nonzero: 
			v.append(M[i])
		
	return v					 
	

def berlekamp(f,q):
	'''
	Algoritmo de Berlakamp. Ver Modern Computer Algebra algoritmo 14.31
	INPUT: f polinomio mónico libre de cuadrados en Fq[x]
	       q Potencia prima impar
	OUTPUT: g factor propio de f o "failure"
	'''

	R=f.base_ring()
	RX=f.parent()
	n=f.degree()
	pol=1
	aux=fast_exp_mod(x,q,f)
	Q=matrix(R,n,n)
	
	#Rellenamos Q de forma que Q[i,j]:= coeficiente de (x^j) en (x^(qi) mod f)

	for i in range(n):
		for j in range(n): Q[i,j]=0

	#Rellenamos la primera fila "a mano"
	Q[0,0]=1

	#En cada iteración calculamos (x^(qi) mod f) y rellenamos su fila de Q
	for i in range(1,n):
		pol=(pol*aux)%f
		for j in range(pol.degree()+1): Q[i,j]=pol[j]

	#Calculamos Q-I
	for i in range(n): Q[i,i]=Q[i,i]-1

	#Q.echelonize()	#Efectúa transformación de Gauss
	#Q_rank = Q.rank()
	#if Q_rank==1 return f
	
	


	'''
	Calculamos el Ker(Q) con funciones de Sage. Intentar cambiarlo por un cálculo a mano
	para que no quede tan cutre
	'''
	'''
	K=Q.kernel()
	B=K.basis_matrix()
	dim=K.dimension()

	if (dimension==1): return f
	'''

	B=nullspace_basis(Q,n)
	dim=len(B)	
	
	if (dim==1): return f
	
	C=random_vector(R,dim)

	a=RX([0])
	for i in range(dim): a=a+C[i]*RX(B[i].list()) #debería funcionar        
	g1=gcd(a,f)
	#print "a= ", a, " dim=  ", dim
	#print Q

	if g1!=1 and g1!=f: return g1
	
	b=fast_exp_mod(a, ((q-1)//2), f)
	g2=gcd(b-1,f)
	if g2!=1 and g2!=f: return g2
	else: return "failure"

R.<x>=PolynomialRing(GF(7))
f=R.random_element((4,10))
print "f = ", f
g=berlekamp(f,7)
if g!="failure": 
    print "g = ",g
    h=f/g
    print "h = ", h
    print "g*h = ", g*h
else: print "failure"	

	  		

	  		
