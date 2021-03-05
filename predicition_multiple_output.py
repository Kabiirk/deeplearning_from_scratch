weights = [ [0.1, 0.1, -0.3],  #hurt?
            [0.1, 0.2, 0.0],   #win?
            [0.0, 1.3, 0.1] ]  #sad?  
            #toes %win #fans

def vect_mat_mul(vect,matrix):
    # assert(len(a) == len(b))
    output = 0
    for i in range(a):
        output += (a[i] * b[i])
    
    return output

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

     #toes          %win          #fans
# (8.5 * 0.1) + (0.65 * 0.1) + (1.2 * -0.3) = 0.555 = hurt prediction
# (8.5 * 0.1) + (0.65 * 0.2) + (1.2 * 0.0) = 0.98 = win prediction
# (8.5 * 0.0) + (0.65 * 1.3) + (1.2 * 0.1) = 0.965 = sad prediction