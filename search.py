# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

  def getStartState(self):
     """
     Returns the start state for the search problem
     """
     util.raiseNotDefined()

  def isGoalState(self, state):
     """
       state: Search state

     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state

     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  start_position = problem.getStartState()
  if problem.isGoalState(start_position):
      return []

  path = util.Stack()
  explored = set()
  explored.add(start_position)
  frontier = util.Stack()
  f_set = set()
  for path_node in problem.getSuccessors(start_position):
      frontier.push(path_node)
      f_set.add(path_node[0]) # just the position

  while frontier.isEmpty() != True:
      current_node = frontier.pop()
      f_set.remove(current_node[0])
      current_position = current_node[0]

      #restructure path so that we're tracking the way we got to this node
      while path.isEmpty() != True:
          path_head = path.pop()
          path_successors = [tup[0] for tup in problem.getSuccessors(path_head[0])]
          if current_position in path_successors:
              path.push(path_head)
              break
      path.push(current_node)

      if problem.isGoalState(current_position):
          directions = []
          # unwind the path into a direction list
          while path.isEmpty() != True:
              directions.insert(0,path.pop()[1])
          return directions

      explored.add(current_position)
      successors = [node for node in problem.getSuccessors(current_position) if node[0] not in explored and node[0] not in f_set]
      if len(successors) > 0:
          for path_node in successors:
              frontier.push(path_node)
              f_set.add(path_node[0]) # just the position

  return []

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  start_position = problem.getStartState()
  if problem.isGoalState(start_position):
      return []

  explored = set()
  explored.add(start_position)
  frontier = util.Queue()
  f_set = set()

  for path_node in problem.getSuccessors(start_position):
      frontier.push((path_node, None)) # tuple: node and parent
      f_set.add(path_node[0]) # just the position

  while frontier.isEmpty() != True:
      current_tuple = frontier.pop()
      current_node = current_tuple[0]
      f_set.remove(current_node[0])
      current_position = current_node[0]

      if problem.isGoalState(current_position):
          directions = []
          # unwind the path into a direction list
          path_tuple = current_tuple
          while path_tuple != None:
              directions.insert(0,path_tuple[0][1]) # get the direction for this node
              path_tuple = path_tuple[1]
          return directions

      explored.add(current_position)
      successors = [node for node in problem.getSuccessors(current_position) if node[0] not in explored and node[0] not in f_set]
      if len(successors) > 0:
          for path_node in successors:
              frontier.push((path_node, current_tuple))
              f_set.add(path_node[0]) # just the position

  return []

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
