from statistics import mean
from math import inf

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [40.190065145492554, 34.190202951431274, 5.818196535110474, 33.18212294578552, 44.35789179801941,
             88.7299211025238, 65.05082678794861, 69.16429281234741, 48.76715421676636, 17.946967840194702,
             3.943119525909424, 30.79296064376831, 93.83038020133972, 13.933507204055786, 22.592549324035645,
             17.884945392608643, 71.13890409469604, 11.180988073348999, 73.12055253982544, 106.64859366416931,
             30.747411966323853, 10.453652381896973, 22.355575799942017, 20.35542893409729, 26.249277114868164,
             72.44681882858276, 18.720587491989136, 14.642655849456787, 28.147958278656006, 22.59117579460144,
             11.569857597351074, 15.13177752494812, 17.121787309646606, 53.63919162750244, 57.67936396598816,
             25.950764894485474, 13.116904735565186, 4.999988794326782, 29.50474452972412, 20.781327486038208,
             56.020689249038696, 16.205856800079346, 61.31421494483948, 2.339021682739258, 10.519450902938843,
             14.446928024291992, 13.901035070419312, 7.292969703674316, 42.24583029747009, 6.878005743026733,
             66.09887838363647, 8.28598666191101, 8.71097993850708, 17.623899936676025, 32.24088263511658,
             96.97105526924133, 41.972874879837036, 10.792967319488525, 17.026946783065796, 55.91787672042847,
             6.24298882484436, 0.0, 69.46583199501038, 85.56682586669922, 25.0569429397583, 3.6279966831207275,
             61.50091314315796, 70.59587669372559, 55.15291738510132, 9.385978698730469, 19.202305555343628,
             24.328471422195435, 1.454993724822998, 28.46215534210205, 5.2365562915802, 51.105376958847046,
             4.006838321685791, 12.56563138961792, 24.968249559402466, 23.801211833953857, 39.902735471725464,
             50.95381045341492, 38.60513710975647, 94.32088971138, 29.242518663406372, 14.083801984786987,
             19.513678789138794, 1.6419415473937988, 15.291718006134033, 44.51226615905762, 35.99953842163086,
             78.7831072807312, 29.434682846069336, 43.93565106391907, 13.021917819976807, 4.020929336547852,
             20.782850742340088, 19.439834117889404, 31.622724294662476, 6.11298394203186]
dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 188),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 227), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 211),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf)]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 32.08427525043488

dfs_cut_times = [40.15061378479004, 42.11570620536804, 5.934502124786377, 33.16863417625427, 41.64064264297485,
                 91.42894101142883, 58.76688551902771, 69.8243818283081, 49.1558883190155, 17.736143589019775,
                 3.9440293312072754, 31.40598201751709, 92.33388113975525, 13.8990159034729, 23.435050010681152,
                 17.807976961135864, 75.09044194221497, 10.973997831344604, 76.34746479988098, 109.21659660339355,
                 29.28302526473999, 11.210627555847168, 22.66620659828186, 21.463472843170166, 28.00026297569275,
                 74.39804720878601, 18.601552963256836, 13.91470742225647, 29.05530858039856, 22.44062876701355,
                 11.532891750335693, 15.524890184402466, 17.720842361450195, 51.64236044883728, 56.955371141433716,
                 26.6197247505188, 13.619247198104858, 5.194941520690918, 29.433502674102783, 19.91081953048706,
                 54.445635080337524, 16.317925453186035, 64.15566563606262, 2.291973114013672, 10.333984136581421,
                 13.853896141052246, 14.398955345153809, 7.4977991580963135, 41.1457622051239, 6.878961086273193,
                 69.05784487724304, 8.531960725784302, 8.805998086929321, 17.163008451461792, 30.075918912887573,
                 93.46499967575073, 42.008841037750244, 10.876002788543701, 17.97395896911621, 55.86889839172363,
                 6.627981424331665, 0.0, 68.54841876029968, 86.98292326927185, 25.523911237716675, 3.7249886989593506,
                 62.39685392379761, 69.36691951751709, 56.61691904067993, 8.701988220214844, 19.3806369304657,
                 25.666011810302734, 1.544001579284668, 27.823038816452026, 6.638864755630493, 48.82648682594299,
                 3.982879161834717, 13.490537643432617, 24.84735345840454, 23.58925199508667, 41.83984971046448,
                 50.19485688209534, 38.881120920181274, 94.85842227935791, 28.59949827194214, 14.02376937866211,
                 19.73867654800415, 1.706003189086914, 15.365748405456543, 44.97144532203674, 36.83159351348877,
                 79.88001608848572, 29.51068925857544, 46.08656620979309, 13.109886407852173, 3.995968818664551,
                 20.882819890975952, 20.096789360046387, 30.900729179382324, 6.2179179191589355]
dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 188),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 227), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 211),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf)]

