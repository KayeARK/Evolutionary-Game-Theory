import numpy as np
import matplotlib.pyplot as plt

td = (np.array([[0,-1,1],[1,0,-1],[-1,1,0]]), np.array([[0,1,-1],[-1,0,1],[1,-1,0]]))

def get_population(number_of_strategies, size=50):
    population = np.random.randint(0, number_of_strategies, size)
    return population

def get_scores(population, opponents, game):
    return [(game[0][i,j], game[1][i,j]) for i,j in zip(population, opponents)]

def mutate(scores, population, opponents):
    mutated_population = []
    
    for score, strategy_pair in zip(scores, zip(population, opponents)):
        
        if score[1] >= score[0]:
            mutated_population.append(strategy_pair[1])
            
        else:
            mutated_population.append(strategy_pair[0])
            
    return np.array(mutated_population)

def evolve(game, size, generations):
    global history
    population = get_population(len(game[0]), size)
    opponents = get_population(len(game[0]), size)
    
    history = [population]
    
    for _ in range(generations):
        scores = get_scores(population, opponents, game)
        population = mutate(scores, population, opponents)
        opponents = get_population(len(game[0]), size)
        history.append(population)
     
    return history

evolve(td, 197, 200)

length=[]
count0=[]
count1=[]
count2=[]
for i in range(len(history)):
    count0.append(np.count_nonzero(history[i]==0))
    count1.append(np.count_nonzero(history[i]==1))
    count2.append(np.count_nonzero(history[i]==2)) 
    length.append(i)

plt.plot(length, count0, label="First Strategy")
plt.plot(length, count1, label="Second Strategy")
plt.plot(length, count2, label="Third Strategy")
plt.legend(loc='upper left')
plt.xlabel("Generation Number")
plt.ylabel("Population")

plt.show()    