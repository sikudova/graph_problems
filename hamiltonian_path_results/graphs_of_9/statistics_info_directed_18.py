from statistics import mean

brute_force_times = [75.16557598114014, 75.20046138763428, 72.3665201663971, 77.70178556442261, 79.74111771583557,
                     86.68173575401306, 30.461443662643433, 81.23400783538818, 80.48826360702515, 78.09626936912537]
brute_force_decisions = [False, False, False, False, False, False, True, False, False, False]

avg_time_bf = mean(brute_force_times)
print(avg_time_bf) # 73.71371810436248

dfs_times = [0.01599884033203125, 0.02034163475036621, 0.013367414474487305, 0.01699972152709961, 0.02205824851989746,
             0.026417255401611328, 0.015003442764282227, 0.014048099517822266, 0.013113260269165039,
             0.013998031616210938]
dfs_decisions = [False, False, False, False, False, False, True, False, False, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs) # 0.017134594917297363

# comparing decisions
print(brute_force_decisions == dfs_decisions) # True
