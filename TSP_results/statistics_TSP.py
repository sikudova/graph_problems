from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

"""
    UNDIRECTED GRAPHS
"""

# brute force
print("brute force")
exec_time_undirected_05_bf = [0.07852136611938476, 0.1520548129081726]
avg_exec_time_undirected_05_bf = mean(exec_time_undirected_05_bf)
print(avg_exec_time_undirected_05_bf)  # 0.11528808951377868

exec_time_undirected_06_bf = [0.48226351499557496, 0.62003671169281]
avg_exec_time_undirected_06_bf = mean(exec_time_undirected_06_bf)
print(avg_exec_time_undirected_06_bf)  # 0.5511501133441925

exec_time_undirected_07_bf = [2.6327684712409973, 3.4961525273323057]
avg_exec_time_undirected_07_bf = mean(exec_time_undirected_07_bf)
print(avg_exec_time_undirected_07_bf)  # 3.0644604992866515

exec_time_undirected_08_bf = [18.033946549892427, 21.992432119846345]
avg_exec_time_undirected_08_bf = mean(exec_time_undirected_08_bf)
print(avg_exec_time_undirected_08_bf)  # 20.013189334869388

exec_time_undirected_09_bf = [148.03565366268157]
avg_exec_time_undirected_09_bf = mean(exec_time_undirected_09_bf)
print(avg_exec_time_undirected_09_bf)  # 148.03565366268157

exec_time_undirected_10_bf = [1287.4022080898285]
avg_exec_time_undirected_10_bf = mean(exec_time_undirected_09_bf)
print(avg_exec_time_undirected_10_bf)  # 1287.4022080898285

# Creating a numpy array
X = np.array([5, 6, 7, 8, 9, 10])
Y = np.array([0.12, 0.55, 3.06, 20.01, 148.04, 1287.40])

x = np.linspace(1, 10, 1000)
plt.plot(x, gamma(x), label='Factorial')

plt.scatter(X, Y, color="deeppink")
plt.plot(X, Y, color="hotpink")

plt.xlim([0, 11])
plt.ylim([0, 1500])

plt.xlabel("number of nodes")
plt.ylabel("time [seconds]")
plt.title("TSP: brute force on undirected graphs")

for i in range(len(X)):
    plt.annotate(str(Y[i]), xy=(X[i], Y[i]))
plt.show()

# DFS
print("DFS")
exec_time_undirected_05_dfs = [0.008609497547149658, 0.02529419183731079]
avg_exec_time_undirected_05_dfs = mean(exec_time_undirected_05_dfs)
print(avg_exec_time_undirected_05_dfs)  # 0.016951844692230225

exec_time_undirected_06_dfs = [0.016703064441680907, 0.043826026916503905]
avg_exec_time_undirected_06_dfs = mean(exec_time_undirected_06_dfs)
print(avg_exec_time_undirected_06_dfs)  # 0.030264545679092404

exec_time_undirected_07_dfs = [0.026952521800994875, 0.0750515604019165]
avg_exec_time_undirected_07_dfs = mean(exec_time_undirected_07_dfs)
print(avg_exec_time_undirected_07_dfs)  # 0.05100204110145569

exec_time_undirected_08_dfs = [0.03930241107940674, 0.1028417706489563]
avg_exec_time_undirected_08_dfs = mean(exec_time_undirected_08_dfs)
print(avg_exec_time_undirected_08_dfs)  # 0.07107209086418152

exec_time_undirected_09_dfs = [0.06608085870742798, 0.11956105470657348]
avg_exec_time_undirected_09_dfs = mean(exec_time_undirected_09_dfs)
print(avg_exec_time_undirected_09_dfs)  # 0.09282095670700073

exec_time_undirected_10_dfs = [0.1012084698677063, 1.2132082772254944]
avg_exec_time_undirected_10_dfs = mean(exec_time_undirected_10_dfs)
print(avg_exec_time_undirected_10_dfs)  # 0.6572083735466003

exec_time_undirected_11_dfs = [0.13373067378997802, 1.5396301078796386]
avg_exec_time_undirected_11_dfs = mean(exec_time_undirected_11_dfs)
print(avg_exec_time_undirected_11_dfs)  # 0.8366803908348083

exec_time_undirected_12_dfs = [0.12815810441970826, 1.9143721747398377, 16.206397533416748]
avg_exec_time_undirected_12_dfs = mean(exec_time_undirected_12_dfs)
print(avg_exec_time_undirected_12_dfs)  # 6.082975937525432

exec_time_undirected_15_dfs = [0.0733103632926941, 1.7953595399856568, 27.580731568336486]
avg_exec_time_undirected_15_dfs = mean(exec_time_undirected_15_dfs)
print(avg_exec_time_undirected_15_dfs)  # 9.816467157204945

exec_time_undirected_17_dfs = [0.07055299997329711, 1.709490385055542, 32.13969754934311]
avg_exec_time_undirected_17_dfs = mean(exec_time_undirected_17_dfs)
print(avg_exec_time_undirected_17_dfs)  # 11.306580311457317

exec_time_undirected_18_dfs = [0.049459924697875975, 1.4490670132637025, 41.36947132587433]
avg_exec_time_undirected_18_dfs = mean(exec_time_undirected_18_dfs)
print(avg_exec_time_undirected_18_dfs)  # 14.28933275461197

exec_time_undirected_20_dfs = [0.9772789335250854, 32.08427525043488, 486.4025458097458]
avg_exec_time_undirected_20_dfs = mean(exec_time_undirected_20_dfs)
print(avg_exec_time_undirected_20_dfs)  # 173.15469999790193

