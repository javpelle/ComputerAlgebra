
# coding: utf-8

# In[151]:


get_ipython().magic(u'display latex')


# <h1><p style="color:#16A085"> Álgebra Computacional </p style></h1>
# 
# Algoritmos realizados por Luis Aguirre Galindo y Javier Pellejero Ortega del Doble Grado de Matemáticas e Ingeniería Informática para la asignatura Álgebra Computacional.
# 
# <h2> Índice </h2>
# 
# - 1. Algoritmo de Euclides
#     - 1.1 Algoritmo de Euclides para un Dominio Euclídeo
#     - 1.2 Algoritmo de Euclides extendido para un Dominio Euclídeo
#     - 1.3 Ejemplos en $\mathbb{Z}$
#     - 1.4 Ejemplos en $\mathbb{Q}[x]$
#     - 1.5 Ejemplos en $\mathbb{F}(7)[x]$
# - 2. Teorema chino del resto
#     - 2.1 Ejemplos en $\mathbb{Z}$
# - 3. MCD en DFU
#     - 3.1 Ejemplos en $\mathbb{Z}[x]$
# - 4. Inverso de un elemento en un cuerpo finito
#     - 4.1 Ejemplos en $\mathbb{Z}_p$
# - 5. Test de irreducibilidad de un polinomio en $\mathbb{F}_q[x]$
#     - 5.1 Ejemplos en $\mathbb{F}(7^2)[x]$
# - 6. Logaritmo discreto en cuerpos $\mathbb{F}_q[x]/(f(x))$
#     - 6.1 Ejemplos en $\mathbb{F}(3^6)[x]/(bx + 2b)$
# - 7. Algoritmo de factorización de un polinomio en cuerpo finito
#     - 7.1 Equal degree-splitting
#     - 7.2 Equal degree-factorization
#     - 7.3 Algoritmo de factorización de un polinomio en cuerpo finito
#     - 7.4 Ejemplos en $\mathbb{F}(3)[x]$
# - 8. Algoritmo de factorización de Berlekamp en cuerpo finito
#     - 8.1 Ejemplos en $\mathbb{F}(7)[x]$
# - 9. Algoritmos de factorización en $\mathbb{Z}[x]$
#     - 9.1 Ejemplo en $\mathbb{Z}[x]$ con modularidad 625
# - 10. Algoritmo de primalidad de *AKS*
#     - 10.1 Ejemplos

# # 1. Algoritmo de Euclides

# # 1.1 Algoritmo de Euclides para un Dominio Euclídeo

# In[2]:


def euclides(a, b, mod):
    # a y b son elementos de un DE y mod la función que devuelve el módulo de ese DE
    # Devuelve gcd
    if (b == 0):
        return a
    else:
        return euclides (b, (mod(a, b)), mod)


# ## 1.2 Algoritmo de Euclides extendido para un Dominio Euclídeo

# In[3]:


def extendedEuclides(a, b, div_mod):
    # a y b son elementos de un DE y div_mod la función que devuelve la dupla cociente, módulo de ese DE
    # Devuelve gcd, s, t que verifica gcd = a*s + b*t
    if (b == 0):
        return a, 1, 0 
    else:
        q, r = div_mod(a, b)
        gcd, d, e = extendedEuclides(b, r, div_mod)
        return gcd, e, (d -q * e)


# ## 1.3 Ejemplos en $\mathbb{Z}$

# In[111]:


def mod_int(a, b): return a % b
def div_mod_int(a, b): return a // b, a % b

def euclides_int(f, g):
    return euclides(f, g, mod_int)

def extendedEuclides_int(f, g):
    return extendedEuclides(f, g, div_mod_int)

print(euclides_int(55, 22))
print(extendedEuclides(55, 22, div_mod_int))


# ## 1.4 Ejemplos en $\mathbb{Q}[x]$

# In[5]:


def div_mod_pol(a, b): return a.quo_rem(b);
def mod_pol(a, b): _, r =  div_mod_pol(a, b); return r

def euclides_pol(f, g):
    return euclides(f, g, mod_pol).monic()

