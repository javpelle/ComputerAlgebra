module Euclides where
import Prelude hiding(gcd,mod,(+),(-),(*),(/),div)
import qualified Prelude   as P
import qualified Data.List as L
import Data.Maybe

euclidesExtendido :: TiposAlgebraicos t -> t->t->(t,t,t)
euclidesExtendido euclideo a b 
  | b==zero   = (a, one, zero)
  | otherwise = let (q,r)  = div a b
                    (d,s,t)= eea euclid b r
                in  (d,t,s-(q*t))
  where DEuclideo zero one (==)(+)(-)(*)(/) deg div=euclideo

mcd euclideo a b = d where (d,_,_)=euclidesExtendido euclideo a b
mcm euclid a b = fst$ _div euclid ((.*) euclid a b) (gcd euclid a b)