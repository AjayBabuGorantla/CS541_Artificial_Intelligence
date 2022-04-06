import numpy as np

class State:
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0] 

    #e.g. the goal state should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0] if n is 4.
    
    greedy_evaluation = None
    AStar_evaluation = None
    heuristic = None
    def __init__(self, state, parent, direction, depth, cost):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth

        if parent:
            self.cost = parent.cost + cost

        else:
            self.cost = cost

    def test(self): #check if the given state is goal
        if self.state == self.goal:
            return True
        return False
        
    #heuristic function based on Manhattan distance
    def heuristic_manhattan_distance(self ,n): 
        self.heuristic = 0
        
        for i in range(1 , n*n):
            distance = abs(self.state.index(i) - self.goal.index(i))
            
            #manhattan distance between the current state and goal state
            self.heuristic = self.heuristic + distance/n + distance%n

        self.greedy_evaluation = self.heuristic    
        self.AStar_evaluation = self.heuristic + self.cost
        
        return( self.greedy_evaluation, self.AStar_evaluation)


    def heuristic_misplaced_tiles(self,n): 
        counter = 0
        self.heuristic = 0
        for i in range(n*n):
            if (self.state[i] != self.goal[i]):
                counter += 1
        self.heuristic = self.heuristic + counter

        self.greedy_evaluation = self.heuristic    
        self.AStar_evaluation = self.heuristic + self.cost

        return( self.greedy_evaluation, self.AStar_evaluation)                

    def heuristic_combined(self, n):
        self.heuristic_manhattan = 0

        for i in range(1 , n*n):
            distance = abs(self.state.index(i) - self.goal.index(i))
            
            #manhattan distance between the current state and goal state
            self.heuristic_manhattan = self.heuristic_manhattan + distance/n + distance%n

        counter = 0
        self.heuristic_misplaced = 0

        for i in range(n*n):
            if (self.state[i] != self.goal[i]):
                counter += 1
        self.heuristic_misplaced = self.heuristic_misplaced + counter

        self.heuristic = self.heuristic_manhattan + self.heuristic_misplaced

        self.greedy_evaluation = self.heuristic    
        self.AStar_evaluation = self.heuristic + self.cost

        return( self.greedy_evaluation, self.AStar_evaluation)


    @staticmethod
    
    #this would remove illegal moves for a given state
    def available_moves(x,n): 
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n-1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n*n - 1:
            moves.remove('Down')

        return moves

    #produces children of a given state
    def expand(self , n): 
        x = self.state.index(0)
        moves = self.available_moves(x,n)
        
        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]
        
        
            children.append(State(temp, self, direction, self.depth + 1, 1)) #depth should be changed as children are produced
        return children
         
    def solution(self):
        solution = []
        solution.append(self.state)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.state)
        solution = solution[:-1]
        solution.reverse()
        return solution