def chinese_remainder(l):

	'''
	Algoritmo del teorema chino del resto. Recibe una lista de pares (mi,vi) y
	devuelve un elemento f tal que f=vi mod mi para todo i. Los mi deben ser
	coprimos. Algoritmo sacado de Modern Computer Algebra, Algoritmo 5.4
	OBSERVACIÓN: La versión del libro no devuelve el menor, pero como es único
	módulo m1*m2*...*mr, se puede hallar haciendo un módulo
	'''

	m=1
	
	for (mi,vi) in l:
		m=m*mi
	
	res=0
	
	for i in range(len(l)):
		m_i=l[i][0]	
		v_i=l[i][1]	
		aux=m/m_i
		#Uso el euclides predefinido de sage, pero se puede meter el nuestro
		d,s,t=xgcd(aux,m_i)
		c_i = (v_i*s)%m_i
		res = res + c_i*aux
		
	return res



print "resto chino ", [(2,1),(3,1),(5,4),(7,0)], " = " , chinese_remainder([(2,1),(3,1),(5,4),(7,0)])


