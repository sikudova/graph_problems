from statistics import mean

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [0.7101202011108398, 0.8674135208129883, 0.5879330635070801, 0.5762393474578857, 0.32387423515319824,
             0.1835346221923828, 0.2761983871459961, 0.3990938663482666, 0.9938464164733887, 0.05199718475341797,
             0.5969915390014648, 1.1192808151245117, 0.22903203964233398, 0.5289924144744873, 0.2929971218109131,
             0.4619936943054199, 0.5850791931152344, 0.30196261405944824, 0.2438046932220459, 0.3540608882904053,
             0.34848618507385254, 0.22349262237548828, 0.10503172874450684, 0.7611992359161377, 0.6696333885192871,
             0.8819088935852051, 0.49790143966674805, 0.7513821125030518, 0.1779956817626953, 0.6336164474487305,
             0.4843106269836426, 0.24803519248962402, 0.15662074089050293, 0.015994787216186523, 0.6763412952423096,
             0.25655055046081543, 0.6518542766571045, 0.5323255062103271, 0.2694125175476074, 0.4359729290008545,
             0.4752655029296875, 0.27144503593444824, 0.1733095645904541, 0.21396088600158691, 0.0891561508178711,
             0.3461027145385742, 0.21206092834472656, 0.32439708709716797, 0.12114167213439941, 0.3244435787200928,
             0.6864981651306152, 0.48099255561828613, 0.07815194129943848, 0.4142887592315674, 0.5595054626464844,
             0.6448714733123779, 0.7878322601318359, 0.33418965339660645, 0.04512524604797363, 0.8373734951019287,
             0.6932845115661621, 0.17414045333862305, 0.4408299922943115, 0.32090115547180176, 0.4020087718963623,
             0.5513019561767578, 0.14529633522033691, 0.4494040012359619, 0.351459264755249, 0.23212385177612305,
             0.7536640167236328, 0.14818644523620605, 0.5576198101043701, 0.2730894088745117, 0.2071239948272705,
             0.14026188850402832, 0.6146261692047119, 0.6795268058776855, 0.060127973556518555, 0.46039319038391113,
             0.485858678817749, 0.41542983055114746, 0.06818652153015137, 0.8205256462097168, 0.5832180976867676,
             0.339752197265625, 0.2463366985321045, 0.09503293037414551, 0.16864848136901855, 0.14759039878845215,
             0.1298384666442871, 0.7061924934387207, 1.1155900955200195, 0.6803774833679199, 0.4499790668487549,
             0.5487298965454102, 0.4650917053222656, 0.09025239944458008, 0.5641493797302246, 0.873173713684082]
dfs_decisions = [False, False, False, False, False, False, True, False, False, False, True, False, False, False, False,
                 False, False, False, True, False, False, False, True, False, False, False, False, False, False, False,
                 False, False, False, True, False, False, False, False, False, False, False, False, True, False, True,
                 False, False, False, False, True, False, False, False, False, False, False, True, False, True, False,
                 False, False, True, False, True, False, False, True, False, False, False, True, False, False, False,
                 False, False, False, True, False, False, False, False, False, False, False, False, True, False, True,
                 False, False, False, False, False, False, True, False, False, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.4253194832801819

# comparing decisions
# print(brute_force_decisions == dfs_decisions)