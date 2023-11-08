import math
from bees_algorithm import BeesAlgorithm
import matplotlib.pyplot as plt
import time



def foo(x):
    x, y = x
    term1 = 1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * x ** 2 - 14 * y + 6 * x * y + 3 * y ** 2)
    term2 = 30 + (2 * x - 3 * y) ** 2 * (18 - 32 * x + 12 * x ** 2 + 48 * y - 36 * x * y + 27 * y ** 2)
    result = term1 * term2
    return -1 * result


search_boundaries = ([-2, -2], [2, 2])

default_parameters = {
    'ns': 10,
    'nb': 5,
    'ne': 1,
    'nre': 15,
    'nrb': 10,
    'stlim': 10,
    'shrink_factor': 0.2,
}

parameters_to_examine = {
    'ns': [10, 15, 20],
    'nb': [5, 10, 15],
    'ne': [1, 2, 3],
    'nre': [15, 25, 30],
    'nrb': [10, 15, 20],
}

for i, (param, values) in enumerate(parameters_to_examine.items()):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    result_values = []
    param_values = []
    times = []
    for value in values:
        bees_parameters = default_parameters.copy()
        bees_parameters[param] = value

        alg = BeesAlgorithm(foo, search_boundaries[0], search_boundaries[1], **bees_parameters)
        t0 = time.time()
        _, result = alg.performFullOptimisation(max_iteration=200)
        t1 = time.time()
        times.append(t1 - t0)
        result_values.append(math.floor(result))
        param_values.append(value)

    ax = ax1
    ax.plot(param_values, result_values, marker='o')
    ax.set_xlabel(param)
    ax.set_ylabel('Result')
    ax.set_title(f'Impact of {param} on Result')

    ax = ax2
    ax.plot(param_values, times, marker='o')
    ax.set_xlabel(param)
    ax.set_ylabel('Time')
    ax.set_title(f'Impact of {param} on Time')
    plt.tight_layout()
    plt.show()

alg = BeesAlgorithm(foo, search_boundaries[0], search_boundaries[1])
result_values = []
for _ in range(1000):
    alg.performSingleStep()
    best = alg.best_solution
    result = best.score
    result_values.append(math.floor(result))

plt.plot(list(range(1, 1001)), result_values)
plt.xlabel('Result')
plt.ylabel('Iteration')
plt.title('Best result thru iterations')
plt.show()
alg.visualize_iteration_steps()
