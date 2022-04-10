from player import Player
import numpy as np
from config import CONFIG

import math
import random

from copy import deepcopy

import pickle
import os

standard_noise_div_weights = 100000
standard_noise_div_biases = 80000


class ArrayPlayers:
    def __init__(self, players):
        self.players = players


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # TODO
        # child: an object of class `Player`
        child.nn.matrix1 += np.random.normal(0, standard_noise_div_weights, child.nn.matrix1.shape)
        child.nn.matrix2 += np.random.normal(0, standard_noise_div_weights, child.nn.matrix2.shape)

        child.nn.bias1 += np.random.normal(0, standard_noise_div_biases, child.nn.bias1.shape)
        child.nn.bias2 += np.random.normal(0, standard_noise_div_biases, child.nn.bias2.shape)

        return child

    def cross_over(self, parent1, parent2):

        parent1.nn.matrix2 = parent2.nn.matrix2
        parent1.nn.bias1 = parent2.nn.bias1
        return parent1

    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            # if os.path.exists("TrainedPlayers2"):
            #     with open('TrainedPlayers2', 'rb') as f2:
            #         result = pickle.load(f2)
            #     return result.players
            # else:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # if os.path.exists("TrainedPlayers2"):
            #     os.remove("TrainedPlayers2")
            # with open('TrainedPlayers2', 'wb') as f:
            #     pickle.dump(ArrayPlayers(prev_players), f)

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            probabilities = []

            sum_fitness = 0
            for i in range(0, len(prev_players)):
                probabilities.append(prev_players[i].fitness)
                sum_fitness += prev_players[i].fitness

            probabilities = np.array(probabilities)
            vector_probability = np.vectorize(self.calculate_probability)
            probabilities = vector_probability(self, probabilities, sum_fitness)

            choose = []
            for i in range(0, len(probabilities)):
                for j in range(0, probabilities[i]):
                    choose.append(i)

            choose = random.sample(choose, len(choose))

            result = []
            for i in range(0, num_players):
                rnd1 = random.randint(0, len(choose) - 1)
                rnd2 = random.randint(0, len(choose) - 1)
                index1 = choose[rnd1]
                index2 = choose[rnd2]
                parent1 = deepcopy(prev_players[index1])
                parent2 = prev_players[index2]
                child = self.cross_over(parent1, parent2)
                result.append(self.mutate(child))
            return result

            # erfan
            # fitnesses = []
            # for pervert in prev_players:
            #     fitnesses.append(pervert.fitness ^ 4)
            # chosen = random.choices(prev_players, weights=fitnesses, cum_weights=None, k=num_players)
            # babies = []
            # for parent in chosen:
            #     babies.append(self.mutate(deepcopy(parent)))
            # return babies

    def next_population_selection(self, players, num_players):

        # TODO
        # num_players example: 100
        # players: an array of `Player` objects

        # TODO (additional): a selection method other than `top-k`
        # TODO (additional): plotting

        probabilities = []

        sum_fitness = 0
        for i in range(0, len(players)):
            probabilities.append(players[i].fitness)
            sum_fitness += players[i].fitness

        probabilities = np.array(probabilities)
        vector_probability = np.vectorize(self.calculate_probability)
        probabilities = vector_probability(self, probabilities, sum_fitness)

        choose = []
        for i in range(0, len(probabilities)):
            for j in range(0, probabilities[i]):
                choose.append(i)

        choose = random.sample(choose, len(choose))

        result = []
        for i in range(0, num_players):
            rnd = random.randint(0, len(choose) - 1)
            index = choose[rnd]
            result.append(deepcopy(players[index]))

        average = 0
        min = players[0].fitness
        max = players[0].fitness
        for player in players:
            average += player.fitness
            if player.fitness > max:
                max = player.fitness
            if player.fitness < min:
                min = player.fitness
        average = average / len(players)

        with open('Results.txt', 'a') as file:
            file.write(str(min) + "   ")
            file.write(str(average) + "   ")
            file.write(str(max) + "   ")

            file.write("\n")
        file.close()

        return result

        # erfan
        # players.sort(key=lambda x: x.fitness, reverse=True)
        # return players[: num_players]

    @staticmethod
    def calculate_probability(self, fitness, fitness_sum):

        fitness /= fitness_sum
        fitness *= 100000
        fitness = math.floor(fitness)
        return fitness
