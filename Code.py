# To find the length of the smallest substring with the maximum number of distinct characters.

#Import defaultdict
from collections import defaultdict

def SmallestSubStrLenght(Str):
  n = len(Str)
  DistinctCount = len(set(list(Str)))
  K = defaultdict(int)
  #Starting Index  
  Index = 0
  MinLen = 2**63 - 1
  DistinctNow = 0 
  for i in range(n):
    K[Str[i]] = K[Str[i]] + 1
    if K[Str[i]] == 1:
      DistinctNow = DistinctNow + 1
    
    if DistinctCount == DistinctNow:
      while K[Str[Index]] > 1:
        if K[Str[Index]] > 1:
          K[Str[Index]] = K[Str[Index]] - 1
        Index = Index + 1
      #Current Length
      Len = i - Index + 1
      MinLen = min(MinLen, Len)
  return MinLen

if __name__ == "__main__":    
    Str = input()
    result = SmallestSubStrLenght(Str)
    print (result)
