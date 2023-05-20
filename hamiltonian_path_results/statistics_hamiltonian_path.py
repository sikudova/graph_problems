from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

"""
    UNDIRECTED GRAPHS
"""

# brute force

exec_time_undirected_05_bf = [0.013539376258850098, 0.0028199481964111327]
avg_exec_time_undirected_05_bf = mean(exec_time_undirected_05_bf)
print(avg_exec_time_undirected_05_bf)  # 0.008179662227630615

exec_time_undirected_06_bf = [0.0644137454032898, 0.017299468517303466]
avg_exec_time_undirected_06_bf = mean(exec_time_undirected_06_bf)
print(avg_exec_time_undirected_06_bf)  # 0.04085660696029663

exec_time_undirected_07_bf = [0.5520655417442322, 0.1533409070968628]
avg_exec_time_undirected_07_bf = mean(exec_time_undirected_07_bf)
print(avg_exec_time_undirected_07_bf)  # 0.35270322442054747

exec_time_undirected_08_bf = [5.057529385089874, 2.0234615993499756]
avg_exec_time_undirected_08_bf = mean(exec_time_undirected_08_bf)
print(avg_exec_time_undirected_08_bf)  # 3.540495492219925

exec_time_undirected_09_bf = [51.316584539413455, 10.601528596878051]
avg_exec_time_undirected_09_bf = mean(exec_time_undirected_09_bf)
print(avg_exec_time_undirected_09_bf)  # 30.959056568145755

exec_time_undirected_10_bf = [1039.0663964748383]
avg_exec_time_undirected_10_bf = mean(exec_time_undirected_10_bf)
print(avg_exec_time_undirected_10_bf)  # 1039.0663964748383

# Creating a numpy array
X = np.array([5, 6, 7, 8, 9, 10])
Y = np.array([0.008179662227630615, 0.04085660696029663, 0.35270322442054747, 3.540495492219925, 30.959056568145755,
              1039.0663964748383])
plt.scatter(X, Y)
plt.show()

# backtracking -- DFS

exec_time_undirected_05_dfs = [0.0032007503509521485, 0.0014554691314697266]
avg_exec_time_undirected_05_dfs = mean(exec_time_undirected_05_dfs)
print(avg_exec_time_undirected_05_dfs)  # 0.0023281097412109373

exec_time_undirected_06_dfs = [0.005310189723968506, 0.002684946060180664]
avg_exec_time_undirected_06_dfs = mean(exec_time_undirected_06_dfs)
print(avg_exec_time_undirected_06_dfs)  # 0.003997567892074585

exec_time_undirected_07_dfs = [0.01276886224746704, 0.006217572689056396]
avg_exec_time_undirected_07_dfs = mean(exec_time_undirected_07_dfs)
print(avg_exec_time_undirected_07_dfs)  # 0.00949321746826172

exec_time_undirected_08_dfs = [0.030452885627746583, 0.021186769008636475]
avg_exec_time_undirected_08_dfs = mean(exec_time_undirected_08_dfs)
print(avg_exec_time_undirected_08_dfs)  # 0.02581982731819153

exec_time_undirected_09_dfs = [0.07081279754638672, 0.024801063537597656]
avg_exec_time_undirected_09_dfs = mean(exec_time_undirected_09_dfs)
print(avg_exec_time_undirected_09_dfs)  # 0.04780693054199219

exec_time_undirected_10_dfs = [0.10025933742523194, 0.12572932958602906]
avg_exec_time_undirected_10_dfs = mean(exec_time_undirected_10_dfs)
print(avg_exec_time_undirected_10_dfs)  # 0.1129943335056305

exec_time_undirected_11_dfs = [0.25685079336166383, 0.40251569271087645]
avg_exec_time_undirected_11_dfs = mean(exec_time_undirected_11_dfs)
print(avg_exec_time_undirected_11_dfs)  # 0.32968324303627017

exec_time_undirected_12_dfs = [0.9974022197723389, 0.8376043796539306]
avg_exec_time_undirected_12_dfs = mean(exec_time_undirected_12_dfs)
print(avg_exec_time_undirected_12_dfs)  # 0.9175032997131347

exec_time_undirected_15_dfs = [0.37655672550201413, 8.821977217197418]
avg_exec_time_undirected_15_dfs = mean(exec_time_undirected_15_dfs)
print(avg_exec_time_undirected_15_dfs)  # 4.599266971349716

exec_time_undirected_17_dfs = [0.3303201055526733, 7.695952711105346, 38.462383236885074]
avg_exec_time_undirected_17_dfs = mean(exec_time_undirected_17_dfs)
print(avg_exec_time_undirected_17_dfs)  # 15.496218684514364

exec_time_undirected_18_dfs = [0.25618696689605713, 6.159137880802154, 98.84085621833802]
avg_exec_time_undirected_18_dfs = mean(exec_time_undirected_18_dfs)
print(avg_exec_time_undirected_18_dfs)  # 35.08539368867874

