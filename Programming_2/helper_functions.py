import numpy as np
import random
from matplotlib import pyplot as plt

class BoardState:

    def __init__(self):
        self.sequence = None
        self.fitness = None
        self.survival_probability = None

    def set_sequence(self, value):
        self.sequence = value
    
    def set_fitness(self, value):
        self.fitness = value
    
    def set_survival_probability(self, value):
        self.survival_probability = value

    def get_features(self):
        return {'sequence':self.sequence, 'fitness': self.fitness, 'survival_probability':self.survival_probability}


# def initialize_population(population_size, chromosome_size):
#     population = list()

#     for i in range(population_size):
#         random_gene = np.random.randint(low = 0, high = chromosome_size -1, size = chromosome_size )
#         population.append(random_gene)

#     return population

def calculate_fitness(chromosome_size, sequence):
    
    maximum_possible_attacking_pairs = (chromosome_size * (chromosome_size - 1))/2
    
    attacking_pairs = 0
    
    for current_gene in range(0, len(sequence)):

        current_queen_position = [current_gene, sequence[current_gene]]

        for previous_gene in range(0, current_gene):

            previous_queen_position = [previous_gene, sequence[previous_gene]]

            slope = (current_queen_position[1] - previous_queen_position[1]) / (current_queen_position[0] - previous_queen_position[0])

            if slope == 0:
                attacking_pairs+=1

            elif (slope == 1 or slope == -1):
                attacking_pairs += 1

    return maximum_possible_attacking_pairs - attacking_pairs


def initialize_population(population_size, chromosome_size):
    population = list()

    for i in range(population_size):
        random_gene_sequence = np.random.randint(low = 0, high = chromosome_size -1, size = chromosome_size )
        new_board_state = BoardState()
        new_board_state.set_sequence(random_gene_sequence)
        new_board_state.set_fitness(calculate_fitness(chromosome_size, new_board_state.sequence))
        population.append(new_board_state)

    return population


def calculate_survival_probability(population):
    
    total_fitness = 0
    
    for i in range(len(population)):
        total_fitness += population[i].fitness
    
    for each_state in population:
        survival_probability = each_state.fitness / total_fitness
        each_state.set_survival_probability(survival_probability)

    return population

def calculate_average_fitness(population):
    total_fitness = 0
    for each_chromosome in population:
        total_fitness += each_chromosome.fitness
    
    average_fitness = total_fitness / len(population)

    return average_fitness


def select_parents(population):
    while True:
        parent_1_random_threshold = random.random()
        parent_1_list = list()

        for each_chromosome in population:
            if(each_chromosome.survival_probability <= parent_1_random_threshold):
                parent_1_list.append(each_chromosome)
        if(len(parent_1_list) != 0):
            random_index = random.randint(0, len(parent_1_list)-1)
            parent_1 = parent_1_list[random_index]
            break
        else: 
            # print("Oops! couldn't find parents.. wait a sec, will try again!")
            continue
    
    while True:
        parent_2_random_threshold = random.random()
        parent_2_list = list()

        for each_chromosome in population:
            if(each_chromosome.survival_probability <= parent_2_random_threshold):
                parent_2_list.append(each_chromosome)
        
        if(len(parent_2_list)!=0):
            # random_index = np.random.randint(len(parent_2_list))
            random_index = random.randint(0, len(parent_2_list)-1)
            parent_2 = parent_2_list[random_index]
        
        else:
            continue
            
        if(parent_1!=parent_2):
            break
            
        else:
            # print("Oops! selected same parents, give me a sec, will select different parents")
            continue

    if((parent_1!= None) and (parent_2!=None)):
        return parent_1, parent_2
    else:
        select_parents(population)

def cross_over(parent_1, parent_2, chromosome_size):

    # split_index = np.random.randint(low = 1, high = chromosome_size)
    split_index = random.randint(1, chromosome_size-1)
    child_1 = BoardState()
    child_2 = BoardState()
    
    child_1.set_sequence([])
    child_1.sequence.extend(parent_1.sequence[0:split_index])
    child_1.sequence.extend(parent_2.sequence[split_index:])

    child_2.set_sequence([])
    child_2.sequence.extend(parent_2.sequence[0:split_index])
    child_2.sequence.extend(parent_1.sequence[split_index:])

    child_1.set_fitness(calculate_fitness(chromosome_size,child_1.sequence))
    child_2.set_fitness(calculate_fitness(chromosome_size,child_2.sequence))

    return child_1, child_2

def mutate(child):
    random_index = random.randint(0, len(child.sequence)-1)
    random_value = random.randint(0, len(child.sequence)-1)

    child.sequence[random_index] = random_value

    # print("mutated..yayy!")

    return child

def Evolution(population, chromosome_size, mutation_probability):
    new_population = list()

    for i in range(int(len(population)/2)):
        parent_1, parent_2 = select_parents(population)
        
        child_1, child_2 = cross_over(parent_1, parent_2, chromosome_size)

        if(random.random() < mutation_probability):
            child_1 = mutate(child_1)
        if(random.random() < mutation_probability):
            child_2 = mutate(child_2)

        new_population.append(child_1)
        new_population.append(child_2)

    return new_population


def stop(population, max_attacking_pairs):
    fitness_values = [each_sequence.fitness for each_sequence in population]

    if max_attacking_pairs in fitness_values:
        return True

    return False

def plot_graph(population_generation_list, average_fitness_list, mutation_probability, population_size):
    plt.plot(population_generation_list, average_fitness_list)
    plt.title("Generation Number vs Average Fitness\nMutation_probability : {0}\nPopulation Size : {1}".format(mutation_probability, population_size))
    plt.xlabel("Generation Number")
    plt.ylabel("Average Fitness")
    plt.show()

def print_population(population):
    for each_chromosome in population:
        print(each_chromosome.sequence)

def random_sampling(population):
    for i in range(0,4):
        random_index = random.randint(0, len(population)-1)
        print(population[random_index].sequence)
        print("\n")




