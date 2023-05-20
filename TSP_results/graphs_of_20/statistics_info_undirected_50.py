from statistics import mean
from math import inf

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [275.3515954017639, 359.3885636329651, 1287.6953632831573, 701.8100199699402, 500.1878879070282,
             193.15083742141724, 269.5129060745239, 251.78663182258606, 127.69906568527222, 897.4425868988037]
dfs_decisions = [(False, inf), (False, inf), (False, inf), (True, 167), (False, inf), (False, inf), (False, inf),
                 (True, 166), (False, inf), (False, inf)]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 486.4025458097458

dfs_cut_times = [265.18295979499817, 362.4096848964691, 1268.2393715381622, 663.4267365932465, 518.7195541858673,
                 192.35490822792053, 311.872599363327, 237.51821112632751, 123.97583246231079, 864.3746449947357]
dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (True, 167), (False, inf), (False, inf), (False, inf),
                     (True, 166), (False, inf), (False, inf)]

avg_time_dfs_cut = mean(dfs_cut_times)
print(avg_time_dfs_cut)  # 480.80745031833646

# comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
print(dfs_decisions == dfs_cut_decisions)
# from statistics import mean
# from math import inf
#
# brute_force_times = []
# brute_force_decisions = []
#
# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)
#
# dfs_times = [359.3885636329651, 1287.6953632831573, 701.8100199699402, 500.1878879070282, 193.15083742141724,
#              269.5129060745239, 251.78663182258606, 127.69906568527222, 897.4425868988037]
# dfs_decisions = [(False, inf), (False, inf), (True, 167), (False, inf), (False, inf), (False, inf), (True, 166),
#                  (False, inf), (False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [362.4096848964691, 1268.2393715381622, 663.4267365932465, 518.7195541858673, 192.35490822792053,
#                  311.872599363327, 237.51821112632751, 123.97583246231079, 864.3746449947357]
# dfs_cut_decisions = [(False, inf), (False, inf), (True, 167), (False, inf), (False, inf), (False, inf), (True, 166),
#                      (False, inf), (False, inf)]
#
# avg_time_dfs_cut = mean(dfs_cut_times)
# print(avg_time_dfs_cut)
#
# # comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
