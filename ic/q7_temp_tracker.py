# We use an ahead-of-time approach, computing values as we go
# inside of our insert

# Complexity: O(1) for space and runtime

class TempTracker(self):
  # Init min and max temperature
  def __init__(self):
    self.min_temp = None
    self.max_temp = None
    # Mean stuff
    self.total_temps = 0
    self.sum = 0.0
    self.mean = None
    # Mode Stuff
    self.occurrences = [0] * (111)
    self.max_occurrences = 0

  # Insert temperatures, keeping track of highest / lowest
  # O(1) time for insert
  def insert(self, temperature):
    # For computing Mean
    self.total_temps += 1
    self.sum += temperature
    self.mean = self.sum / self.total_temps

    # For mode
    self.occurrences[temperature] += 1
    if self.occurrences[temperature] > self.max_occurrences:
      self.mode = temperature
      self.max_occurrences = self.occurrences[temperature]

    if (self.max_temp is None) or temperature > self.max_temp:
      self.max_temp = temperature
    if (self.min_temp is None) or temperature < self.min_temp:
      self.min_temp = temperature

  # Return highest temperature seen so far
  # O(1) Space and time
  def get_max(self):
    return self.max_temp

  # Return lowest temperature seen so far
  # O(1) space and time
  def get_min(self):
    return self.min_temp

  # Return mean
  def get_mean(self):
    return self.mean

  # Return Mode
  def get_mode(self):
    return self.mode


