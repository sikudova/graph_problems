from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

"""
    UNDIRECTED GRAPHS
"""

# brute force

exec_time_undirected_05_bf = [0.013539376258850098, 0.0028199481964111327]
avg_exec_time_undirected_05_bf = mean(exec_time_undirected_05_bf)
print(avg_exec_time_undirected_05_bf)

exec_time_undirected_06_bf = [0.0644137454032898, 0.017299468517303466]
avg_exec_time_undirected_06_bf = mean(exec_time_undirected_06_bf)
print(avg_exec_time_undirected_06_bf)

exec_time_undirected_07_bf = [0.5520655417442322, 0.1533409070968628]
avg_exec_time_undirected_07_bf = mean(exec_time_undirected_07_bf)
print(avg_exec_time_undirected_07_bf)

exec_time_undirected_08_bf = [5.057529385089874, 2.0234615993499756]
avg_exec_time_undirected_08_bf = mean(exec_time_undirected_08_bf)
print(avg_exec_time_undirected_08_bf)

exec_time_undirected_09_bf = [51.316584539413455, 10.601528596878051]
avg_exec_time_undirected_09_bf = mean(exec_time_undirected_09_bf)
print(avg_exec_time_undirected_09_bf)

exec_time_undirected_10_bf = [1039.0663964748383]
avg_exec_time_undirected_10_bf = mean(exec_time_undirected_10_bf)
print(avg_exec_time_undirected_10_bf)

# backtracking -- DFS

exec_time_undirected_05_dfs = [0.0032007503509521485, 0.0014554691314697266]
avg_exec_time_undirected_05_dfs = mean(exec_time_undirected_05_dfs)
print(avg_exec_time_undirected_05_dfs)

exec_time_undirected_06_dfs = [0.005310189723968506, 0.002684946060180664]
avg_exec_time_undirected_06_dfs = mean(exec_time_undirected_06_dfs)
print(avg_exec_time_undirected_06_dfs)

exec_time_undirected_07_dfs = [0.01276886224746704, 0.006217572689056396]
avg_exec_time_undirected_07_dfs = mean(exec_time_undirected_07_dfs)
print(avg_exec_time_undirected_07_dfs)

exec_time_undirected_08_dfs = [0.030452885627746583, 0.021186769008636475]
avg_exec_time_undirected_08_dfs = mean(exec_time_undirected_08_dfs)
print(avg_exec_time_undirected_08_dfs)

exec_time_undirected_09_dfs = [0.07081279754638672, 0.024801063537597656]
avg_exec_time_undirected_09_dfs = mean(exec_time_undirected_09_dfs)
print(avg_exec_time_undirected_09_dfs)

exec_time_undirected_10_dfs = [0.10025933742523194, 0.12572932958602906]
avg_exec_time_undirected_10_dfs = mean(exec_time_undirected_10_dfs)
print(avg_exec_time_undirected_10_dfs)

exec_time_undirected_11_dfs = [0.25685079336166383, 0.40251569271087645]
avg_exec_time_undirected_11_dfs = mean(exec_time_undirected_11_dfs)
print(avg_exec_time_undirected_11_dfs)

exec_time_undirected_12_dfs = [0.9974022197723389, 0.8376043796539306]
avg_exec_time_undirected_12_dfs = mean(exec_time_undirected_12_dfs)
print(avg_exec_time_undirected_12_dfs)

exec_time_undirected_15_dfs = [0.37655672550201413, 8.821977217197418]
avg_exec_time_undirected_15_dfs = mean(exec_time_undirected_15_dfs)
print(avg_exec_time_undirected_15_dfs)

exec_time_undirected_17_dfs = [7.695952711105346, 38.462383236885074]
avg_exec_time_undirected_17_dfs = mean(exec_time_undirected_17_dfs)
print(avg_exec_time_undirected_17_dfs)

"""
    DIRECTED GRAPHS
"""

exec_time_directed_05_bf = [0.020903899669647216, 0.008481600284576417]
avg_exec_time_directed_05_bf = mean(exec_time_directed_05_bf)
print(avg_exec_time_directed_05_bf)

exec_time_directed_06_bf = [0.12221641302108764, 0.06451254606246948]
avg_exec_time_directed_06_bf = mean(exec_time_directed_06_bf)
print(avg_exec_time_directed_06_bf)

exec_time_directed_07_bf = [0.975179271697998, 0.5257037568092346]
avg_exec_time_directed_07_bf = mean(exec_time_directed_07_bf)
print(avg_exec_time_directed_07_bf)

exec_time_directed_08_bf = [7.893085327148437, 6.058364832401276]
avg_exec_time_directed_08_bf = mean(exec_time_directed_08_bf)
print(avg_exec_time_directed_08_bf)

exec_time_directed_09_bf = [73.71371810436248, 67.93632833957672]
avg_exec_time_directed_09_bf = mean(exec_time_directed_09_bf)
print(avg_exec_time_directed_09_bf)

# Creating a numpy array
X = np.array([5, 6, 7, 8, 9])
Y = np.array([0.011436206102371217, 0.0671105432510376, 0.5515723693370819, 5.2581102859973905, 50.89203989505768])
plt.scatter(X, Y)
plt.show()
