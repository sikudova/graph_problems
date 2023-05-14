from statistics import mean

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [0.14526939392089844, 0.18448948860168457, 0.025963544845581055, 0.07361698150634766, 0.2761979103088379,
             0.04500102996826172, 0.03696608543395996, 0.03703188896179199, 0.029992341995239258, 0.24412870407104492,
             0.048165321350097656, 0.0952444076538086, 0.28498363494873047, 0.10184168815612793, 0.06803512573242188,
             0.21706271171569824, 0.02992081642150879, 0.10403132438659668, 0.1389636993408203, 0.05041766166687012,
             0.21644854545593262, 0.07400226593017578, 0.023008108139038086, 0.026989459991455078, 0.304002046585083,
             0.09899377822875977, 0.08100533485412598, 0.12810301780700684, 0.2969987392425537, 0.3225376605987549,
             0.06500363349914551, 0.04499244689941406, 0.0930027961730957, 0.045030832290649414, 0.12600064277648926,
             0.07596397399902344, 0.1410815715789795, 0.17099523544311523, 0.10603475570678711, 0.13196635246276855,
             0.04099726676940918, 0.039101362228393555, 0.09653472900390625, 0.07799911499023438, 0.03700113296508789,
             0.05889320373535156, 0.21804332733154297, 0.1627063751220703, 0.03200554847717285, 0.1831045150756836,
             0.046035051345825195, 0.09796357154846191, 0.04103732109069824, 0.08499836921691895, 0.10495924949645996,
             0.029000043869018555, 0.14500045776367188, 0.03603672981262207, 0.05899834632873535, 0.1960005760192871,
             0.056995391845703125, 0.17496418952941895, 0.0740354061126709, 0.0679633617401123, 0.12099790573120117,
             0.12401795387268066, 0.04798316955566406, 0.1190035343170166, 0.04202914237976074, 0.05099987983703613,
             0.06799960136413574, 0.1360149383544922, 0.04812216758728027, 0.0509648323059082, 0.07427978515625,
             0.11699676513671875, 0.03296613693237305, 0.06599974632263184, 0.1051325798034668, 0.0943906307220459,
             0.06203579902648926, 0.02200150489807129, 0.1279621124267578, 0.1159980297088623, 0.05800127983093262,
             0.026999235153198242, 0.06800246238708496, 0.08603286743164062, 0.04399681091308594, 0.040001869201660156,
             0.08899903297424316, 0.03499937057495117, 0.041998863220214844, 0.024967193603515625, 0.01900005340576172,
             0.05512690544128418, 0.04902338981628418, 0.11200332641601562, 0.09323835372924805, 0.09119653701782227]
dfs_decisions = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.09529343366622925

# comparing decisions
# print(brute_force_decisions == dfs_decisions)