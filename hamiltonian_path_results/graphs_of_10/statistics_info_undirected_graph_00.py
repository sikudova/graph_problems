from statistics import mean

brute_force_times = [1039.0663964748383]
brute_force_decisions = [False]

avg_time_bf = mean(brute_force_times)
print(avg_time_bf)

dfs_times = [0.12846779823303223]
dfs_decisions = [False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)

# comparing decisions
print(brute_force_decisions == dfs_decisions)

