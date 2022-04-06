from helper_functions import *

def main():
    chromosome_size = 8
    population_size = 500

    max_attacking_pairs = int((chromosome_size * (chromosome_size - 1))/2)
    max_iterations = 100
    mutation_probability = 0.001

    population = initialize_population(population_size, chromosome_size)
    population = calculate_survival_probability(population)

    # print_population(population)

    print("......Some samples from Initial Population........\n")
    random_sampling(population)
    
    average_fitness_list = list()

    population_generation_number_list = [i for i in range(max_iterations)]

    iteration = 0
    
    while (iteration!=max_iterations):
        population = Evolution(population, chromosome_size, mutation_probability)
        population = calculate_survival_probability(population)
        average_fitness_list.append(calculate_average_fitness(population))
        # print(iteration)
        # print(population[0].sequence)
        # print(len(population))
        iteration+=1

    print(".....some samples from the final population......\n")
    random_sampling(population)

    plot_graph(population_generation_number_list, average_fitness_list, mutation_probability, len(population))


    # parent_1, parent_2 = select_parents(population)

    # print(parent_1.sequence, parent_2.sequence)

    # for i in range(len(population)):
    #     print(population[i].survival_probability)
    # print_population(population)
    

if __name__ == "__main__":
    main()    