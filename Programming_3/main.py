import numpy as np
import random
from matplotlib import pyplot as plt
from Robby import Robby


def main():
    N = 5000 #number of episodes
    M = 200 #no of steps in each episode
    learning_rate = 0.2 
    gamma_value = 0.9
    epsilon_value = 0.1

    #Initialise empty Q Matrix (a dictionary)
    Q_matrix = dict()

    robot = Robby()
    Q_matrix_trained = robot.Train(Q_matrix, N, M, epsilon_value, learning_rate, gamma_value)
    print("size of Q Matrix: ",len(Q_matrix_trained))
    robot.Test(Q_matrix_trained, N, M, epsilon_value)


if __name__ == "__main__":
    main()






