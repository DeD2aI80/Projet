import numpy as np

class Network:

    def __init__(self, layers, weights = 0, biases = 0): # ,f):

        self.layers = layers
        
        if  weights == 0 and biases == 0:
            self.weights = [np.random.randn(x, y) for x, y in zip(layers[:-1], layers[1:])]
            self.biases = [np.random.randn(1, y) for y in layers[1:]]
        else:
            self.weights = weights
            self.biases = biases

        #self.f = activation[f]
        #self.fPrime = activationPrime[f]
     
     
    def forward(self, X):
        if isinstance(X, type([])):
            X = np.array(X)
        
        Y = X
        self.hidden = [X]
        for w,b in zip(self.weights, self.biases):
            #print type(X), type(w), np.shape(w), type(b)
            Y = Y.dot(w) + b
            #Y = self.f(Y)
            #self.hidden.append(Y)            

        return Y