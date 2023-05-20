from statistics import mean

brute_force_times = [77.94542670249939, 17.061647653579712, 93.38018083572388, 80.32979607582092, 75.7983250617981,
                     15.327104568481445, 78.51605677604675, 83.28641605377197, 76.02771425247192, 81.69061541557312]
brute_force_decisions = [False, True, False, False, False, True, False, False, False, False]

avg_time_bf = mean(brute_force_times)
print(avg_time_bf)  # 67.93632833957672

dfs_times = [0.01999211311340332, 0.005185127258300781, 0.022353410720825195, 0.025179147720336914,
             0.018177032470703125, 0.0060384273529052734, 0.01899409294128418, 0.024985790252685547,
             0.014993906021118164, 0.03299260139465332]
dfs_decisions = [False, True, False, False, False, True, False, False, False, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.01888916492462158

# comparing decisions
print(brute_force_decisions == dfs_decisions)  # True
