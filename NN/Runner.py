from NN import Network

def f(x):
    return 1 if x > 0 else 0


def get_training_dataset():
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    labels = [[1], [0], [0], [0]]
    return input_vecs, labels


def train_and_perceptron():
    network = Network.Network([2,1,2])
    input_vecs, labels = get_training_dataset()
    network.train(labels,input_vecs,0.1, 10)
    return network

def get_result(x):
    return 1 if x > 0 else 0


if __name__ == '__main__':
    network = train_and_perceptron()
    print(network)

    print('1 and 1 = ',end=" ")
    print(get_result(list(network.predict([1, 1]))[0]))

