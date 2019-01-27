def  baby_giant(h,g,ordg):
    '''
    @param h result of logarithm, h \in <g>
    @param g the base of the logarithm
    @param orgg the order of `<g>` (finite)
    
    Compute `log_g(h)` with `<g>` of order ordg
    '''
    baby = [1]
    giant = [h]

    n = ceil(sqrt(ordg))
    gn = g^n
    inv_g = g^-1


    # compute baby = { g^(jn): 0 <= j < n }
    for i in  xrange(1,n): baby.append( baby[i-1]*gn )

    # compute giant = { h*g^(-i): 0 <= i < w }
    for j in  xrange(1,n): giant.append( giant[j-1]*inv_g )
     
    # We take elements from giant that are in baby
    # for each of those: x = j*n + i
    intersections = set(baby).intersection(set(giant))
    for  inters  in intersections:
        i = giant.index(inters)
        j = baby.index(inters)
        x = i+n*j

        print  'x = i + n*j = (%s) + (%d)*(%s) = (%s)' % (i,n,j,x,)
        # print '==> g^x = h <-> (%s)^(%s) = (%s)\n' % (g,x,h,)
        
    if len(intersections)==0: 
        print ("No discrete log of %s found to base " + \
        "%s using baby_giant") % (h,g,)






def baby_giant_test(a,b,ordb):
    sstr = "## log_({0})({1}) with <{0}> of order {2} ##".format(b,a,ordb)
    ostr = '#'*len(sstr)

    print ostr
    print sstr
    print ostr
    print

    baby_giant(a,b,ordb)
    print

    # for some reason, discrete_log uses 1 less than our baby_giant...
    try: dlog = discrete_log(a,b,ordb-1,operation='*')
    except ValueError: dlog= None

    print "using sage the result is", dlog
    print


# test using finite group of 3^6 elements
K.<b> = GF(3^6)
bb = K.gen()
a = bb^210

baby_giant_test(a, bb, K.order()-1)


# test using K[x]/f(x) whete K is the finite group of 3^6 elements
R.<x> = PolynomialRing(K)
f = b*x + 2*b # an element of K[x]
I = R.ideal([f]) # ideal generated from f
Q = R.quotient_ring(I) # K[x]/f(x)

A = Q(b*x^3 + x + b)
ordA = order_from_multiple(A,Q.order(),operation='*',check=False)
B = A^245
C = Q(x^2 + b)

baby_giant_test(B,A,ordA)
baby_giant_test(C,A,ordA)
