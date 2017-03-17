# Write a function that determines if an expression
# is well-parenthesized.

def is_valid(code):
  openers_to_closers = {
    '(' : ')',
    '{' : '}',
    '[' : ']'
  }

  openers = frozenset(openers_to_closers.keys())
  closers = frozenset(openers_to_closers.values())

  openers_stack = []


  for char in code:
    if char in openers:
      openers_stack.append(char)
    elif char in closers:
      if not openers_stack:
        return False
      else:
        last_unopened_opener = openers_stack.pop()

        # Check if closer corresponds to last seen opener
        if not openers_to_closers[last_unopened_opener] == char:
          return False
  return openers_stack = []
