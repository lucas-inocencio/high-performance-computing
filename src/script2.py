# import results_jacobi.csv and boxplot it

import csv
import matplotlib.pyplot as plt
import numpy as np

with open('results_jacobi.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    data = list(csv_reader)

    # Extract unique labels
    labels = np.unique([row[0] for row in data])
    
    # Extract times for each label
    times = []
    for label in labels:
        times.append(np.array([float(row[1]) for row in data if row[0] == label]))
    
    # Boxplot times small sample
    plt.boxplot(times, labels=labels)
    plt.ylabel('Tempo (Segundos)')
    plt.show()