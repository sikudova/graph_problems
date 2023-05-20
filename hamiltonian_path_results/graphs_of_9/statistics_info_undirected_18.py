from statistics import mean

brute_force_times = [22.34045672416687, 9.631818294525146, 20.747003316879272, 86.91829800605774, 7.262838125228882,
                     1.0107076168060303, 118.12936735153198, 32.87578248977661, 103.46188950538635, 110.78768396377563]
brute_force_decisions = [True, True, True, True, True, True, False, True, False, False]

avg_time_bf = mean(brute_force_times)
print(avg_time_bf)  # 51.316584539413455

dfs_times = [0.018654346466064453, 0.023494243621826172, 0.020855426788330078, 0.09208321571350098, 0.00499415397644043,
             0.0020351409912109375, 0.3276348114013672, 0.030047893524169922, 0.0997467041015625, 0.08858203887939453]
dfs_decisions = [True, True, True, True, True, True, False, True, False, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.07081279754638672

# comparing decisions
print(brute_force_decisions == dfs_decisions)  # True
