from functions import *


##################### محمد محمود ابراهيم ابوالليل#####################
class SearchAgent:
    def __init__(self, CurrentState, strategy, goal):
        self.Moves = None
        self.CurrentState = CurrentState  # initial State of Puzzle
        self.Changepuzzle = None
        self.Display = None
        self.AvailableMoves = None
        self.SelectInput = None
        self.ChangePuzzle = None
        self.Check = None
        self.strategy = strategy
        self.goal = goal
        self.MovesCost = None
        self.PuzzleMoves = None

    def Play(self):
        self.Display(self.CurrentState)
        self.Moves = self.AvailableMoves(self.CurrentState)
        move = self.SelectInput(self.Moves)
        self.CurrentState = self.ChangePuzzle(self.CurrentState.copy(), move)
        return self.Check(self.CurrentState)

    def isgoal(self, State):
        if State == self.goal:
            return True

    def select_node(self, fringe):
        if self.strategy == 'DFS': return -1
        if self.strategy == 'BFS': return 0
        if self.strategy == 'UCS': return self.get_min('cost', fringe)

    def solve(self):

        fringe = []
        visited = []
        initial_node = self.init_node(self.CurrentState)
        fringe.append(initial_node)
        while len(fringe) > 0:
            current_node = fringe.pop(self.select_node(fringe))
            if current_node['state'] in visited: continue
            visited.append(current_node['state'])
            #print(current_node['path']); #input()
            if self.isgoal(current_node['state']):
                return self.get_solution(current_node, len(visited))
            possible_actions = self.AvailableMoves(current_node['state'])
            for action in possible_actions:
                next_node = self.add_node(current_node, action)
                fringe.append(next_node)
        return None

    def get_min(self, key, fringe):
        idx_min = 0
        for i in range(1, len(fringe)):
            if fringe[i][key] < fringe[idx_min][key]:
                idx_min = i
        return idx_min

    def init_node(self, intial_state):
        initial_node = {}
        initial_node['state'] = intial_state
        initial_node['path'] = []
        if self.strategy == 'UCS': initial_node['cost'] = 0
        return initial_node

    def add_node(self, current_node, action):
        next_node = {}
        next_node['state'] = self.ChangePuzzle(current_node['state'].copy(),action)
        next_node['path'] = current_node['path'][:]
        next_node['path'].append(action)
        if self.strategy == 'UCS':
            next_node['cost'] = current_node['cost'] + self.compute_cost(
                action, current_node['state'])
        return next_node

    def compute_cost(self, action, current_node):
        return self.MovesCost[action]

    def get_solution(self, current_node, time):
        solution = {}
        solution['solution'] = current_node['path']
        solution['time'] = time
        if self.strategy == 'UCS':
            solution['cost'] = current_node['cost']
        return solution


State = [1, 2, 0, 3, 4, 5, 6, 7, 8]
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
Puzzle = SearchAgent(State, "DFS", goal)
Puzzle.Display = display
Puzzle.AvailableMoves = AvailableMoves
Puzzle.SelectInput = SelectInput
Puzzle.ChangePuzzle = ChangePuzzle
Puzzle.Check = Check
Puzzle.PuzzleMoves = ['v', '<', '>','^']  ### only if there is a cost as in UCS
Puzzle.MovesCost = {
    'v': 1,
    '<': 1,
    '>': 1,
    '^': 1
}  ### only if there is a cost as in UCS
print(Puzzle.solve())  #solve way


def Diplay():
    while True:
        if not Puzzle.Play():
            print("YOU WIN")
            break


#To Play Your game which is 8-puzzle
# Diplay()
