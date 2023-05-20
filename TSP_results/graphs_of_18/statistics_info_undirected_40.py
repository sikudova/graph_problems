from statistics import mean
from math import inf

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [42.244977712631226, 16.91797375679016, 99.98986005783081, 12.295022964477539, 10.031023979187012,
             16.819670915603638, 9.878023386001587, 3.605991840362549, 54.03115177154541, 65.40809106826782,
             10.573098421096802, 27.619799852371216, 44.30800437927246, 23.022202491760254, 14.549646854400635,
             59.75904440879822, 14.084782600402832, 53.13405394554138, 139.74265837669373, 34.91502404212952,
             119.52116107940674, 60.687949419021606, 39.852150440216064, 68.31826043128967, 54.122865200042725,
             26.546748399734497, 9.183867931365967, 26.664366722106934, 13.234009981155396, 56.868414640426636,
             34.75892782211304, 74.35082650184631, 45.324501514434814, 85.94445013999939, 17.8056800365448,
             73.93666410446167, 22.733577728271484, 3.983534812927246, 10.92505145072937, 7.747478008270264,
             38.438528299331665, 10.381954193115234, 44.22681999206543, 60.2682785987854, 32.35005331039429,
             58.272380113601685, 36.80429935455322, 107.84431886672974, 13.188825130462646, 61.257519245147705]
dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 190),
                 (False, inf), (False, inf), (True, 138), (False, inf), (False, inf), (False, inf), (True, 169),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 219),
                 (False, inf), (False, inf), (True, 127), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (True, 214), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (True, 197), (False, inf), (False, inf), (False, inf),
                 (True, 144)]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 41.36947132587433

dfs_cut_times = [42.12791132926941, 16.95297622680664, 101.52488446235657, 17.582171201705933, 12.718031644821167,
                 14.671964406967163, 9.60499382019043, 3.594965934753418, 50.157963037490845, 62.211997985839844,
                 119.83383917808533, 59.45885467529297, 41.94727444648743, 55.540324211120605, 52.96825075149536,
                 26.502116918563843, 9.411026000976562, 27.12051510810852, 13.859038829803467, 58.18450379371643,
                 34.68761682510376, 74.45794081687927, 45.1694974899292, 86.04399180412292, 18.264026403427124,
                 74.4700140953064, 23.451329946517944, 4.05202317237854, 11.26486587524414, 8.04407811164856,
                 35.555845975875854, 10.505448579788208, 43.874021768569946, 61.88691830635071, 32.61237120628357,
                 57.60034418106079, 37.660871744155884, 108.66684937477112, 13.46595287322998, 57.440247774124146]
dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 190),
                     (False, inf), (False, inf), (True, 138), (False, inf), (False, inf), (False, inf), (True, 169),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 219),
                     (False, inf), (False, inf), (True, 127), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (True, 214), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (True, 197), (False, inf), (False, inf), (False, inf),
                     (True, 144)]

avg_time_dfs_cut = mean(dfs_cut_times)
print(avg_time_dfs_cut)  # 40.8786965072155

# comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
print(dfs_decisions == dfs_cut_decisions)  # true

# from statistics import mean
# from math import inf
#
# brute_force_times = []
# brute_force_decisions = []
#
# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)
#
# dfs_times = [10.573098421096802, 27.619799852371216, 44.30800437927246, 23.022202491760254, 14.549646854400635,
#              59.75904440879822, 14.084782600402832, 53.13405394554138, 139.74265837669373, 34.91502404212952]
# dfs_decisions = [(False, inf), (False, inf), (False, inf), (True, 169), (False, inf), (False, inf), (False, inf),
#                  (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [8.661094188690186, 25.39195942878723, 43.95293354988098, 22.808827877044678, 14.989664077758789,
#                  58.85148620605469, 13.830373048782349, 48.30841279029846, 142.00911378860474, 35.025598764419556]
# dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (True, 169), (False, inf), (False, inf), (False, inf),
#                      (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs_cut = mean(dfs_cut_times)
# print(avg_time_dfs_cut)
#
# # comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
# from statistics import mean
# from math import inf
#
# brute_force_times = []
# brute_force_decisions = []
#
# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)
#
# dfs_times = [119.52116107940674, 60.687949419021606, 39.852150440216064, 68.31826043128967, 54.122865200042725,
#              26.546748399734497, 9.183867931365967, 26.664366722106934, 13.234009981155396, 56.868414640426636]
# dfs_decisions = [(True, 219), (False, inf), (False, inf), (True, 127), (False, inf), (False, inf), (False, inf),
#                  (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [119.83383917808533, 59.45885467529297, 41.94727444648743, 55.540324211120605, 52.96825075149536,
#                  26.502116918563843, 9.411026000976562, 27.12051510810852, 13.859038829803467, 58.18450379371643]
# dfs_cut_decisions = [(True, 219), (False, inf), (False, inf), (True, 127), (False, inf), (False, inf), (False, inf),
#                      (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs_cut = mean(dfs_cut_times)
# print(avg_time_dfs_cut)
#
# # comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
# from statistics import mean
# from math import inf
#
# brute_force_times = []
# brute_force_decisions = []
#
# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)
#
# dfs_times = [34.75892782211304, 74.35082650184631, 45.324501514434814, 85.94445013999939, 17.8056800365448,
#              73.93666410446167, 22.733577728271484, 3.983534812927246, 10.92505145072937, 7.747478008270264]
# dfs_decisions = [(False, inf), (False, inf), (True, 214), (False, inf), (False, inf), (False, inf), (False, inf),
#                  (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [34.68761682510376, 74.45794081687927, 45.1694974899292, 86.04399180412292, 18.264026403427124,
#                  74.4700140953064, 23.451329946517944, 4.05202317237854, 11.26486587524414, 8.04407811164856]
# dfs_cut_decisions = [(False, inf), (False, inf), (True, 214), (False, inf), (False, inf), (False, inf), (False, inf),
#                      (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs_cut = mean(dfs_cut_times)
# print(avg_time_dfs_cut)
#
# # comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
# from statistics import mean
# from math import inf
#
# brute_force_times = []
# brute_force_decisions = []
#
# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)
#
# dfs_times = [38.438528299331665, 10.381954193115234, 44.22681999206543, 60.2682785987854, 32.35005331039429,
#              58.272380113601685, 36.80429935455322, 107.84431886672974, 13.188825130462646, 61.257519245147705]
# dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 197), (False, inf),
#                  (False, inf), (False, inf), (True, 144)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [35.555845975875854, 10.505448579788208, 43.874021768569946, 61.88691830635071, 32.61237120628357,
#                  57.60034418106079, 37.660871744155884, 108.66684937477112, 13.46595287322998, 57.440247774124146]
# dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 197), (False, inf),
#                      (False, inf), (False, inf), (True, 144)]
#
# avg_time_dfs_cut = mean(dfs_cut_times)
# print(avg_time_dfs_cut)
#
# # comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