def extendedEuclides_pol(f, g):
    gcd, s, t = extendedEuclides(f, g, div_mod_pol)
    k = gcd.leading_coefficient()
    return gcd.monic(), s / k, t / k
    
R.<x> = QQ[]

a = (x^2 +2*x + 1)
b =  (x^2 - 1)
c = (x+2/3)*(x-3/2)*(x^2+1)
d = (x+2/3)*(x+2/3)*(x^2+1)

print(euclides_pol(a, b))
print(extendedEuclides_pol(a, c))
print(extendedEuclides_pol(c, d))


# ## 1.5 Ejemplos en $\mathbb{F}(7)[x]$

# In[6]:


R.<x> = PolynomialRing(FiniteField(7))
f = R.random_element(3)
g = R.random_element(3)

print(extendedEuclides_pol(f, g))


# # 2. Teorema chino del resto

# In[7]:


def chineseRemainder(coprimes, elems, div_mod, rem):
    # coprimes: n elementos de un DE coprimos entre sí
    # elems: n elemes cualesquiera de un DE
    # div _mod: función que devuelve la dupla cociente, módulo
    # rem: función que devuelve la operación rem (similar a módulo) de un DE
    # Devuelve elemento del DE que verifica f ≡ elem_i mod coprimes_i para todo 0 ≤ i < n 
    m = 1
    for mi in coprimes:
        m = m * mi
    result = 0;
    for i in range(len(coprimes)):
        n = m / coprimes[i]
        _, a, _ = extendedEuclides(n, coprimes[i], div_mod)
        c = rem((a * elems[i]), coprimes[i])
        result = c * n + result
    return result


# ## 2.1 Ejemplos en $\mathbb{Z}$

# In[148]:


def rem(a, b):
    r = abs(a) % abs(b)
    return r if a >= 0 else -r
print chineseRemainder([3,5,7],[4,5,33], div_mod_int, rem)


# # 3. MCD en DFU

# In[149]:


def gcdDFU(a, b):
    # a y b: elementos del DFU sobre los que se calcula el MCD
    # Devuelve gcd(a, b)
    if a.degree() < b.degree():
        return mcdDFU(b, a)
    while b != 0:
        q, r = (b.leading_coefficient()**(a.degree() - b.degree() + 1) * a).quo_rem(b)
        a = b
        b = r
    return a


# ## 3.1 Ejemplos en $\mathbb{Z}[x]$

# In[150]:


R.<x> = ZZ[]
a = (x + 1)**2
b = (x + 1)*(x - 1)
print gcdDFU(a, b).monic()


# # 4. Inverso de un elemento en un cuerpo finito

# In[124]:


def inverseFiniteField(a):
    # a: elemento de un cuerpo
    # Devuelve inverso de a en field
    azz = ZZ(a)
    field = a.parent()
    _, _, b = extendedEuclides_int(field.cardinality(), azz)
    return field(b)


# ## 4.1 Ejemplos en $\mathbb{Z}_p$

# In[129]:


Z7 = Integers(7)
a = Z7(3)
print inverseFiniteField(a)

Z31 = Integers(31)
b = Z31(14)
print inverseFiniteField(b)

Z61 = Integers(61)
c = Z61(27)
print inverseFiniteField(c)


# # 5. Test de irreducibilidad de un polinomio en $\mathbb{F}_q[x]$

# In[13]:


def fast_exp_mod(b,e,m):
#Devuelve b^e mod m.
    r = 1
    b = b % m
    while e > 0:
        if e % 2 == 1:
            r = (r * b) % m
        e = e // 2
        b  = (b * b) % m
    return r 

