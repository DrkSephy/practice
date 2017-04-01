# Word frequencies: Design a method to find the frequency of occurrences of any given word in a book.
# What if we were running this algorithm multiple times?

# Store words that were queried in a hash table for O(1) lookups in the future
frequencies = {}

def save(word, frequency):
  if word not in frequencies:
    frequencies[word] = frequency
  return

def count(word, book):
  words = book.split(' ')
  occurrences = 0
  for text in words:
    if text == word:
      occurrences += 1
  save(word, occurrences)
  return occurrences

count('hello', 'hello world meow hello testing')
