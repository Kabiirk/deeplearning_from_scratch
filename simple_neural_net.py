weight = 0.1

# 1 Input NN
def neural_network(inp, weight):
    prediction = inp*weight
    return prediction

number_of_entries = [8.5, 9.5, 10, 9]

inp = number_of_entries[0]

pred = neural_network(inp, weight)
print(pred) # = 0.85