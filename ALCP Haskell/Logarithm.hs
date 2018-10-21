module Logarithm  where
#include "Header.hs"
import Quotient
import Polynomials
import Numbers
import FiniteField

logarithm::Show d=>Dictionary d->d->d->(Integer,Integer)
logarithm field α β=
  chineseInteger$ [0..12] >>= (\u->logarithmEq field u α β)

logarithmEq::Show d=>Dictionary d->Integer->d->d->[(Integer,Integer)]
logarithmEq field seed α β=
  end $ loop $ zip (iterate f (one,0,0)) (iterate (f.f) (one,0,0)) 
   
  where Field zero one (==)(+)(-)(*)(/)=field
        n= order field α

        f (x,a,b)| opt P.==0 = (α*x, 1 P.+a,       b)
                 | opt P.==1 = (x*x, 2 P.*a, 2 P.* b) 
                 | opt P.==2 = (β*x,      a, 1 P.+ b)
                 where opt= hash seed x `P.mod` 3

        loop= fromJust. L.find (\((x,_,_),(y,_,_))-> x==y).tail
          
        end ((_,a,b),(_,a',b'))= 
          [((./) (integer`mod`n') a'' b'' ,n')| b'' /=zero]
          where n' = n     /g
                a''= (a'-a)/g
                b''= (b-b')/g
                g=gcd integer (a'-a) $ gcd integer (b-b') n
                Euclid zero one (==)(+)(-)(*)(/) deg div=integer

hash seed x= pow (integer`mod`541) (seed+1) (tonum$show x) 
             where tonum= foldr (\u v->v*256+toInteger(ord u)) 0 
