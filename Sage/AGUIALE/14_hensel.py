def hensel_step(m,f,g,h,s,t,base=None):
    '''
    m \in R (anillo conmutatico)
    f,g,h,s,t \in R[x]

        f congruente gh mod m --> condicion de hensel
        sg + th congruente 1 mod m --> factorización de xgcd
        lc(f) no divisor de cero mod m
        h monico
        def f = n = deg g + deg h
        deg s < deg h
        deg t < deg g
    '''

    base = base or m # en el paso esto es m^(l-1)
    m_l = base*m # la nueva elevación: m^l

    ## Resolvemos las ecuaciones modulo la base m_l

    e = (f- g*h) % m_l
    
    (q,r) = (s*e).quo_rem(h)
    (q,r) = tuple([k % m_l for k in (q,r)])

    g_ = (g + t*e + q*g) % m_l
    h_ = (h + r)% m_l


    b = (s*g_ + t*h_ - 1) % m_l

    (c,d) = (s*b).quo_rem(h_) # calculamos c,d
    (c,d) = tuple([k % m_l for k in (c,d)]) # les hacemos el módulo

    s_ = (s - d) % m_l
    t_ = (t - t*b - c*g_) % m_l

    return (g_,h_,s_,t_)


def hensel_lift(p,l,f,g,h,s,t):
    m = 1
    for i in range(1,l):
        m = m*p
        (g,h,s,t) = hensel_step(p,f,g,h,s,t,base=m)
    return (g,h,s,t)

m = 5

K.<y> = PolynomialRing(FiniteField(5))
R.<x> = PolynomialRing(ZZ)

f= x^4 -1
g = x^3 + 2*x^2 - x - 2
h = x - 2
(d,s,t) = tuple([R(k) for k in xgcd(K(g),K(h))])

print "EXAMPLE 15.8 (continued); page 447 Modern Computer Algebra"
print "m =",m
print "f =",f
print "g =",g
print "h =",h
print "s =",s
print "t =",t
print "(g',h',s',t') mod %d =" % m^4,hensel_lift(m,4,f,g,h,s,t)
