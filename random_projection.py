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

stats1 = [0]*18
for i in range(D):
    for j in range(i, D):
        # cos = np.dot(projs[i], projs[j]) / (np.linalg.norm(projs[i]) * np.linalg.norm(projs[j]))
        # print(cos)
        ang = ang_vectors(projs[i], projs[j])
        idx = int(ang/10)
        stats1[idx] += 1
#
# for i in range(18):
#     print(str(i*10)+":")
#     print(stats[i])




# method 2:
np.random.seed(200)

vecs_d_2 = np.random.multivariate_normal(np.zeros(d), np.identity(d), size=D)

stats2 = [0]*18
for i in range(D):
    for j in range(i, D):
        # cos = np.dot(projs[i], projs[j]) / (np.linalg.norm(projs[i]) * np.linalg.norm(projs[j]))
        # print(cos)
        ang = ang_vectors(vecs_d_2[i], vecs_d_2[j])
        idx = int(ang/10)
        stats2[idx] += 1

for i in range(18):
    print(str(i*10)+":")
    print(stats1[i], stats2[i])


x = np.arange(18)*10
y = np.array(stats2)
pic = plt.plot(x, y)
plt.show()