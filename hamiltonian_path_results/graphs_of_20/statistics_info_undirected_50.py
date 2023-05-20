from statistics import mean

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [2184.9835793972015, 39.165761947631836, 116.89392709732056, 0.3439974784851074, 165.18524146080017,
             373.2747039794922, 1333.4319694042206, 0.14600801467895508, 5.474034070968628, 8518.391503095627]
dfs_decisions = [False, True, True, True, True, True, False, True, True, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 1273.7290725946427

# comparing decisions
print(brute_force_decisions == dfs_decisions)
# from statistics import mean
#
# brute_force_times = []
# brute_force_decisions = []
#
# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)
#
# dfs_times = [5.474034070968628, 8518.391503095627]
# dfs_decisions = [True, False]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# # comparing decisions
# print(brute_force_decisions == dfs_decisions)
