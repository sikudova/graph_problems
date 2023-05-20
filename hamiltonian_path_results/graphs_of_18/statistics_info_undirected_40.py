from statistics import mean

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [271.92718529701233, 42.64096236228943, 240.7225637435913, 53.37266540527344, 31.993360996246338,
             25.675352573394775, 26.019840002059937, 17.6193687915802, 179.89300870895386, 98.54425430297852]
dfs_decisions = [False, False, False, False, False, False, False, False, False, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 98.84085621833802

# comparing decisions
print(brute_force_decisions == dfs_decisions)
