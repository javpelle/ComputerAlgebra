module Matrices where

import Definitions
import Data.List
import Prelude hiding ((+),(-),(*),(/),div,mod)
import qualified Prelude as P

mat::Dictionary d->Integer->Dictionary [[d]]
mat field n=Field{
  _zero=[[zero|i<-[1..n]]|j<-[1..n]],
  _one = [[if i P.==j then one else zero|i<-[1..n]]|j<-[1..n]],
  (.==) = \a b-> and $ zipWith (\c d->and $ zipWith (==) c d) a b,
  (.+)   = zipWith $ zipWith (+),
  (.-)  = zipWith $ zipWith (-),
  (.*) = \a b->[[foldr1 (+) [(a!!i!!k)*(b!!k!!j)|k<-[0..n' P.-1]] 
                | i<-[0..n' P.-1]]  | j<-[0..n' P.-1]
  (./)  = \a b->error "not a real field"
  ]
  } where Field zero one (==) (+) (-) (*) (/)=field
          n'=fromInteger n
  

