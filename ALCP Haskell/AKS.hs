module AKS where
#include "Header.hs"

import Numbers
import Quotient
import Polynomials

-- Tal y como se describe en "Primes in P"

aks::Integer->Bool --isPrime
aks n
  | ispow (fromInteger n)                               = False
  | any (inRange (2,n P.-1).gcd integer n)[2..r]        = False
  | n<=r                                                = True
  | any (condition.round)[1..sqrt(fromIntegral $ φ r)*l]= False
  | otherwise                                           = True
  where ispow n= 
          any (\b->let a=n**(1/b) in a==fromInteger(round a)) [2..l]
        r= toInteger $ fromJust $ L.find (\a->P.gcd n a==1 
             && fromInteger(order(integer `mod` a) n) > l^2) [2..]
        φ= product . map(\(p,n)->(p-1)*(p^(n-1))) . factor
        l= logBase 2 $ fromInteger n
        condition a=
          pow eucl (x+[a]) n /= (pow eucl x n + [a])
          where x=[1,0]
                zn=integer `mod` n
                eucl@(Field zero one (==)(+)(-)(*)(/))= pol zn`mod`m
                m=(.-) (pol zn) (pow (pol zn) x r) (_one (pol zn))
