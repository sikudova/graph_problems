from statistics import mean
from math import inf

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [67.98010849952698]
dfs_decisions = [(False, inf)]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)

dfs_cut_times = [68.83213543891907]
dfs_cut_decisions = [(False, inf)]

avg_time_dfs_cut = mean(dfs_cut_times)
print(avg_time_dfs_cut)

# comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
print(dfs_decisions == dfs_cut_decisions)
from statistics import mean
from math import inf