avg_time_dfs_cut = mean(dfs_cut_times)
print(avg_time_dfs_cut)  # 32.30685531377792

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
# dfs_times = [3.943119525909424, 30.79296064376831, 93.83038020133972, 13.933507204055786, 22.592549324035645,
#              17.884945392608643, 71.13890409469604, 11.180988073348999, 73.12055253982544, 106.64859366416931]
# dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
#                  (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [3.9440293312072754, 31.40598201751709, 92.33388113975525, 13.8990159034729, 23.435050010681152,
#                  17.807976961135864, 75.09044194221497, 10.973997831344604, 76.34746479988098, 109.21659660339355]
# dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
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
# dfs_times = [30.747411966323853, 10.453652381896973, 22.355575799942017, 20.35542893409729, 26.249277114868164,
#              72.44681882858276, 18.720587491989136, 14.642655849456787, 28.147958278656006, 22.59117579460144]
# dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
#                  (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [29.28302526473999, 11.210627555847168, 22.66620659828186, 21.463472843170166, 28.00026297569275,
#                  74.39804720878601, 18.601552963256836, 13.91470742225647, 29.05530858039856, 22.44062876701355]
# dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
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
# dfs_times = [11.569857597351074, 15.13177752494812, 17.121787309646606, 53.63919162750244, 57.67936396598816,
#              25.950764894485474, 13.116904735565186, 4.999988794326782, 29.50474452972412, 20.781327486038208]
# dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
#                  (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [11.532891750335693, 15.524890184402466, 17.720842361450195, 51.64236044883728, 56.955371141433716,
#                  26.6197247505188, 13.619247198104858, 5.194941520690918, 29.433502674102783, 19.91081953048706]
# dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
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
# dfs_times = [56.020689249038696, 16.205856800079346, 61.31421494483948, 2.339021682739258, 10.519450902938843,
#              14.446928024291992, 13.901035070419312, 7.292969703674316, 42.24583029747009, 6.878005743026733]
# dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
#                  (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [54.445635080337524, 16.317925453186035, 64.15566563606262, 2.291973114013672, 10.333984136581421,
#                  13.853896141052246, 14.398955345153809, 7.4977991580963135, 41.1457622051239, 6.878961086273193]
# dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
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
# dfs_times = [66.09887838363647, 8.28598666191101, 8.71097993850708, 17.623899936676025, 32.24088263511658,
#              96.97105526924133, 41.972874879837036, 10.792967319488525, 17.026946783065796, 55.91787672042847,
#              6.24298882484436, 0.0, 69.46583199501038, 85.56682586669922, 25.0569429397583, 3.6279966831207275,
#              61.50091314315796, 70.59587669372559, 55.15291738510132, 9.385978698730469]
# dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 188), (False, inf),
#                  (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
#                  (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [69.05784487724304, 8.531960725784302, 8.805998086929321, 17.163008451461792, 30.075918912887573,
#                  93.46499967575073, 42.008841037750244, 10.876002788543701, 17.97395896911621, 55.86889839172363,
#                  6.627981424331665, 0.0, 68.54841876029968, 86.98292326927185, 25.523911237716675, 3.7249886989593506,
#                  62.39685392379761, 69.36691951751709, 56.61691904067993, 8.701988220214844]
# dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 188), (False, inf),
#                      (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
#                      (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf)]
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
# dfs_times = [19.202305555343628, 24.328471422195435, 1.454993724822998, 28.46215534210205, 5.2365562915802,
#              51.105376958847046, 4.006838321685791, 12.56563138961792, 24.968249559402466, 23.801211833953857,
#              39.902735471725464, 50.95381045341492, 38.60513710975647, 94.32088971138, 29.242518663406372,
#              14.083801984786987, 19.513678789138794, 1.6419415473937988, 15.291718006134033, 44.51226615905762,
#              35.99953842163086, 78.7831072807312, 29.434682846069336, 43.93565106391907, 13.021917819976807,
#              4.020929336547852, 20.782850742340088, 19.439834117889404, 31.622724294662476, 6.11298394203186]
# dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 227), (False, inf),
#                  (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 211),
#                  (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
#                  (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
#                  (False, inf), (False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [19.3806369304657, 25.666011810302734, 1.544001579284668, 27.823038816452026, 6.638864755630493,
#                  48.82648682594299, 3.982879161834717, 13.490537643432617, 24.84735345840454, 23.58925199508667,
#                  41.83984971046448, 50.19485688209534, 38.881120920181274, 94.85842227935791, 28.59949827194214,
#                  14.02376937866211, 19.73867654800415, 1.706003189086914, 15.365748405456543, 44.97144532203674,
#                  36.83159351348877, 79.88001608848572, 29.51068925857544, 46.08656620979309, 13.109886407852173,
#                  3.995968818664551, 20.882819890975952, 20.096789360046387, 30.900729179382324, 6.2179179191589355]
# dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 227), (False, inf),
#                      (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 211),
#                      (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
#                      (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
#                      (False, inf), (False, inf)]
#
# avg_time_dfs_cut = mean(dfs_cut_times)
# print(avg_time_dfs_cut)
#
# # comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
