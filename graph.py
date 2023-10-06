# Order:
# Rock, Paper, Scissors, Lizard, Spock.

graph: list =[
  [0, -1, 1, 1, -1],
  [1, 0, -1, -1, 1],
  [-1, 1, 0, 1, -1],
  [-1, 1, -1, 0, 1],
  [1, -1, 1, -1, 0],
]

def getRelation(x: int, y: int)-> int:
  return graph[x][y]
