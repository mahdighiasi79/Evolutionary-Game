# This is a sample Python script.
import math
import matplotlib.pyplot as plt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.


def parse(string):

    float_point = string.find('.')
    if float_point == -1:
        float_point = len(string)

    int_value = 0
    for j in range(0, float_point):
        temp = ord(string[float_point - j - 1])
        temp -= 48
        int_value += temp * math.pow(10, j)

    float_value = 0
    string = string[float_point + 1:]
    for j in range(0, len(string)):
        temp = ord(string[len(string) - j - 1])
        temp -= 48
        float_value += temp * math.pow(10, j)
    float_value *= math.pow(10, -len(string))

    return int_value + float_value


if __name__ == '__main__':

    with open('D:\computer\Computational Intelligence\EvolutionaryGames-main\Results.txt') as f:
        lines = f.readlines()

    mines = []
    averages = []
    maxes = []

    for line in lines:
        space = line.find(' ')
        mines.append(parse(line[0: space]))
        line = line[space + 3:]
        space = line.find(' ')
        averages.append(parse(line[0: space]))
        line = line[space + 3:]
        space = line.find(' ')
        maxes.append(parse(line[0: space]))

    generations = []
    for i in range(0, len(lines)):
        generations.append(i + 1)

    plt.plot(generations, mines, label="minimums")
    plt.plot(generations, averages, label="averages")
    plt.plot(generations, maxes, label="maximums")

    plt.xlabel('generation')
    plt.title('evolution')
    plt.legend()
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
