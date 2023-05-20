from statistics import mean

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [0.15538525581359863, 1.4394690990447998, 0.10500335693359375, 0.020999431610107422, 0.010999917984008789,
             0.010999917984008789, 0.0039997100830078125, 0.005000114440917969, 0.199753999710083, 0.016150951385498047,
             0.003000020980834961, 0.0021195411682128906, 0.0211179256439209, 0.05686593055725098, 0.02017354965209961,
             0.002001523971557617, 0.2212831974029541, 0.0031282901763916016, 0.019000530242919922, 2.29880690574646,
             0.0031299591064453125, 0.004999876022338867, 0.0019998550415039062, 0.04047751426696777,
             0.005116462707519531, 0.004003047943115234, 0.006000041961669922, 0.019999980926513672,
             0.0019996166229248047, 0.0030002593994140625, 1.0083847045898438, 0.0071146488189697266,
             0.012000083923339844, 0.0279996395111084, 0.04263567924499512, 0.012999773025512695, 2.987678050994873,
             0.0039997100830078125, 0.00500035285949707, 0.009999752044677734, 0.12170171737670898,
             0.004114866256713867, 0.014885187149047852, 0.0029997825622558594, 0.006123542785644531,
             0.18518352508544922, 0.006002187728881836, 0.02199721336364746, 0.0060002803802490234,
             0.034002065658569336, 0.004000425338745117, 0.004120588302612305, 0.01800394058227539,
             0.002996206283569336, 0.03500103950500488, 0.003997325897216797, 0.009001731872558594,
             0.012136459350585938, 0.0040013790130615234, 0.0029981136322021484, 0.00913238525390625,
             0.020999670028686523, 0.006999969482421875, 0.0030028820037841797, 0.053694725036621094,
             0.023128271102905273, 0.002963542938232422, 0.002028226852416992, 0.009344339370727539,
             0.032999515533447266, 0.07999992370605469, 0.011098384857177734, 0.003965139389038086,
             0.0020363330841064453, 0.005997180938720703, 0.006002664566040039, 0.003094911575317383,
             0.0020017623901367188, 0.0030002593994140625, 0.01399850845336914, 0.12824296951293945,
             0.031128406524658203, 0.00412440299987793, 0.04300522804260254, 0.001993894577026367, 0.012357950210571289,
             0.00299835205078125, 0.002089977264404297, 0.006049156188964844, 0.009988784790039062, 0.06299805641174316,
             0.0019998550415039062, 0.0031442642211914062, 0.002997159957885742, 0.004002094268798828,
             0.0029981136322021484, 0.0020003318786621094, 0.07313823699951172, 0.010121583938598633,
             0.002000570297241211]
dfs_decisions = [True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                 True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                 True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                 True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                 True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                 True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.10025933742523194

# comparing decisions
print(brute_force_decisions == dfs_decisions)
