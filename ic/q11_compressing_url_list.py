# I wrote a crawler that visits web pages, stores a few keywords in a database, 
# and follows links to other web pages. I noticed that my crawler was wasting a 
# lot of time visiting the same pages over and over, so I made a set, visited, 
# where I'm storing URLs I've already visited. Now the crawler only visits a URL 
# if it hasn't already been visited.

# Thing is, the crawler is running on my old desktop computer in my parents' 
# basement (where I totally don't live anymore), and it keeps running out of 
# memory because visited is getting so huge.

# How can I trim down the amount of space taken up by visited?


# O(26^n)
class Trie:
  def __init__(self):
    self.root_node = {}

  def check_present_and_add(self, word):
    current_node = self.root_node
    is_new_word = False

    # Work downwards in the trie, adding the nodes
    # as needed, and keeping track of whether we add
    # any nodes.
    for char in word:
      if char not in current_node:
        is_new_word = True
        current_node[char] = {}
      current_node = current_node[char]

    # Mark the end of a word
    if "End of Word" not in current_node:
      is_new_word = True
      current_node["End of Word"] = {}

    return is_new_word