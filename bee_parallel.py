import time
from bees_algorithm import ParallelBeesAlgorithm


def foo(x):
    x, y = x
    term1 = 1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * x ** 2 - 14 * y + 6 * x * y + 3 * y ** 2)
    term2 = 30 + (2 * x - 3 * y) ** 2 * (18 - 32 * x + 12 * x ** 2 + 48 * y - 36 * x * y + 27 * y ** 2)
    result = term1 * term2
    return -1 * result


search_boundaries = ([-2, -2], [2, 2])

if __name__ == '__main__':
    alg = ParallelBeesAlgorithm(foo, search_boundaries[0], search_boundaries[1])
    t0 = time.time()
    alg.performFullOptimisation(max_iteration=1000)
    best = alg.best_solution
    result = best.score
    t1 = time.time()
    print(f'Parallel alg Result: {result}, Time: {t1 - t0}')
