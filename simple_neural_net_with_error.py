weight = 0.1 
lr = 0.01 # Learning Rate / Increase in Weight
print("Initial Weight : ", weight)

# Define neural Network
def neural_network(input, weight):
    prediction = input * weight
    
    return prediction

#  PREDICT: Making A Prediction And Evaluating Error
number_of_toes = [8.5]
win_or_lose_binary = [1]  # (won!!!)
input = number_of_toes[0]
true = win_or_lose_binary[0]
# Initial Prediction
pred = neural_network(input,weight)
error = (pred - true) ** 2 # Raw Error
print("Raw Error : ", error)

#  COMPARE: Making A Prediction With a Higher Weight And Evaluating Error
p_up = neural_network(input,weight+lr) # Higher
e_up = (p_up - true) ** 2 # Error
print("Error when we take a higher Weight : ", e_up)

#  COMPARE: Making A Prediction With a Lower Weight And Evaluating Error
p_dn = neural_network(input,weight-lr) # Lower
e_dn = (p_dn - true) ** 2
print("Error when we take a Lower Weight : ", e_dn)

#  COMPARE + LEARN: Comparing our Errors and Setting our New Weight
# In our case, error is lesser when the higher weight is taken
# i.e. weight = 0.11
if(error > e_dn or error > e_up):
    if(e_dn < e_up):
        weight -= lr
        
    if(e_up < e_up):
        weight += lr

# In this case, our updated weight is same as initial weight because
# the error was very low after 1st iteration itself (0.004 i.e. 0.4%)
print("New Updated Weight : ", float(weight))