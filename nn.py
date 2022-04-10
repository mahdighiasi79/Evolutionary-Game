import numpy as np

import math
import random


class NeuralNetwork():

    def __init__(self, layer_sizes):

        # TODO
        # layer_sizes example: [4, 10, 2]
        self.input_size = layer_sizes[0]
        self.hidden_size = layer_sizes[1]
        self.output_size = layer_sizes[2]

        self.matrix1 = []
        self.matrix2 = []

        self.bias1 = []
        self.bias2 = []

        for i in range(0, self.input_size * self.hidden_size):
            self.matrix1.append(random.random())
        self.matrix1 = np.array(self.matrix1)
        self.matrix1 = self.matrix1.reshape(self.input_size, self.hidden_size)

        for i in range(0, self.hidden_size * self.output_size):
            self.matrix2.append(random.random())
        self.matrix2 = np.array(self.matrix2)
        self.matrix2 = self.matrix2.reshape(self.hidden_size, self.output_size)

        for i in range(0, self.hidden_size):
            self.bias1.append(random.random())
        self.bias1 = np.array(self.bias1)

        for i in range(0, self.output_size):
            self.bias2.append(random.random())
        self.bias2 = np.array(self.bias2)

    @staticmethod
    def activation(self, x):

        # result = math.exp(-x)
        # result += 1
        # result = 1 / result
        # return result
        if x > 0:
            return x
        else:
            return 0

    def forward(self, x):

        x = np.array(x)

        hidden_layer = x @ self.matrix1
        hidden_layer += self.bias1
        sigmoid = np.vectorize(self.activation)
        hidden_layer = sigmoid(self, hidden_layer)

        output_layer = hidden_layer @ self.matrix2
        output_layer += self.bias2
        output_layer = sigmoid(self, output_layer)
        return output_layer
