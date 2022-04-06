from bestFS_search_algorithms import greedy_search, AStar_search


#count the number of inversions       
def number_of_inversions(puzzle):
    inversion_count = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            if(i!=j and puzzle[i]!=0 and puzzle[j]!=0):
                if(puzzle[i]>puzzle[j]):
                    inversion_count += 1
            else:
                continue
    return inversion_count

def check_if_puzzle_is_solvable(puzzle): #check if initial state puzzle is solvable: number of inversions should be even.
    inversion_number = number_of_inversions(puzzle)
    print("The number of inversions are: ",inversion_number)
    if (inversion_number %2 ==0):  #because the present goal state is constant and its parity is even, however if goal state changes additional functionality needs to be added for checking odd parity
        return True
    return False

def main():

    #buidling the initial state

    print("\nPlease enter the value of n when prompted...............\n\n(for your reference 'n' is the number of rows/number of columns in your puzzle. For e.g. n=3 if it's a 3X3 puzzle)")
    n = int(input("\nNow enter the value of n\n"))
    print("Enter your" ,n,"*",n, "puzzle. Press enter after entering each value until you input the 9th value of the puzzle")
    root = []
    for i in range(0,n*n):
        entry = int(input())
        root.append(entry)

    print("The given state is:", root)
    print("\n")

    if check_if_puzzle_is_solvable(root):

        greedy_solution = greedy_search(root, n)
        print('The solution path found using Greedy best first search algorithm is\n\n', greedy_solution[0])
        # print('Number of explored nodes is ', Greedy_solution[1])   
        print('\nNumber of steps taken to reach the goal is: ', len(greedy_solution[0]))
        
        print("\n")

        AStar_solution = AStar_search(root, n)
        print('The solution path found using A* search algorithm is\n\n', AStar_solution[0])
        # print('Number of explored nodes is ', AStar_solution[1])   
        print('\nNumber of steps taken to reach the goal is: ', len(AStar_solution[0]))
        
        
    else:
        print("Oops! The given puzzle cannot reach the goal. Try another puzzle.\n(Hint: ensure its parity matches the goal state;)")

if __name__=="__main__":
    main()


     