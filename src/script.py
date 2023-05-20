# import result_c.csv and results_f.csv and plot a graph with x axis as the first collumm, y axis as the second collumn and the third collumn of each file as the label in the same graph.

import csv
import matplotlib.pyplot as plt
import numpy as np

def compute_mean(x, y):
    unique_x = np.unique(x)
    mean_y = []
    for val in unique_x:
        indices = np.where(x == val)
        mean_y.append(np.mean(y[indices]))
    return unique_x, mean_y

def plot_graph(x, y1, y2, label):
    plt.plot(x, y1, label=f'{label} - linha-coluna')
    plt.plot(x, y2, label=f'{label} - coluna-linha')

# Import data from results_c.csv
with open('results_c.csv', 'r') as file_c:
    csv_reader_c = csv.reader(file_c)
    next(csv_reader_c)  # Skip header row
    data_c = list(csv_reader_c)

# Extract columns from data_c
x_c = np.array([float(row[0]) for row in data_c])
y1_c = np.array([float(row[1]) for row in data_c])
y2_c = np.array([float(row[2]) for row in data_c])

# Compute mean values for x_c
x_mean_c, y1_mean_c = compute_mean(x_c, y1_c)
_, y2_mean_c = compute_mean(x_c, y2_c)

# Import data from results_f.csv
with open('results_f.csv', 'r') as file_f:
    csv_reader_f = csv.reader(file_f)
    next(csv_reader_f)  # Skip header row
    data_f = list(csv_reader_f)

# Extract columns from data_f
x_f = np.array([float(row[0]) for row in data_f])
y1_f = np.array([float(row[1]) for row in data_f])
y2_f = np.array([float(row[2]) for row in data_f])

# Compute mean values for x_f
x_mean_f, y1_mean_f = compute_mean(x_f, y1_f)
_, y2_mean_f = compute_mean(x_f, y2_f)

# Plot the graph
plt.figure()
plot_graph(x_mean_c, y1_mean_c, y2_mean_c, 'C')
plot_graph(x_mean_f, y1_mean_f, y2_mean_f, 'Fortran')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph with Mean Values for Each Unique x_c')
plt.legend()
plt.show()