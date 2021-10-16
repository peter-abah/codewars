# Can You Get the Loop
# KATA LINK: https://www.codewars.com/kata/52a89c2ea8ddc5547a000863

# You are given a node that is the beginning of a linked list. This list always contains a tail and a loop. 
# Your objective is to determine the length of the loop.


def loop_size(node):
  d = {}
  i = 0
  while True:
    if node in d:
      break
    d[node] = (i, node.next)
    node_n = node
    node = node.next
    i += 1
      
  return d[node_n][0] - d[d[node_n][1]][0] + 1
        