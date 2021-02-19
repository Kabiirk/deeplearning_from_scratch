import numpy as np

# Predictions with multiple inputs
weights = [0.1, 0.2, 0]

def w_sum(a,b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    
    return output

def neural_network(inputs, weights):
    pred = w_sum(inputs, weights)
    return pred


# This dataset is the current
# status at the beginning of
# each game for the first 4 games
# in a season.
# toes = current number of toes
# wlrec = current games won (percent)
# nfans = fan count (in millions)
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

# input corresponds to every entry
# for the first game of the season
inp = [toes[0],wlrec[0],nfans[0]]
pred = neural_network(inp,weights)
print(pred) # = 0.98


# input   weight   local prediction
# ( 8.50 * 0.1 ) = 0.85 = toes prediction
# ( 0.65 * 0.2 ) = 0.13 = wlrec prediction
# ( 1.20 * 0.0 ) = 0.00 = fans prediction
# toes prediction + wlrec prediction + fans prediction = final prediction
#       0.85      +     0.13         +     0.00        =     0.98


# Now the same code but in Numpy

weights = np.array([0.1, 0.2, 0])

def neural_net(np_inp, np_weight):
    pred = np_inp.dot(np_weight)
    
    return pred

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])
# input corresponds to every entry
# for the first game of the season

input = np.array([toes[0],wlrec[0],nfans[0]])
pred = neural_network(input,weights)
print(pred) # = 0.98