module Euclides where
import Prelude hiding(gcd,mod,(+),(-),(*),(/),div)
import qualified Prelude   as P
import qualified Data.List as L
import Data.Maybe
import Definitions

euclidesExtendido :: TiposAlgebraicos t -> t->t->(t,t,t)
euclidesExtendido euclideo a b 
  | b==zero   = (a, one, zero)
  | otherwise = let (q,r)  = div a b
                    (d,s,t)= euclidesExtendido euclideo b r
                in  (d,t,s-(q*t))
  where DEuclideo zero one (==)(+)(-)(*)(/) deg div=euclideo

mcd :: TiposAlgebraicos t -> t -> t -> t
mcd euclideo a uno = a where uno = _uno euclideo
mcd euclideo a b = mcd euclideo b (resto euclideo a b)

mcm euclid a b = fst$ _div euclid ((.*) euclid a b) (mcd euclid a b)

resto euclideo a b = r where (_, r) = _div euclideo a b