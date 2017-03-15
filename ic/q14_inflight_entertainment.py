# Write a function that takes an integer flight_length (in minutes) and a 
# list of integers movie_lengths (in minutes) and returns a boolean indicating 
# whether there are two numbers in movie_lengths whose sum equals flight_length.

# When building your function:

# Assume your users will watch exactly two movies
# Don't make your users watch the same movie twice
# Optimize for runtime over memory.

# flight_length: integer (in minutes)
# movie_lengths: list of integers 

# Complexity: O(n) time, O(n) space
def find_movies(flight_length, movie_lengths):
  # Build a hash table of the compliment for each movie length seen
  second_movie = set()

  for movie in movie_lengths:
    remaining_time = flight_length - movie
    # If the remaining time exists in our hash set, then two movies
    # exist that we can watch on our trip. Return true
    if remaining_time in second_movie:
      return True
    # else, we store the compliment (remaining time) inside our hashset
    second_movie.add(movie)
  return False



print find_movies(100, [10, 20, 30, 40, 50, 60, 70])