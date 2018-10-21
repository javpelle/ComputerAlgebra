module Experiment where

--Vestigio de una era pasada, en la que quería hacerlo todo bien.
--Hace falta ser un Haskeller lvl 35 para esto

import Prelude hiding (+) (-) (*) (/) (deg) (div)
import qualified Prelude as P

data Dictionary d=Ring{_zero::d, (.+)::d->d->d}|Group{_one::d, (.*)::d->d->d}

class Structurable d where
  (+)::d->d->Structure d->d
  (*)::d->d->Structure d->d
  zero::Structure d->d
  one::Structure d->d
  literal::Structure d->d->d
  literal=const

data Structure d=ℤ| (Structure d):/d

getOps::Structure d->Dictionary d
  getOps ℤ=

instance Structurable Integer where
  (a+b) ℤ = ((.+) (getOps ℤ)) (a ℤ) (b ℤ)
  (a+b) (s :/ p) = 

{-
class Arrobable e t | e->t where
  (^-^)::Dictionary t->e->t

instance Arrobable a a where
  dict^-^exp=exp
instance Arrobable (Dictionary d->d) d  where 
  dict^-^exp=exp dict

zero::Dictionary d-> d                                          ; zero=_zero
one::Dictionary d-> d                                           ; one=_one
(+)::Arrobable e d=>e->e->Dictionary d->d      ; (a+b) dic=(.+) dic (dic^-^a) (dic^-^b)
(-)::(Dictionary d->d)->(Dictionary d->d)->Dictionary d->d      ; (a-b) des=(.-) des (a des) (b des)
(*)::(Dictionary d->d)->(Dictionary d->d)->Dictionary d->d      ; (a*b) des=(.*) des (a des) (b des)
(/)::(Dictionary d->d)->(Dictionary d->d)->Dictionary d->d      ; (a/b) des=(./) des (a des) (b des)
deg::(Dictionary d->d)->Dictionary d->Integer                   ; deg a des=_deg des (a des)
div::(Dictionary d->d)->(Dictionary d->d)->Dictionary d->(d,d)  ; div a b des=_division des(a des)(b des)
fact::(Dictionary d->d)->Dictionary d-> (d,[(d,Integer)])       ; fact a des=_factor des (a des)
literal::d->Dictionary d->d                                     ; literal a des=a
-}

{- De Polynomials. 
cyclotomic::Dictionary d->[d]
cyclotomic field =
  [foldr (\a b->fst $ _division (pol field) b a) (start n) (dividers n)| n<-[1..]]
  where Field one zero (==) (+) (-) (*) (/)= field
        start n=[one]++replicate (n P.- 1) zero++[zero-one]
        dividers n=[cyclotomic field!!k|k<-[1..n-1], k `P.mod` n P.==0]
 -}    
