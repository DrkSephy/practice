# Problem: Implement fizzbuzz.
# Return the string representation of numbers from 1 to n.
# Multiples of 3 --> 'Fizz'
# Multiples of 5 --> 'Buzz'
# Multiples of 3 and 5 --> 'FizzBuzz'

def fizzbuzz(num):
  results = []
  if num is None:
    raise TypeError('num cannot be None')
  if num < 1:
    raise ValueError('num cannot be less than 1')
  for i in range(1, num + 1):
    if i % 3 == 0 and i % 5 == 0:
      results.append('FizzBuzz')
    elif i % 3 == 0:
      results.append('Fizz')
    elif i % 5 == 0:
      results.append('Buzz')
    else:
      results.append(str(i))

  return results

print fizzbuzz(100)