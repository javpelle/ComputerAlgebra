def AKS(n):
    # comprobamos que no sea potencia de la forma a^b
    for b in xrange(2,log(n,2)):
        a = n^(1/b)
        if floor(a)==a: return 'composite'

    # Obtenemos r tal que O_r(n) > log_2(n)^2
    r=2; nextR=True
    m=pari(log(n,2)^2).floor() 
    M=max(3, pari(log(n,2)^5).ceil())
    while nextR and r<M:
        nextR=False
        k=1
        while not nextR and k<= m:
            mod = power_mod(n,k,r)
            nextR = (mod==1) or (mod==0)
            k+=1
        r+=1
    r-=1

    # si 1 < gcd(a,n) < n para a en (1,r] -> compuesto
    for a in xrange(r,1,-1):
        mcd = gcd(a,n)
        if 1 < mcd  and mcd < n: return 'composite'

    # si r>=n -> primo
    if(r>=n): return 'prime'

    # para a en [1,N] si (x+a)^n == x^n+ a en (Z_n[x] / (x^r - 1)) -> comp
    N=pari(sqrt(euler_phi(r))*log(n,2)).floor()
    for a in xrange(1,N+1):
        R.<x>=PolynomialRing(Integers(n))
        S=R.quotient((x^r)-1)
        c=S((x^n + a))
        d=(x+a)^n

        if (c!=d): return 'composite'
    return 'prime'

def printaks(i):
    print "%d is %s" % (i,AKS(i))

for i in range(2,20):
    printaks(i)

printaks(561)
printaks(1105)
