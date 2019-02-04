import numpy as np
import math
import matplotlib.pyplot as plt

D = 1000
d = 100


# helper function: calculate the angle within [0, pi) between two vectors
def ang_vectors(v1, v2):
    """

    :param v1: vector1, n-d array
    :param v2: vector2, n-d array
    :return: angle between v1 and v2 in degree
    """
    cos = np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    # print(cos)
    if cos>1:
        cos = 1
    return math.degrees(math.acos(cos))


# method 1:
np.random.seed(1)
# generate D orthonormal D-dim vecotrs
vecs_D = np.identity(D)
# generate d random Gaussian D-dim vectors as coordinate vecotrs
vecs_d = np.random.multivariate_normal(np.zeros(D), np.identity(D), size=d).T

# the (D, d) matrix in which each row is a projected vector
projs = np.matmul(vecs_D, vecs_d)



# method 2:
np.random.seed(200)

vecs_d_2 = np.random.multivariate_normal(np.zeros(d), np.identity(d), size=D)



# evaluation
def eval(vecs, num):
    stats = []
    for i in range(D):
        for j in range(i, D):
            ang = ang_vectors(vecs[i], vecs[j])
            stats.append(ang)

    n, bins, patch = plt.hist(stats, bins=72, range=(0, 180))
    plt.plot(bins)
    plt.xlabel("pairwise angle")
    plt.ylabel("# of pairs")
    plt.title("method "+str(num))
    plt.show()
    # print(len(stats))
    # print(stats[0:20])



eval(projs, 1)
eval(vecs_d_2, 2)

