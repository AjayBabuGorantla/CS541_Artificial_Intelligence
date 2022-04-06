from State import State
from queue import PriorityQueue
    
def greedy_search(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    # evaluation = root.heuristic_manhattan_distance(n) #we can use heuristic_misplaced_tiles(n) instead.
    # evaluation = root.heuristic_misplaced_tiles(n)
    evaluation = root.heuristic_combined(n)
    frontier.put((evaluation[0], counter, root)) #based on greedy evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                # evaluation = child.heuristic_manhattan_distance(n) #we can use heuristic_misplaced_tiles(n) instead.
                # evaluation = child.heuristic_misplaced_tiles(n)
                evaluation = child.heuristic_combined(n)
                frontier.put((evaluation[0], counter, child)) #based on greedy evaluation
    return


def AStar_search(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    # evaluation = root.heuristic_manhattan_distance(n) #we can use heuristic_misplaced_tiles(n) instead.
    # evaluation = root.heuristic_misplaced_tiles(n)
    evaluation = root.heuristic_combined(n)
    frontier.put((evaluation[1], counter, root)) #based on A* evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                # evaluation = child.heuristic_manhattan_distance(n) #we can use heuristic_misplaced_tiles(n) instead.
                # evaluation = child.heuristic_misplaced_tiles(n)
                evaluation = root.heuristic_combined(n)
                frontier.put((evaluation[1], counter, child)) #based on A* evaluation
    return