exec_time_undirected_20_dfs = [2184.9835793972015]
avg_exec_time_undirected_20_dfs = mean(exec_time_undirected_18_dfs)
print(avg_exec_time_undirected_20_dfs)  # 2184.9835793972015

"""
    DIRECTED GRAPHS
"""

exec_time_directed_05_bf = [0.020903899669647216, 0.008481600284576417]
avg_exec_time_directed_05_bf = mean(exec_time_directed_05_bf)
print(avg_exec_time_directed_05_bf)  # 0.014692749977111817

exec_time_directed_06_bf = [0.12221641302108764, 0.06451254606246948]
avg_exec_time_directed_06_bf = mean(exec_time_directed_06_bf)
print(avg_exec_time_directed_06_bf)  # 0.09336447954177857

exec_time_directed_07_bf = [0.975179271697998, 0.5257037568092346]
avg_exec_time_directed_07_bf = mean(exec_time_directed_07_bf)
print(avg_exec_time_directed_07_bf)  # 0.7504415142536163

exec_time_directed_08_bf = [7.893085327148437, 6.058364832401276]
avg_exec_time_directed_08_bf = mean(exec_time_directed_08_bf)
print(avg_exec_time_directed_08_bf)  # 6.975725079774857

exec_time_directed_09_bf = [73.71371810436248, 67.93632833957672]
avg_exec_time_directed_09_bf = mean(exec_time_directed_09_bf)
print(avg_exec_time_directed_09_bf)  # 70.8250232219696

# exec_time_directed_10_bf = []
# avg_exec_time_directed_10_bf = mean(exec_time_directed_10_bf)
# print(avg_exec_time_directed_10_bf)

# backtracking -- DFS

exec_time_directed_05_dfs = [0.003203885555267334, 0.002072429656982422]
avg_exec_time_directed_05_dfs = mean(exec_time_directed_05_dfs)
print(avg_exec_time_directed_05_dfs)  # 0.002638157606124878

exec_time_directed_06_dfs = [0.004874305725097656, 0.004375927448272705]
avg_exec_time_directed_06_dfs = mean(exec_time_directed_06_dfs)
print(avg_exec_time_directed_06_dfs)  # 0.004625116586685181

exec_time_directed_07_dfs = [0.007960774898529054, 0.007995171546936035]
avg_exec_time_directed_07_dfs = mean(exec_time_directed_07_dfs)
print(avg_exec_time_directed_07_dfs)  # 0.007977973222732544

exec_time_directed_08_dfs = [0.012252397537231445, 0.014757654666900634]
avg_exec_time_directed_08_dfs = mean(exec_time_directed_08_dfs)
print(avg_exec_time_directed_08_dfs)  # 0.01350502610206604

exec_time_directed_09_dfs = [0.017134594917297363, 0.01888916492462158]
avg_exec_time_directed_09_dfs = mean(exec_time_directed_09_dfs)
print(avg_exec_time_directed_09_dfs)  # 0.01801187992095947

exec_time_directed_10_dfs = [0.026027748584747313, 0.057115442752838134]
avg_exec_time_directed_10_dfs = mean(exec_time_directed_10_dfs)
print(avg_exec_time_directed_10_dfs)  # 0.041571595668792725

exec_time_directed_11_dfs = [0.026520299911499023, 0.08819966554641724]
avg_exec_time_directed_11_dfs = mean(exec_time_directed_11_dfs)
print(avg_exec_time_directed_11_dfs)  # 0.057359982728958134

exec_time_directed_12_dfs = [0.028445162773132325, 0.1087782096862793, 0.2098950505256653]
avg_exec_time_directed_12_dfs = mean(exec_time_directed_12_dfs)
print(avg_exec_time_directed_12_dfs)  # 0.11570614099502563

exec_time_directed_15_dfs = [0.02385194778442383, 0.11079739809036254, 0.4253194832801819]
avg_exec_time_directed_15_dfs = mean(exec_time_directed_15_dfs)
print(avg_exec_time_directed_15_dfs)  # 0.1866562763849894

exec_time_directed_17_dfs = [0.026592068672180176, 0.09529343366622925, 0.597760865688324]
avg_exec_time_directed_17_dfs = mean(exec_time_directed_17_dfs)
print(avg_exec_time_directed_17_dfs)  # 0.2398821226755778

exec_time_directed_18_dfs = [0.02353695869445801, 0.0754707932472229, 0.43618140459060667]
avg_exec_time_directed_18_dfs = mean(exec_time_directed_18_dfs)
print(avg_exec_time_directed_18_dfs)  #

exec_time_directed_20_dfs = [0.05978033304214478, 0.3333092975616455, 2.1275508570671082]
avg_exec_time_directed_20_dfs = mean(exec_time_directed_20_dfs)
print(avg_exec_time_directed_20_dfs)  #
