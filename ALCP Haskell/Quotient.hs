module Quotient where

#include "Header.hs"
import Numbers

mod::Dictionary d->d->Dictionary d
mod euclid m=Field{ 
    _zero= zero, _one=one,
    (.==)= \a b-> snd (div (a-b) m)==zero,
    (.+) = \a b-> snd $ div (a+b) m,
    (.-) = \a b-> snd $ div (a-b) m,
    (.*) = \a b-> snd $ div (a*b) m,
    (./) = \a b-> let g=gcd euclid a $ gcd euclid b m
                      a'=fst $ div a g
                      b'=fst $ div b g
                      m'=fst $ div m g
                      (d',s',t')=eea euclid b' m'  
                  in reduce $ assert (deg d' P.== 1) (a'*s'/d')
  } where Euclid zero one (==)(+)(-)(*)(/) deg div=euclid
          reduce a=snd$div a m

isUnit euclid m=_deg euclid m ==1

chinese :: Dictionary d-> [(d,d)]->(d,d)
chinese euclid= foldr1 chinese2
  where chinese2 (x1,y1) (x2,y2)= reduce
          ((x1*y2*(./) (euclid`mod`y1) one y2)+
           (x2*y1*(./) (euclid`mod`y2) one y1), y1*y2)
        Euclid zero one (==)(+)(-)(*)(/) deg div=euclid
        reduce (a,b)=(snd$ a `div`b,b)

-- para euclid=integer, tengo uno a prueba de no-primos.
chineseInteger=chinese integer.chineseFilter.chineseSplit where 

  chineseSplit::[(Integer,Integer)]->[[(Integer,Integer)]]
  chineseSplit l= Ext.groupWith (fst.head.factor.snd)$ L.sort $ l>>=
    (\(x,y)->[(snd$_div integer x $ pow integer b e,pow integer b e)
              |(b,e)<-factor y]) 

  chineseFilter::[[(Integer,Integer)]]->[(Integer,Integer)]
  chineseFilter l= map filterPrime l where
    filterPrime l=
      assert(all (\(x',y')->snd(_div integer x y')==x') l) (x,y)
      where (x,y)=last l
