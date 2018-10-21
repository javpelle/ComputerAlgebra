module FiniteField where
#include "Header.hs"
import Quotient
import Polynomials
import Numbers

finite p n=assert (LO.member p primes) $
            pol zp `mod`(head$filter(irred p) $enumPol p n)
           where zp= integer`mod`p

enumList p 1=[[c]|c<-[0..p P.-1]]
enumList p n=[c:q|c<-[0..p P.-1],q<-enumList p (n P.-1)]

enumPol::Integer->Integer->[[Integer]]
enumPol p n=[1:q|q<-enumList p n]

--Test de irreducibilidad en Zq, p primo
irred::Integer->[Integer]->Bool
irred p f=
  zero == h n && 
   all (isUnit (pol field).gcd (pol field) f.h )primedivs 
  where 
    n=_deg (pol field) f P.- 1 
    field@(Field _zero _one (.==)(.+)(.-)(.*)(./))=integer `mod` p
    Field zero one (==)(+)(-)(*)(/) =pol field`mod`f
    h n_i=pow (pol field`mod`f) x (pow integer p n_i) - x
    x=[_one,_zero] --polinomio x
    primedivs=[n `P.div` p_i| p_i<-(fst.unzip.factor) n]

--TODO pretty-print de la tabla de multiplicar
printtable p n=
  let Field zero one (==)(+)(-)(*)(/)=finite p n
      trad a=if null a then 0
                       else (p P.* (trad$tail a)) P.+ head a 
  in [map (trad.reverse)
       [(a*b)/b|a<-tail$enumList p n]|b<-tail$enumList p n]
