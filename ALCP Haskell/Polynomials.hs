module Polynomials where
#include "Header.hs"

pol::Dictionary d->Dictionary [d]
pol (Euclid zero one(==)(+)(-)(*)(/)deg div)=
  pol (Field zero one(==)(+)(-)(*)(/))

pol field = Euclid _zero _one (.==)(.+)(.-)(.*)(./) _deg _div where
  Field zero one (==) (+) (-) (*) (/) = field 

  _one=[one]; _zero=[]
  p.==q  = let l=length p P.- length q
           in  and $ zipWith (==) (pad(0 P.-l)++p) (pad l++q)
  p.+q   = let l=length p P.- length q 
           in reduction$zipWith (+) (pad(0 P.-l)++p) (pad l++q)
  p.-q   = p .+ map (zero-) q
  p.*q   = if q.==_zero then [] else reduction$
              (map (*head q) p++pad (length q P.-1)) .+ (p.*tail q)
  p./q   = assert (r.==_zero) c
           where (c,r)=_div p q

  _deg p = length(reduction p)
  _div p q
    |q.==_zero = error "división por cero"
    |otherwise=(reduction (c.*[one/head q']),reduction r)
    where q'=reduction q
          (c,r)=divmonic p (q'.*[one/head q'])
  
  reduction = dropWhile (==zero)
  pad a=replicate a zero
  divmonic p q
    |q.==_zero     = error "division por cero" 
    |_deg p<_deg q = (_zero,p)
    |otherwise     = (c.+(head p:pad),r) 
    where (c,r)    = divmonic (p.-(map (*head p) q++pad)) q 
          pad      = replicate (_deg p P.- _deg q) zero

monic field p = map (/head p) $ dropWhile (==zero) p
                where Field zero one (==)(+)(-)(*)(/)= field

derivate::Dictionary d->[d]->[d]
derivate ring p= reduce[mul ring (p!!i) (l-i-1) |i<-[0,1..l-2] ]
                 where l     = length p
                       reduce= dropWhile ((.==) ring (_zero ring))