def irreducibility_test(f, q):
    # Sacado de Shoup
    # f elemento de Fq
    # q entero de la forma p^n con p primo y n  natural
    # Devuelve True si irreducible, False en otro caso
    h = (x) % f
    l = f.degree()
    for k in range(1, l // 2 + 1):
        h = fast_exp_mod(h, q, f)
        if gcd(h - x, f) != 1: return False
    return True


# ## 5.1 Ejemplos en $\mathbb{F}(7^2)[x]$

# In[14]:


order = 49
R.<x>=PolynomialRing(GF(order, 'z'))
f = x^21+x^2+1
print "El polinomio ", f, " es irreducible en F49[x]?: ", irreducibility_test(f,order), "."
g = R.random_element(6)
print "El polinomio ", g, " es irreducible en F49[x]?: ", irreducibility_test(g,order), "."


# # 6. Logaritmo discreto en cuerpos $\mathbb{F}_q[x]/(f(x))$

# In[130]:


def baby_giant(v, g, ordG):
    # v: elemento al que se le aplica el logaritmo
    # g: base del logaritmo
    # ordG: orden de <g> 
    # Devuelve el logaritmo
    
    m = ceil(sqrt(ordG))

    #  Generamos baby = { g^(j): 0 <= j < n }
    baby = [g^0]
    for i in  xrange(1,m): baby.append( baby[i-1]*g )
    
    # Generamos giant = { h*g^(-i): 0 <= i < w }
    giant = [v]
    inv_gm = g^(-m)
    for i in  xrange(1,m): giant.append( giant[i-1]*inv_gm )
     
    # Tomamos los elementos que están simultáneamente en baby y giant
    # Nos quedamos con el que tenga menor índice en giant.
    # Para ese índice, calculamos x = j*m + i
    # Si la intersección es vacía, no existe el logaritmo
    intersection = set(baby).intersection(set(giant))
    if len(intersection) == 0: 
        print ("No existe logaritmo discreto de %s en base " +         "%s") % (v,g)
    else:
        b = len(giant)
        for inters in intersection:
            if giant.index(inters) < b:
                b = giant.index(inters)
                a = baby.index(inters)
                x = a+b*m
        
        #print  'x = a + b*m= (%s) + (%s)*(%d) = (%s)' % (a,b,m,x)  
        return x


# ## 6.1 Ejemplos en $\mathbb{F}(3^6)[x]/(bx + 2b)$

# In[131]:


K.<b> = GF(3^6)
R.<x> = PolynomialRing(K)
f = b*x + 2*b # polinomio de K[x]
I = R.ideal([f]) # ideal generado por bx + 2b
Q = R.quotient_ring(I) # K[x]/f(x)

Ax = Q(b*x^3 + x + b)
ordA = order_from_multiple(Ax,Q.order(),operation='*',check=False)

Bx = Ax^245
Cx = Q(x^2 + b)

print(baby_giant(Bx,Ax,ordA))
print(baby_giant(Cx,Ax,ordA))


# # 7. Algoritmo de factorización de un polinomio en cuerpo finito

# ## 7.1 Equal degree-splitting

# In[17]:


def eq_degree_splitting(f, q, d):
    # f: polinomio mónico libre de cuadrados con grado n
    # q: potencia prima impar
    # d: entero menor que n, divide a n y todos los factores irreducibles de f tienen grado d.
    # devuelve un factor mónico de f
    R = f.parent()
    a = R.random_element((1, f.degree() - 1)) # 0 < deg a < deg f
    
    g1 = gcd(a,f)
    if (g1 != 1): return g1
    
    b = fast_exp_mod(a, (q^d - 1) // 2, f)
    
    g2 = gcd(b - 1, f)  
    if (g2 != 1 and g2 != f): return g2
    else: return "failure"


# ## 7.2 Equal degree-factorization

# In[132]:


def eq_degree_factorization(f, q, d):
    # f: polinomio mónico libre de cuadrados con grado n
    # q: potencia prima impar
    # d: entero menor que n, divide a n y todos los factores irreducibles de f tienen grado d.
    # devuelve todos los factores mónicos irreducibles de f
    if (f.degree() == d): return [f]
    while(True):
        g = eq_degree_splitting(f, q, d)
        if (g != "failure"): break
    return eq_degree_factorization(g, q, d) + eq_degree_factorization(f // g, q, d)


# ## 7.3 Algoritmo de factorización de un polinomio en cuerpo finito

# In[133]:


def poly_fact_finite_field(f, q):
    # f: polinomio no constante
    # q: potencia prima impar
    # devuelve factorización de f
    R = f.parent()
    h = f.variables()[0] # variable x (para no depender de la letra)
    v = f / f.leading_coefficient()
    i = 0
    U = []
    while (True): 
        i = i + 1
        h = fast_exp_mod(h, q, f)
        g = gcd(h - f.variables()[0], v)
        if (g != 1):
            G = eq_degree_factorization(g, q, i) #Computar los factores mónicos irreducibles de g
            for gj in G:
                e = 0
                while(gcd(v, gj) != 1): # Calcular multiplicidades     
                    v = v // gj 
                    e = e + 1
                U = U + [(gj, e)] 
        if (v == 1): break
    return U


# ## 7.4 Ejemplos en $\mathbb{F}(3)[x]$

# In[135]:


R.<x>=PolynomialRing(GF(3))
f=x^4+x^3+x-1
f2=x^8+x^7-x^6+x^5-x^3-x^2-x
print f.factor()
print poly_fact_finite_field(f,3)
print
print f2.factor()
print poly_fact_finite_field(f2,3)


# # 8. Algoritmo de factorización de Berlekamp en cuerpo finito
# 

# In[57]:


def berlekamp(f, q):
    # f: polinomio no constante
    # q: potencia prima impar
    # devuelve un factor de f
    R = f.base_ring()
    RX = f.parent()
    n = f.degree()
    pol = 1
    aux = fast_exp_mod(f.variables()[0], q, f)
    Q = matrix(R, n, n)

    # Rellenamos Q de forma que Q[i,j]:= coeficiente de (x^j) en (x^(qi) mod f)

    for i in range(n):
        for j in range(n): Q[i, j] = 0

    # Rellenamos 1er elemento para completar la primera fila
    Q[0, 0] = 1

    # En cada iteración calculamos (x^(qi) mod f) y rellenamos la fila i-ésima de Q
    for i in range(1,n):
        pol = (pol * aux) % f
        for j in range(pol.degree() + 1): 
            Q[i, j] = pol[j]

    # Calculamos Q-I
    for i in range(n): Q[i, i] = Q[i, i] - 1

    Q.echelonize() # Efectúa transformación por el metodo de eliminacion Gaussiana
    K = Q.kernel() # Espacio vectorial que conforma el núcleo
    B = K.basis_matrix() # Base de la Berlekamp algebra
    r = K.dimension() # Dimensión del núcleo

    if (r == 1): return f

    C = random_vector(R, r)

    a = RX([0]) # Inicializamos la variable, porque da error si no 
    
    for i in range(r): # Calculamos a = C1*B1 + C2*B2 + ...Cr*Br
        a = a + C[i] * RX(B[i].list()) 


    g1 = gcd(a,f)

    if g1 != 1 and g1 != f: 
        return g1

    b = fast_exp_mod(a, ((q - 1) // 2), f)
    g2 = gcd(b - 1, f)

    if g2 != 1 and g2 != f:
        return g2
    else: 
        return "failure"


# ## 8.1 Ejemplos en $\mathbb{F}(7)[x]$

# In[60]:


R.<x> = PolynomialRing(GF(7))
f = 6*x^9 + 2*x^8 + x^7 + 5*x^6 + 5*x^5 + 6*x^3 + 2*x^2 + 3
g = berlekamp(f, 7)
if g != "failure":
    print f, " = "
    print "= (", g, ") * (", f / g, ")\n"
else:
    print "No se encontró el factor. Intentelo de nuevo\n"

f = R.random_element((4, 10))
g = berlekamp(f, 7)

if g != "failure":
    print f, " = "
    print "= (", g, ") * (", f / g, ")"
else:
    print "No se encontró el factor. Intentelo de nuevo"


# # 9. Algoritmos de factorización en $\mathbb{Z}[x]$

# In[137]:


def hensel_step(p, f, g, h, s, t, m):
    # p: primo
    # f: polinomio con coeficientes en los enteros
    # g, h: polinomios con coeficientes en los enteros que verifican f = g * h mod m
    # s, t: polinomios con coeficientes en los enteros que verifican 1 = s*g + t*h mod m
    # m: elevación previa
    # Devuelve g_, h_, t_, s_ que verifican f_ = g_ * h_ mod m*p y 1 = s_*g_ + t_*h_ mod m*p
  
    m_l = p * m # la nueva elevación: m^l

    ## Resolvemos las ecuaciones modulo la base m_l

    e = (f - g * h) % m_l
    
    (q, r) = (s * e).quo_rem(h)
    (q, r) = tuple([k % m_l for k in (q,r)])

    g_ = (g + t * e + q * g) % m_l
    h_ = (h + r) % m_l


    b = (s * g_ + t * h_ - 1) % m_l

    (c, d) = (s * b).quo_rem(h_) # calculamos c,d
    (c, d) = tuple([k % m_l for k in (c , d)]) # les hacemos el módulo

    s_ = (s - d) % m_l
    t_ = (t - t*b - c*g_) % m_l

    return (g_, h_, s_, t_)


def hensel_lift(p, l, f, g, h, s, t):
    # p: primo
    # l: potencia de p a la que vamos a elevar
    # f: polinomio con coeficientes en los enteros
    # g, h: polinomios con coeficientes en los enteros que verifican f = g * h mod p
    # s, t: polinomios con coeficientes en los enteros que verifican 1 = s*g + t*h mod p
    # Devuelve g_, h_, t_, s_ que verifican f_ = g_ * h_ mod p^l y 1 = s_*g_ + t_*h_ mod p^l
    m = 1
    for i in range(1, l):
        m = m * p
        (g, h, s, t) = hensel_step(p, f, g, h, s, t, m)
    return (g, h, s, t)


# # 9.1 Ejemplo en $\mathbb{Z}[x]$ con modularidad 625

# In[138]:


m = 5

K.<y> = PolynomialRing(GF(m))
R.<x> = PolynomialRing(ZZ)

f = x^4 - 1
f5 = K(f)
g5 = berlekamp(f5, m)
h5 = f5 // g5

(d,s,t) = tuple([R(k) for k in xgcd(g5,h5)])

print "m =",m
print "f =",f
print "g =",R(g5)
print "h =",R(h5)
print "s =",s
print "t =",t
print "(g',h',s',t') mod %d =" % m^4,hensel_lift(m, 4, f, R(g5), R(h5), s, t)


# # 10. Algoritmo de primalidad de *AKS*

# In[141]:


def ordr (r, n, m):
    # r: entero
    # n: elemento a verificar su primalidad
    # m: log_2(n)^2
    # Devuelve True si verifica que O_r(n) > log_2(n)^2. False en otro caso
    k = 1
    nextR = False
    while not nextR and k <= m:
        mod = power_mod(n, k, r)
        nextR = (mod == 1) or (mod == 0)
        k += 1
    return nextR

def AKS(n):
    # n: elemento a verificar su primalidad
    # Devuelve True si primo, False en caso contrario    
    
    # comprobamos que no sea potencia de la forma a^b
    for b in xrange(2, log(n, 2)):
        a = n ^ (1 / b)
        if floor(a) == a: return 'composite'

    # Obtenemos r tal que O_r(n) > log_2(n)^2
    r = 1
    nextR = True
    maxK = pari(log(n, 2) ^ 2).floor() 
    while nextR:
        r += 1
        nextR = False
        nextR = ordr(r, n, maxK)

    # si 1 < gcd(a,n) < n para a en (1,r] -> compuesto
    for a in range(2, r + 1):
        mcd = euclides(a,n, mod_int)
        if 1 < mcd  and mcd < n: return 'composite'

    # si r>=n -> primo
    if(r >= n): return 'prime'

    # para a en [1,N] si (x+a)^n == x^n+ a en (Z_n[x] / (x^r - 1)) -> comp
    N = pari(sqrt(euler_phi(r)) * log(n, 2)).floor()
    for a in xrange(1, N + 1):
        R.<x> = PolynomialRing(Integers(n))
        S = R.quotient((x ^ r) - 1)
        c = S((x ^ n + a))
        d = (x + a) ^ n

        if (c != d): return 'composite'
    return 'prime'


# ## 10.1 Ejemplos

# In[147]:


print(AKS(18))
print(AKS(149))
print(AKS(131))
print(AKS(163))

