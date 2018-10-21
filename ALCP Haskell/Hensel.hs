module Hensel  where
#include "Header.hs"

import Quotient
import Polynomials
import Numbers
import FiniteField
import Factorization
import Utilities

--Paso 1
primeMod::[Integer]->Integer
primeMod f= 
  fromJust$ L.find (test f) primes
  where test f p=
          (head f`P.mod`p P./=0) && (f'/=[]) && (m==[1])
          where f'=derivate (integer`mod`p) f
                m=monic (integer`mod`p)$
                    gcd (pol(integer`mod`p)) f f'
                (==)=(.==) (pol(integer`mod`p))

--Paso 3: devuelve el N que debe sobrepasar Hensel
mignotteBound::Integer->[Integer]->Integer
mignotteBound p f=
  ceiling $ logBase (fromInteger p)  bound
  where norm= sqrt$ sum$ map(\a->fromInteger (a*a)) f
        bound= 2.0^length f*norm

--Paso 4: devuelve, en el mismo formato, el hensel Lift, de n a n\^2
henselLift n (f,g,h,s,t)=
  assert ((.==) (pol(integer`mod`n)) f (g'*h')) $ 
  assert ((.==) (pol(integer`mod`n)) one ((s'*g')+(t'*h'))) $
  assert (f==(g'*h')) $ 
  assert (one==((s'*g')+(t'*h'))) $
  (f,g',h',s',t')
  where (g',h')= ((g*(one+q))+(t*δ), h+r)  
                 where δ=f-(g*h)
                       (q,r)=(s*δ) `div` h
        (s',t')= (s-r, ((one-ε)*t)-(g'*q))
                 where ε=(s*g')+(t*h')-one
                       (q,r)=(s*ε) `div` h'

        Euclid zero one(==)(+)(-)(*)(/) deg div=pol (integer`mod`(n P.*n))

liftTo p pN (f,g,h,s,t)
  | p>=pN  = (f,g,h,s,t)
  | otherwise = liftTo (p*p) pN $ henselLift p (f,g,h,s,t)

products m []=[([1],[1])]
products m (x:xs)=
  [(trueRepr m $a*c, trueRepr m $ b*d)
   |(a,b)<-[(one,x),(x,one)],(c,d)<-products m xs]
  where Euclid zero one(==)(+)(-)(*)(/)deg div=pol$(integer`mod`m)

--Paso 5: recombina los factores como buenamente puede
recombine::[Integer]->Integer->[[Integer]]->[[Integer]]
recombine f m factors=
  [real_divs!!(2^i) 
   |i<-[0.. ceiling(logBase 2 $ fromInteger$ length real_divs)P.-1]]
  where real_divs=concatMap (\(a,b)->[a|(a*b)==f]) divs
        divs=products m factors
        Euclid zero one(==)(+)(-)(*)(/)deg div=pol$integer
  
--Devuelve los coeficientes al representante mas cercano a 0
trueRepr n= map (\a-> if a<=(n`div`2) then a else a-n)

factorPolInt::[Integer]->[[Integer]]
factorPolInt f=
  recombine f pN lifted
  where p=primeMod f
        n=mignotteBound p f
        pN=p^n
        
        factors=map(map to_zp) $factorPol p 1(monic fp (map (:[]) f))
                where to_zp []= 0; to_zp [a]=a
                      fp=finite p 1
      
        lifted::[[Integer]]
        lifted=map (trueRepr pN) $ liftTo p pN f factors

        liftTo m pN f factors
          | m>=pN = factors
          | otherwise = liftTo (m*m) pN f $ liftallStep m f factors
        
        liftallStep::Integer->[Integer]->[[Integer]]->[[Integer]]
        liftallStep m f [] = []
        liftallStep m f (g:gs)=
          g':liftallStep m h' gs
          where (d,s,t)= eea(pol$ integer`mod`m) g h
                (_,g',h',_,_)=henselLift m (f,g,h,s/d,t/d)
                (/)=(./) (pol$ integer`mod`m)
                h=foldr ((.*) (pol$ integer`mod`m)) 
                   (_one (pol$ integer`mod`m)) gs