exec_time_undirected_25_dfs = [0.34378833055496216, 13.664074635505676]
avg_exec_time_undirected_25_dfs = mean(exec_time_undirected_25_dfs)
print(avg_exec_time_undirected_25_dfs)  # 173.15469999790193

# Creating a numpy array
X = np.array([5, 6, 7, 8, 9, 10, 11, 12, 15, 17, 18, 20])
Y = np.array([0.017, 0.03, 0.05, 0.07, 0.09, 0.66, 0.84, 6.08, 9.82, 11.31, 14.29, 173.15])

x = np.linspace(1, 10, 1000)
plt.plot(x, gamma(x), label='Factorial')

plt.scatter(X, Y, color="deeppink")
plt.plot(X, Y, color="hotpink")

plt.xlim([0, 30])
plt.ylim([0, 200])

plt.xlabel("number of nodes")
plt.ylabel("time [seconds]")
plt.title("TSP: DFS on undirected graphs")

for i in range(len(X)):
    plt.annotate(str(Y[i]), xy=(X[i], Y[i]))
plt.show()

# DFS with cut
print("DFS with cut")
exec_time_undirected_05_dfs_cut = [0.008107140064239501, 0.021480400562286377]
avg_exec_time_undirected_05_dfs_cut = mean(exec_time_undirected_05_dfs_cut)
print(avg_exec_time_undirected_05_dfs_cut)  # 0.01479377031326294

exec_time_undirected_06_dfs_cut = [0.016131067276000978, 0.0393637228012085]
avg_exec_time_undirected_06_dfs_cut = mean(exec_time_undirected_06_dfs_cut)
print(avg_exec_time_undirected_06_dfs_cut)  # 0.02774739503860474

exec_time_undirected_07_dfs_cut = [0.02672301769256592, 0.06958707809448242]
avg_exec_time_undirected_07_dfs_cut = mean(exec_time_undirected_07_dfs_cut)
print(avg_exec_time_undirected_07_dfs_cut)  # 0.04815504789352417

exec_time_undirected_08_dfs_cut = [0.038769650459289554, 0.09727057695388794]
avg_exec_time_undirected_08_dfs_cut = mean(exec_time_undirected_08_dfs_cut)
print(avg_exec_time_undirected_08_dfs_cut)  # 0.06802011370658875

exec_time_undirected_09_dfs_cut = [0.06475890159606934, 0.11514847755432128]
avg_exec_time_undirected_09_dfs_cut = mean(exec_time_undirected_09_dfs_cut)
print(avg_exec_time_undirected_09_dfs_cut)  # 0.08995368957519531

exec_time_undirected_10_dfs_cut = [0.10038108348846436, 1.0079834127426148]
avg_exec_time_undirected_10_dfs_cut = mean(exec_time_undirected_10_dfs_cut)
print(avg_exec_time_undirected_10_dfs_cut)  # 0.5541822481155396

exec_time_undirected_11_dfs_cut = [0.13336875915527344, 1.3438779020309448]
avg_exec_time_undirected_11_dfs_cut = mean(exec_time_undirected_11_dfs_cut)
print(avg_exec_time_undirected_11_dfs_cut)  # 0.7386233305931091

exec_time_undirected_12_dfs_cut = [0.12836777448654174, 1.801866602897644, 10.525104520320893]
avg_exec_time_undirected_12_dfs_cut = mean(exec_time_undirected_12_dfs_cut)
print(avg_exec_time_undirected_12_dfs_cut)  # 4.15177963256836

exec_time_undirected_15_dfs_cut = [0.07251903295516968, 1.7935310101509094, 24.924170200824737]
avg_exec_time_undirected_15_dfs_cut = mean(exec_time_undirected_15_dfs_cut)
print(avg_exec_time_undirected_15_dfs_cut)  # 8.930073414643605

exec_time_undirected_17_dfs_cut = [0.06846372604370117, 1.7305724263191222, 31.816961703300475]
avg_exec_time_undirected_17_dfs_cut = mean(exec_time_undirected_17_dfs_cut)
print(avg_exec_time_undirected_17_dfs_cut)  # 11.205332618554433

exec_time_undirected_18_dfs_cut = [0.04640944480895996, 1.447214550971985, 40.8786965072155]
avg_exec_time_undirected_18_dfs_cut = mean(exec_time_undirected_18_dfs_cut)
print(avg_exec_time_undirected_18_dfs_cut)  # 14.12410683433215

exec_time_undirected_20_dfs_cut = [0.9797120022773743, 32.30685531377792, 480.80745031833646]
avg_exec_time_undirected_20_dfs_cut = mean(exec_time_undirected_20_dfs_cut)
print(avg_exec_time_undirected_20_dfs_cut)  # 171.36467254479726

exec_time_undirected_25_dfs_cut = [0.34423747539520266, 13.788212883472443]
avg_exec_time_undirected_25_dfs_cut = mean(exec_time_undirected_25_dfs_cut)
print(avg_exec_time_undirected_25_dfs_cut)  #

# Creating a numpy array
X = np.array([5, 6, 7, 8, 9, 10, 11, 12, 15, 17, 18, 20])
Y = np.array([0.015, 0.03, 0.05, 0.07, 0.09, 0.55, 0.74, 4.15, 8.93, 11.21, 14.12, 171.36])

x = np.linspace(1, 10, 1000)
plt.plot(x, gamma(x), label='Factorial')

plt.scatter(X, Y, color="deeppink")
plt.plot(X, Y, color="hotpink")

plt.xlim([0, 30])
plt.ylim([0, 200])

plt.xlabel("number of nodes")
plt.ylabel("time [seconds]")
plt.title("TSP: DFS with cut on undirected graphs")

for i in range(len(X)):
    plt.annotate(str(Y[i]), xy=(X[i], Y[i]))
plt.show()
