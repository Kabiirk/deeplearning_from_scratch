weights = [ [0.1, 0.1, -0.3],  #hurt?
            [0.1, 0.2, 0.0],   #win?
            [0.0, 1.3, 0.1] ]  #sad?  
            #toes %win #fans

def neural_network(input, weights):
    pred = vect_mat_mul(input,weights)
    
    return pred