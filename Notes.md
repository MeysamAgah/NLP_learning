## Damerau–Levenshtein distance
The Damerau–Levenshtein distance is a measure of the similarity between two strings, which takes into account the number of insertion, deletion, substitution, and transposition operations needed to transform one string into the other.
<br>
Algorithm: The formula to calculate each element of distance matrix according to Damerau–Levenshtein distance is:
<br>
Inputs: string1 and string2
<br>
m = number of characters of string1
<br>
n = number of characters of string2
<br>
d = distance_matrix (m+1) x (n+1)
<br>
i = a number between 0 and m
<br>
j = a number between 0 and n
<br>
IF MIN (i, j) = 0 THEN d<sub>(i, j)</sub> = MAX (i, j)
<br>
ELSE THEN
<br>
  IF a<sub>(i)</sub> = b<sub>(j)</sub> THEN d<sub>(i, j)</sub> = d<sub>(i-1, j-1)</sub>
  <br>
  ELSE THEN
  <br>
    d<sub>(i, j)</sub> = MIN{
                            d<sub>(i-1, j-1)</sub> + 1,
                            d<sub>(i, j-1)</sub> + 1,
                            d<sub>(i-1, j)</sub> + 1
                            }
