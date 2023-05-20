from statistics import mean

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [0.17303085327148438, 0.08400225639343262, 0.02099776268005371, 0.029999971389770508, 0.03800082206726074,
             0.05199909210205078, 0.021001338958740234, 0.0489654541015625, 0.045033931732177734, 0.10600638389587402,
             0.031992197036743164, 0.04996681213378906, 0.035002946853637695, 0.05099797248840332, 0.05699634552001953,
             0.13000011444091797, 0.04002737998962402, 0.04400777816772461, 0.03000640869140625, 0.059995412826538086,
             0.036966800689697266, 0.14403319358825684, 0.024999141693115234, 0.02599930763244629, 0.04799914360046387,
             0.09300398826599121, 0.12198209762573242, 0.057013511657714844, 0.0240018367767334, 0.04396653175354004,
             0.039032936096191406, 0.0830235481262207, 0.09797453880310059, 0.08600091934204102, 0.03401470184326172,
             0.04198503494262695, 0.0989995002746582, 0.02400040626525879, 0.07900261878967285, 0.04199719429016113,
             0.03599905967712402, 0.05000019073486328, 0.10602498054504395, 0.04097628593444824, 0.07300019264221191,
             0.03599810600280762, 0.02800130844116211, 0.021997928619384766, 0.04300546646118164, 0.03299546241760254,
             0.039997100830078125, 0.03501081466674805, 0.04299044609069824, 0.037998199462890625, 0.0850062370300293,
             0.051993370056152344, 0.031999826431274414, 0.05499982833862305, 0.10300683975219727, 0.04199671745300293,
             0.07796096801757812, 0.052013397216796875, 0.0649878978729248, 0.06200361251831055, 0.14400649070739746,
             0.03902482986450195, 0.027999401092529297, 0.12496328353881836, 0.03601241111755371, 0.05499124526977539,
             0.07603096961975098, 0.029002904891967773, 0.0790252685546875, 0.01997208595275879, 0.19496655464172363,
             0.09403300285339355, 0.03999972343444824, 0.03400301933288574, 0.029961824417114258, 0.04501080513000488,
             0.09799385070800781, 0.05199861526489258, 0.03099966049194336, 0.06300163269042969, 0.08299469947814941,
             0.057000160217285156, 0.09603643417358398, 0.03499865531921387, 0.034003496170043945, 0.12399673461914062,
             0.034967899322509766, 0.07403802871704102, 0.03299283981323242, 0.09300112724304199, 0.10199904441833496,
             0.06700277328491211, 0.023996829986572266, 0.029999494552612305, 0.07999968528747559, 0.054015398025512695]
dfs_decisions = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.05978033304214478

# comparing decisions
print(brute_force_decisions == dfs_decisions)
