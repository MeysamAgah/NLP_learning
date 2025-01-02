def Damerau_Levenshtein_distance(a,b):
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
