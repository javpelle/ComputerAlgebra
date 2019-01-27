def euclid_extended (a, b, first=True):
    '''
    Algoritmo extendido de euclides (Identidad de Bezout). 
    Resuelve la identidad:
    
    	mcd(a,b) = a*s + b*t

    Devuelve el resultado en el formato (r,(s,t)).
    
    La versión del algorimo usada es la que viene en 
    [wikipedia][algoritmo], que usa matrices para resolver
    las ecuaciones. 

    Con esta versión, basta con devolver las matrices y usar
    el álgebra de sage para multiplicarlas. 

    [algoritmo]: <https://es.wikipedia.org/wiki/Algoritmo_de_Euclides#Algoritmo_de_Euclides_extendido>
    '''
    
    # Caso base, a := mcd y delvolvemos la identidad
    # Esto da lugar a una iteración más respecto al [algoritmo],
    # ya que éste para cuando r == mcd, no cuando a == mcd && r==0,
    # con lo que el restultado está en la file 0, no en la 1.
    if b == 0: return Matrix([[1,0],[0,1]])

    (q, r) = a.quo_rem (b)
    Q_i = Matrix ([[0,1],[1, -q]]) 

    # Continuamos iterando y el resultado lo multiplicamos
    M = euclid_extended (b , r, False) * Q_i 

    # If this is the entry point, return the pair (mcd, (s,t))
    if first: 
        m = M[0]
        return (a*m[0]+ b*m[1], m)

    return M


def eprint(a,b,m): 
    '''Function to pretty print tests'''
    (m,(s,t)) = m
    form = "{0} = ({1})({3}) + ({2})*({4})"
    print form.format('mcd','a','b','s','t'),"==>", form.format(m,a,b,s,t)

eprint(9,6,euclid_extended(9,6))

R.<x> = PolynomialRing(ZZ)
eprint(x^2+x,x,euclid_extended(x^2+x,x))
eprint(18*x,30*x,euclid_extended(18*x,30*x))
eprint(12*x^3-28*x^2+20*x-4,
       -12*x^2+10*x-2,euclid_extended(12*x^3-28*x^2+20*x-4,-12*x^2+10*x-2))
eprint(5,67,euclid_extended(5,67))
