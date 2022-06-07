import numpy as np
import random
def sigmoid(x):
    return 1 / (1 + np.exp(x))

tra_in = np.array([[0,0,1],
                [1,1,1],
                [1,0,1],
                [0,1,1],
                [1,0,0]])

tra_out = np.array([[0,1,1,0,1]]).T
np.random.seed(1)
s_w = 2 * np.random.random((3,2)) - 1


for i in range(20000):
    in_l = tra_in
    outputs = sigmoid(np.dot(in_l, s_w))

    err = tra_out - outputs
    adj = np.dot(in_l.T, err * (outputs * (1 - outputs)))

    s_w += adj

print(outputs)
