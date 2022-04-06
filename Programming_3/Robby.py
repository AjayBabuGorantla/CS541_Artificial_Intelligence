import numpy as np
import random
from matplotlib import pyplot as plt

class Robby():
    def __init__(self, x = 0, y = 0, reward = 0, cans_collected = 0):
        self.x = x
        self.y = y
        self.reward = reward
        self.cans_collected = cans_collected
    
    #Sensors
    def sense_current(self, grid):
        return grid[self.x][self.y]
    
    def sense_north(self, grid):
        return grid[self.x][self.y+1]

    def sense_south(self, grid):
        return grid[self.x][self.y-1]
    
    def sense_west(self, grid):
        return grid[self.x-1][self.y]
    
    def sense_east(self, grid):
        return grid[self.x+1][self.y]
    
    #Actions
    def move_north(self, grid):
        if(self.sense_north(grid) == 3): #checks if the square to the north is a wall
            return False
        self.y = self.y + 1
        return True
    
    def move_south(self, grid):
        if(self.sense_south(grid) == 3): #checks if the square to the south is a wall
            return False
        self.y = self.y - 1
        return True
    
    def move_west(self, grid):
        if(self.sense_west(grid) == 3): #checks if the square to the west is a wall
            return False
        self.x = self.x - 1
        return True

    def move_east(self, grid):
        if(self.sense_east(grid) == 3): #checks if the square to the east is a wall
            return False
        self.x = self.x + 1

    def pickup_can(self, grid):
        if(self.sense_current(grid) == 1):
            grid[self.x][self.y] = 0   #removes the can from grid
            return True
        else:
            return False

    def state(self, grid):
        state_tuple = (self.sense_current(grid), self.sense_north(grid), self.sense_south(grid),self.sense_east(grid),self.sense_west(grid))

        return state_tuple

    def select_action(self, current_state, Q_matrix, epsilon_value):
        if(random.randint(1, 100) <=(100 * epsilon_value)):
            action = random.randint(0,4)
            return action

        possible_actions = list()
        q_value_pick_up = Q_matrix[current_state][0]
        possible_actions.append(q_value_pick_up)
        q_value_move_north = Q_matrix[current_state][1]
        possible_actions.append(q_value_move_north)
        q_value_move_south = Q_matrix[current_state][2]
        possible_actions.append(q_value_move_south)
        q_value_move_east = Q_matrix[current_state][3]
        possible_actions.append(q_value_move_east)
        q_value_move_west = Q_matrix[current_state][4]
        possible_actions.append(q_value_move_west)

        max_q_value = max(possible_actions)
        if(max_q_value == q_value_pick_up):
            action = 0
        if(max_q_value == q_value_move_north):
            action = 1
        if(max_q_value == q_value_move_south):
            action = 2
        if(max_q_value == q_value_move_east):
            action = 3
        if(max_q_value == q_value_move_west):
            action = 4

        return action
    
    def perform_action(self, action, grid):
        if(action==0):
            action_result = self.pickup_can(grid)
            if(action_result == True):
                self.cans_collected = self.cans_collected + 1
                return 10 #reward for picking up the can

            else:
                return -1 #reward for trying to picking up a can in an empty square
        
        elif(action==1):
            action_result = self.move_north(grid)
            if(action_result == True):
                return 0
            else:
                return -5 #reward hitting a wall
        
        elif(action==2):
            action_result = self.move_south(grid)
            if(action_result == True):
                return 0
            else:
                return -5 #reward for hitting a wall

        elif(action==3):
            action_result = self.move_east(grid)
            if(action_result == True):
                return 0
            else:
                return -5 #reward for hitting a wall
        
        elif(action==4):
            action_result = self.move_west(grid)
            if(action_result == True):
                return 0
            else:
                return -5 #reward for hitting a wall
        
    def Episode(self, grid, Q_matrix, epsilon_value, M, learning_rate, gamma_value):
        # M = 200 #No of steps
        # learning_rate = 0.2
        # gamma_value = 0.9
        counter = 0

        while(counter<M):
            current_state = self.state(grid)
            if(current_state not in Q_matrix):
                Q_matrix[current_state] = np.zeros(5)
            action = self.select_action(current_state, Q_matrix, epsilon_value)
            reward = self.perform_action(action, grid)
            self.reward = self.reward + reward
            new_state = self.state(grid)
            if(new_state not in Q_matrix):
                Q_matrix[new_state] = np.zeros(5)
            Q_matrix[current_state][action] = Q_matrix[current_state][action] + learning_rate * (reward + gamma_value * (max(Q_matrix[new_state]) - Q_matrix[current_state][action]))
            counter+=1

    def Train(self, Q_matrix, N, M, epsilon_value, learning_rate, gamma_value):
        counter = 0
        reward_list = list()

        while(counter < N):
            grid = np.random.randint(2, size = (12,12)) # Creates a 12X12 grid(we will create a wall in later steps which makes it a 10X10)
            for i, temp_i in enumerate(grid):
                for j, temp_j in enumerate(grid[i]):
                    if(i==0 or i ==11 or j == 0 or j == 11):
                        grid[i][j] = 3

            #randomly places Robby in a location
            self.x = random.randint(1,10)
            self.y = random.randint(1,10)
            self.cans_collected = 0
            self.reward = 0
            self.Episode(grid, Q_matrix, epsilon_value, M, learning_rate, gamma_value)
            
            print("Episode: ", counter)
            print("Cans Collected: ", self.cans_collected)
            print("Total Reward: ", self.reward)
            
           

            if((N-counter) % 50 == 0): #reduces the epsilon value gradually after every 50 steps
                epsilon_value = epsilon_value - 0.001 
            if((N-counter) % 100 == 0): #adds reward for every 100 episodes
                reward_list.append(self.reward)
            counter+=1

        print("Average Reward(Training): ", sum(reward_list)/(N/100)) #Average value of reward across every 100 episodes
        # y_values = 
        average_train_reward = sum(reward_list)/(N/100)
        plt.title("Training Episodes\nN = {0}, M = {1}\nAverage Reward = {2}".format(N, M, average_train_reward))
        plt.xlabel("Episodes")
        plt.ylabel("Reward")
        plt.plot(list(range(0,N,100)),reward_list)
        plt.show()

        return Q_matrix
    
    def test_episode(self, grid, Q_matrix, M, epsilon_value):
        counter = 0
        while(counter<M):
            current_state = self.state(grid)
            action = self.select_action(current_state, Q_matrix, epsilon_value)
            reward = self.perform_action(action, grid)
            self.reward +=reward
            counter+=1

    def Test(self, Q_matrix, N, M, epsilon_value):
        counter = 0 
        reward_list = list()
        while(counter < N):
            grid = np.random.randint(2, size = (12,12)) # Creates a 12X12 grid(we will create a wall in later steps which makes it a 10X10)
            for i, temp_i in enumerate(grid):
                for j, temp_j in enumerate(grid[i]):
                    if(i == 0 or i == 11 or j == 0 or j == 11):
                        grid[i][j] = 3
            self.x = random.randint(1,10)
            self.y = random.randint(1,10)
            self.cans_collected = 0
            self.reward = 0
            self.test_episode(grid, Q_matrix, M, epsilon_value)
            # if((N-counter) % 100 == 0): #adds reward for every 100 episodes
            reward_list.append(self.reward)
            counter+=1
        # print("Average Reward(Test): ", sum(reward_list)/(N/100))
        # average_test_reward = sum(reward_list)/(N/100)
        
        average_test_reward = sum(reward_list)/N
        test_standard_deviation = np.std(np.array(reward_list))
        print("Average Reward(Test): ", average_test_reward)
        print("Standard Deviation(Test): ", test_standard_deviation)
        plt.title("Test Episodes\nN = {0}, M = {1}\nAverage Reward = {2}\nStandard Deviation = {3}".format(N, M, average_test_reward, test_standard_deviation))
        plt.xlabel("Episodes")
        plt.ylabel("Reward")
        plt.plot(list(range(N)),reward_list)
        plt.show()

