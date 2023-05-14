from statistics import mean

brute_force_times = [0.3791923522949219, 4.881776332855225, 28.283538818359375, 3.901174783706665, 3.323777914047241,
                     4.911128997802734, 29.168546199798584, 1.369478702545166, 28.37167763710022, 1.4249942302703857]
brute_force_decisions = [True, True, True, True, True, True, True, True, True, True]

avg_time_bf = mean(brute_force_times)
print(avg_time_bf)  # 10.601528596878051

dfs_times = [0.025002479553222656, 0.01300048828125, 0.06800103187561035, 0.002000093460083008, 0.005998373031616211,
             0.008002758026123047, 0.05400228500366211, 0.01000070571899414, 0.05900287628173828, 0.002999544143676758]
dfs_decisions = [True, True, True, True, True, True, True, True, True, True]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.024801063537597656

# comparing decisions
print(brute_force_decisions == dfs_decisions)  # True
