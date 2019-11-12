# Hierarchical Clustering
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Mall_Customers.csv')

X = dataset.iloc[:, 3:].values

import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = "ward"))

plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Distance")
plt.show()

#plt.savefig('dendrogram.png', dpi = 300)
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity="euclidean", linkage='ward')
hc_pred = hc.fit_predict(X)

# Visualising the clusters
plt.scatter(X[hc_pred == 0, 0], X[hc_pred == 0, 1], s = 100, color = 'red', label = 'Careful')
plt.scatter(X[hc_pred == 1, 0], X[hc_pred == 1, 1], s = 100, color = 'blue', label = 'Standard')
plt.scatter(X[hc_pred == 2, 0], X[hc_pred == 2, 1], s = 100, color = 'green', label = 'Target')
plt.scatter(X[hc_pred == 3, 0], X[hc_pred == 3, 1], s = 100, color = 'yellow', label = 'Careless')
plt.scatter(X[hc_pred == 4, 0], X[hc_pred == 4, 1], s = 100, color = 'gray', label = 'Sensible')
plt.title('Clusters of clients')
plt.xlabel('Annual income')
plt.ylabel('Spending score')
plt.legend()
plt.show()