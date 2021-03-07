            #toes %win #fans
ih_wgt = [ [0.1, 0.2, -0.1],#hid[0]
           [-0.1,0.1, 0.9], #hid[1]
           [0.1, 0.4, 0.1] ]#hid[2]

           # hid[0] hid[1] hid[2]
hp_wgt = [ [0.3, 1.1, -0.3],#hurt?
           [0.1, 0.2, 0.0], #win?
           [0.0, 1.3, 0.1] ]#sad?

weights = [ih_wgt, hp_wgt]

# FUNCTIONS 
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

# NEURAL NETWORK
def neural_network(input, weights):
    # Stacking of NN happens here !
    hid = vect_mat_mul(input,weights[0]) # Hidden Layer
    pred = vect_mat_mul(hid,weights[1]) # Output Layer
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65,0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

# input corresponds to every entry
# for the first game of the season
input = [toes[0],wlrec[0],nfans[0]]
pred = neural_network(input,weights)

print(pred)