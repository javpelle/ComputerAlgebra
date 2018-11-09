module Numbers where

import Definitions
import Control.Exception

integer=DEuclideo {
 _cero=0::Integer,
 _uno =1::Integer,
 (.==)=(==),
 (.+)=(+),
 (.-)=(-),
 (.*)=(*),
 (./)= \n m->let (c,r)=_div integer n m
             in assert (r==0) c,
 _grado= id,
 _div= \a b->(div a b, mod a b)
}
