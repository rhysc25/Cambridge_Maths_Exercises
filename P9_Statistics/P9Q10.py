import numpy as np
import matplotlib.pyplot as plt
import operator    
def get_proportion(n, op, results):
    return sum(op(i, n) for i in results)/len(results) 

# Edit the line below to change the number of experiments, and observe the effect on the results
num_experiments = 100000

# Initialize an empty list to store the results
results = []

# Main loop over experiments
for i in range(num_experiments):
    # Generate ten random numbers in the range 0 to 1, count how
    # many of them exceed 0.5 - this is equivalent to tossing a head
    num_heads = 0
    for j in range(10):
        if np.random.rand() > 0.5:
            num_heads += 1

    # Store how many heads there were in this experiment
    results.append(num_heads)

# Plot a historgram of the number of heads
n, bins, patches = plt.hist(results, 10, facecolor='green', alpha=0.7)
plt.xlabel('number of heads')
plt.ylabel('frequency');

print('Proportion with five heads: {}'.format(get_proportion(5, operator.eq, results)))
print('Proportion with seven heads: {}'.format(get_proportion(7, operator.eq, results)))
print('Proportion with more than seven heads: {}'.format(get_proportion(7, operator.gt, results)))