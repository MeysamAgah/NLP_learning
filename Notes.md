## 2. Damerau–Levenshtein distance
The Damerau–Levenshtein distance is a measure of the similarity between two strings, which takes into account the number of insertion, deletion, substitution, and transposition operations needed to transform one string into the other.
<br><br>
Algorithm: The following procedure outlines the steps to calculate the Damerau–Levenshtein distance between two strings:
<br><br>
Inputs: a(string1) and b(string2)
<br><br>
m = number of characters of a
<br><br>
n = number of characters of b
<br><br>
d = distance_matrix (m+1) x (n+1)
<br><br>
i = number between 0 and m
<br><br>
j = number between 0 and n
<br><br>
![](https://raw.githubusercontent.com/MeysamAgah/NLP_learning/refs/heads/main/pics/2.1.jpg)
<br><br>
Here's an example of how algorithm works:<br><br>
Consider our goal is calculate distance between words kitten and sitting.<br>
Step 1: we initialize matrix and fill values with 0<br>

$$\begin{bmatrix}
 & "" & k & i & t & t & e & n \\
"" & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
s & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
i & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 
t & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
t & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
i & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
n & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
g & 0 & 0 & 0 & 0 & 0 & 0 & 0 
\end{bmatrix}$$

<br>
Step 2: we update matrix according to this equation:<br>
IF MIN (i, j) = 0 THEN d<sub>a, b</sub>(i, j)= MAX(i, j)
<br><br>

$$\begin{bmatrix}
 & "" & k & i & t & t & e & n \\
"" & 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
s & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
i & 2 & 0 & 0 & 0 & 0 & 0 & 0 \\ 
t & 3 & 0 & 0 & 0 & 0 & 0 & 0 \\
t & 4 & 0 & 0 & 0 & 0 & 0 & 0 \\
i & 5 & 0 & 0 & 0 & 0 & 0 & 0 \\
n & 6 & 0 & 0 & 0 & 0 & 0 & 0 \\
g & 7 & 0 & 0 & 0 & 0 & 0 & 0 
\end{bmatrix}$$

<br><br>

Step 3: in this step we calculate one of matrix elements (i=1, j=1):<br>
a<sub>i</sub> = s <br>
b<sub>j</sub> = k <br>
a<sub>i</sub> ≠ b<sub>j</sub> <br>
d<sub>(i-1, j-1)</sub> + 1 = 1 <br>
d<sub>(i, j-1)</sub> + 1 = 2 <br>
d<sub>(i-1, j)</sub> + 1 = 2 <br>
MIN { d<sub>(i-1, j-1)</sub> + 1, d<sub>(i, j-1)</sub> + 1, d<sub>(i-1, j)</sub> + 1} = 1 <br>
THEN d<sub>(i, j) = 1<br>

$$\begin{bmatrix}
 & "" & k & i & t & t & e & n \\
"" & 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
s & 1 & 1 & 0 & 0 & 0 & 0 & 0 \\
i & 2 & 0 & 0 & 0 & 0 & 0 & 0 \\ 
t & 3 & 0 & 0 & 0 & 0 & 0 & 0 \\
t & 4 & 0 & 0 & 0 & 0 & 0 & 0 \\
i & 5 & 0 & 0 & 0 & 0 & 0 & 0 \\
n & 6 & 0 & 0 & 0 & 0 & 0 & 0 \\
g & 7 & 0 & 0 & 0 & 0 & 0 & 0 
\end{bmatrix}$$

<br><br>
Step 4: we fill rest of values according to algorithm. resulted matrix is:<br><br>

$$\begin{bmatrix}
 & "" & k & i & t & t & e & n \\
"" & 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
s & 1 & 1 & 2 & 3 & 4 & 5 & 6 \\
i & 2 & 2 & 1 & 2 & 3 & 4 & 5 \\ 
t & 3 & 3 & 2 & 1 & 2 & 3 & 4 \\
t & 4 & 4 & 3 & 2 & 1 & 2 & 3 \\
i & 5 & 5 & 4 & 3 & 2 & 2 & 3 \\
n & 6 & 6 & 5 & 4 & 3 & 3 & 2 \\
g & 7 & 7 & 6 & 5 & 4 & 4 & 3 
\end{bmatrix}$$

<br><br>

Python code to calculate Damerau–Levenshtein distance of two strings
```python
def d_l_distance(a,b):
  """
  This function computes the Damerau-Levenshtein distance between two strings.
  a: string1
  b: string2
  Output: A matrix representing the distances and the final computed distance value.
  """
  m = len(a) #length of first string
  n = len(b) #length of second string
  distance_matrix = [[0 for j in range(n+1)] for i in range(m+1)] #initializing matrix
  for i in range(m+1):
    for j in range(n+1):
      if min(i,j)==0:
        distance_matrix[i][j] = max(i,j) 
      else:
        if a[i-1]==b[j-1]:
          #no action needed
          distance_matrix[i][j] = distance_matrix[i-1][j-1]
        else:
          #DELETE, INSERT, REPLACE
          distance_matrix[i][j] = min(distance_matrix[i-1][j],distance_matrix[i][j-1],distance_matrix[i-1][j-1])+1

  print(f"distance matrix between {a} and {b} is:")
  for k in distance_matrix: #to visualize resulted distance matrix like a matrix
    print(k)
  print(f"distance between {a} and {b} is: {distance_matrix[m][n]}")
```
<br><br>

**References:**
<br>
https://www.geeksforgeeks.org/damerau-levenshtein-distance
<br>
https://ryanong.co.uk/2020/01/02/day-2-damerau-levenshtein-distance
<br>
https://medium.com/@ethannam/understanding-the-levenshtein-distance-equation-for-beginners-c4285a5604f0
<br>
https://www.youtube.com/watch?v=MiqoA-yF-0M&list=WL&index=2&t=485s
