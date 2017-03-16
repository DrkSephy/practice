# Write a function fib() that a takes an integer n 
# and returns the nnth fibonacci ↴ number.

# We could use a dictionary, where the keys represent 
# capacities and the values represent the max possible monetary 
# values at those capacities. Or we could use a list, where the 
# indices represent capacities and the values represent max monetary 
# values. Dictionaries are built on arrays, so we can save some 
# overhead by just using a list.

# This is a classic computer science puzzle called "the unbounded knapsack problem."

# We use a bottom-up ↴ approach to find the max value at our duffel bag's weight_capacity 
# by finding the max value at every capacity from 0 to weight_capacity.

def max_duffel_bag_value(cake_tuples, weight_capacity):

  # list to hold the maximum possible value at every
  # integer capacity from 0 to weight_capacity
  # starting each index with value 0
  max_values_at_capacities = [0] * (weight_capacity + 1)

  for current_capacity in xrange(weight_capacity + 1):
    # write a loop through all the cakes (ignoring cakes that are too heavy to fit):
    for cake_weight, cake_value in cake_tuples:
      # if the cake weights as much or less than the current capacity
      # see what our max value could if we took it
      if cake_weight <= current_capacity
        # find max_value_using_cake

        # should we use the cake or not?
        # if we use the cake, the most kilograms we can include in addition to the cake
        # we're adding is the current capacity minus the cake's weight. we find the max
        # value at that integer capacity in our list max_values_at_capacities
        max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]

        # now we see if it's worth taking the cake. how does the
        # value with the cake compare to the current_max_value?
        current_max_value = max(max_value_using_cake, current_max_value)

    # add each capacity's max value to our list so we can use them
    # when calculating all the remaining capacities
    max_values_at_capacities[current_capacity] = current_max_value
 return max_values_at_capacities[weight_capacity]

# O(n*k) time, and O(k) space, where n is number of types of cake and 
# k is the capacity of the duffel bag. We loop through each cake (n cakes) 
# for every capacity (k capacities), so our runtime is O(n * k) O(n * k), 
# and maintaining the list of k + 1 capacities gives us the O(k) O(k) space.
