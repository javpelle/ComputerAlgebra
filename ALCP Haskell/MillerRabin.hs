module MillerRabin where
#include "Header.hs"

import Utilities

-- (n-1)=s*2\^r
-- Si a\^s /= 1 mod n
-- y a\^(s*2\^t) /= -1 mod n (para cualquier 0<=t<=r-1)
-- entonces n es compuesto. A a se le llama testigo

millerRabin::Integer->Integer->Bool
millerRabin k n=
  all test $ take k $ map (getRandom n) [1..]
  where (s,r)=div2 (n-1)
        test t| t_s==1   = True
              | otherwise= elem (n-1) $ take r $
                            iterate (\a->(a*a)`P.mod`n) t_s
              where t_s  = (t^s) `P.mod` n

        div2 n| n`P.mod`2==0 = (n',s'+1) 
              | otherwise= (n,0)
              where (n',s')=div2 (n`div`2)
        getRandom n i =unsafePerformIO $ do
          g<-getStdGen; return $ randomRs (1,n-1) g !!i

-- (take 30 ( filter (millerRabin 30) [2..]))
