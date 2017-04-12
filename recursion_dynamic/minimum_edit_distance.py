# Given two strings, determine the minimum edit distance
# (The number of edits needed to transform string one into
# string two.) Use dyanmic programming.

# ex: String 2: a b c d e f , String 1: a z c e d -> 3 edits

def minimum_edit_distance(str1, str2):
  # Initialize Matrix
  matrix = [[0] * (len(str1) + 1) for i in range(len(str2) + 1)]

  # Initialize first col to 0, 1, 2, 3, 4, 5
  for i in range(0, len(str1) + 1):
    matrix[0][i] = i

  # Initialize first row to 0, 1, 2, 3, 4, 5, 6
  for j in range(0, len(str1)):
    matrix[j][0] = j

  # Iterate over matrix, filling in values
  # print len(str1)
  # for i in range(1, len(str1)):
  #   print i

  for i in xrange(1, len(str2) + 1):
    for j in xrange(1, len(str1) + 1):
      # Are the string characters at these positions equal?
      if str1[j-1] == str2[i-1]:
        # If so, get the diagonal to the left
        matrix[i][j] = matrix[i-1][j-1]
      else:
        # Find minimum from left, top, left-diagonal and add 1
        value = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
        matrix[i][j] = value
  return matrix[len(str2)][len(str1)]


print minimum_edit_distance('abcdef', 'azced')