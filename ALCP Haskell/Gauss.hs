module Gauss where
#include "Header.hs"

type Gauss=(Integer,Integer)

gaussOps::Dictionary Gauss
gaussOps=Euclid _zero _one (.==)(.+)(.-)(.*)(./) deg div where
  (==)=(P.==); (+)=(P.+); (-)=(P.-); (*)=(P.*)
  _one= (1,0); _zero=(0,0)
  z.==w        = z == w
  (a,b).+(c,d) = (a+c, b+d)
  (a,b).-(c,d) = (a-c, b-d)
  (a,b).*(c,d) = ((a*c)-(b*d), (b*c)+(a*d))
  z   ./ w = assert (deg w P.==1) z.*conj w
  deg w=fst $ w .* conj w
  div z w=
    let q=L.minimumBy (on compare (\u->norm (z.-(w.*u)))) options
        options=[(floor α,floor β).+(i,j)|i<-[0,1],j<-[0,1]]
        (α,β)=(fromInteger(fst$ z.*conj w) P./ fromInteger(norm w),
          fromInteger(snd$ z.*conj w) P./ fromInteger(norm w))
    in (q,z.-(q.*w))
   
norm (u,v) = (u P.* u) P.+ (v P.* v)
conj (u,v) = (u,0 P.-v)
