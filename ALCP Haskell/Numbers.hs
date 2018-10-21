module Numbers where

#include "Header.hs"

integer=Euclid {
 _zero=0::Integer,
 _one =1::Integer,
 (.==)=(==),
 (.+)=(+),
 (.-)=(-),
 (.*)=(*),
 (./)= \n m->let (c,r)=_div integer n m
             in assert (r==0) c,
 _deg= P.id,
 _div= \a b->(P.div a b, P.mod a b)
}
