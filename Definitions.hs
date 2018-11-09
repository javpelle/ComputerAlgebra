module Definitions where
import Prelude hiding(gcd,mod,(+),(-),(*),(/),div)
import qualified Prelude   as P
import qualified Data.List as L
import Data.Maybe

data TiposAlgebraicos t=
  Cuerpo {_cero::t, _uno::t, (.==)::t->t->Bool, (.+)::t->t->t,
         (.-) ::t->t->t   , (.*) ::t->t->t   , (./)::t->t->t  }|

  DEuclideo {_cero::t, _uno::t, (.==)::t->t->Bool, (.+)::t->t->t,
         (.-) ::t->t->t,    (.*) ::t->t->t   , (./)::t->t->t,
         _grado ::t->Integer, _div::t->t->(t,t)                 }|

  DFU {_cero::t, _uno::t, (.==)::t->t->Bool, (.+)::t->t->t,
         (.-) ::t->t->t,    (.*) ::t->t->t,
         _factor::t->(t,[(t,Integer)])                        }



-- pow :: Dictionary d->d->Integer->d
-- pow ring a b=
--  if b==0 then one  else α*α*(if b`P.mod`2 == 1 then a else one )
--  where (*)=(.*) ring; one=_one ring
--        α=pow ring a (b`P.div`2)

-- mul :: Dictionary d->d->Integer->d
-- mul ring a b=
--  if b==0 then zero else α+α+(if b`P.mod`2 == 1 then a else zero)
--  where (+)=(.+) ring; zero=_zero ring
--        α=mul ring a (b`P.div`2)

-- order :: Dictionary  t->t->Integer
-- order ring elem=1 P.+(toInteger $ fromJust $ L.findIndex(==one) 
--    $ take 100000 $iterate(*elem)elem)
--  where (*)=(.*)ring; one=_one ring; (==)=(.==)ring
