weights = [ [0.1, 0.1, -0.3],  #hurt?
            [0.1, 0.2, 0.0],   #win?
            [0.0, 1.3, 0.1] ]  #sad?  
            #toes %win #fans

def dot(K, L):
    
    # Created for ease of calculating dot product
    # Ref. : https://stackoverflow.com/questions/32669855/dot-product-of-two-lists-in-python/32669935
    if len(K) != len(L):
        return 0
    
    return sum(i[0] * i[1] for i in zip(K, L))

def vect_mat_mul(vect,matrix):
    
    # Performs :
    # dot(inp,matrix[0])
    # dot(inp,matrix[1])
    # dot(inp,matrix[2])

    assert(len(vect) == len(matrix))
    output_list = []

    for i in range(len(matrix)):
        output_list.append(dot(vect, matrix[i]))
    
    return output_list

def neural_network(input_vect, weights):
    pred = vect_mat_mul(input_vect,weights)
    
    return pred

""" 
This dataset is the current
status at the beginning of
each game for the first 4 games
in a season.
toes = current number of toes
wlrec = current games won (percent)
nfans = fan count (in millions)
"""
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65,0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

# input corresponds to every entry
# for the first game of the season
inp = [toes[0],wlrec[0],nfans[0]]
pred = neural_network(inp,weights)

print(pred)

# We need dot method to multiple our 1D vector to each 1D list in out matrix
     #toes          %win          #fans
# (8.5 * 0.1) + (0.65 * 0.1) + (1.2 * -0.3) = 0.555 = hurt prediction => dot(inp,matrix[0])
# (8.5 * 0.1) + (0.65 * 0.2) + (1.2 * 0.0) = 0.98 = win prediction    => dot(inp,matrix[1])
# (8.5 * 0.0) + (0.65 * 1.3) + (1.2 * 0.1) = 0.965 = sad prediction   => dot(inp,matrix[2])