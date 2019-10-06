import numpy as np 

input = 2
goal_pred = 0.8
weight = 0.5 

alpha = 0.1

for i in range(5):
    
    # Calculate pred
    pred = input * weight
    # calculate error
    error = (pred - goal_pred) ** 2 

    # get derivative
    delta_weight = input  *  (pred - goal_pred)
    # update weight
    weight = weight -(alpha * delta_weight)

    print(f"Error: {error}, pred: {pred}")
