from statistics import mean

brute_force_times = [0.10509467124938965, 0.002000570297241211, 0.030055761337280273, 0.03898978233337402,
                     0.0010342597961425781, 0.0481109619140625, 0.0, 0.001005411148071289, 0.0020012855529785156,
                     0.004016876220703125, 0.008085966110229492, 0.0030014514923095703, 0.004040718078613281,
                     0.00804591178894043, 0.010041952133178711, 0.03709125518798828, 0.004002809524536133,
                     0.03978848457336426, 0.0030002593994140625, 0.0019998550415039062, 0.0039997100830078125,
                     0.002000093460083008, 0.003000020980834961, 0.009000062942504883, 0.028000354766845703,
                     0.002000093460083008, 0.017999887466430664, 0.031000137329101562, 0.0019998550415039062,
                     0.01000070571899414, 0.013000011444091797, 0.0030012130737304688, 0.003998994827270508,
                     0.0030007362365722656, 0.0009968280792236328, 0.03299999237060547, 0.0009999275207519531,
                     0.006999492645263672, 0.007013082504272461, 0.04304909706115723, 0.003014087677001953,
                     0.038025617599487305, 0.041971683502197266, 0.0019998550415039062, 0.015012502670288086,
                     0.003000020980834961, 0.0379633903503418, 0.043908119201660156, 0.03999781608581543,
                     0.0010318756103515625, 0.04015493392944336, 0.010955333709716797, 0.002681255340576172,
                     0.003996849060058594, 0.003998756408691406, 0.011974096298217773, 0.0019996166229248047,
                     0.04094815254211426, 0.0399470329284668, 0.0010001659393310547, 0.002962350845336914,
                     0.017967939376831055, 0.004999399185180664, 0.002001047134399414, 0.0019979476928710938,
                     0.00399470329284668, 0.012998819351196289, 0.00403285026550293, 0.0020003318786621094,
                     0.0009989738464355469, 0.0469510555267334, 0.012013435363769531, 0.041005611419677734,
                     0.002000093460083008, 0.001001119613647461, 0.0019996166229248047, 0.0070002079010009766,
                     0.0010001659393310547, 0.015000104904174805, 0.0069997310638427734, 0.0029997825622558594,
                     0.004000663757324219, 0.0019996166229248047, 0.0039997100830078125, 0.03399991989135742,
                     0.03300213813781738, 0.003998756408691406, 0.0009975433349609375, 0.002001523971557617,
                     0.019962549209594727, 0.006000041961669922, 0.003000020980834961, 0.0409998893737793,
                     0.0010006427764892578, 0.0009999275207519531, 0.01699972152709961, 0.011999845504760742,
                     0.0010001659393310547, 0.0009999275207519531, 0.016000032424926758]
brute_force_decisions = [True, True, True, False, True, False, True, True, True, True, True, True, True, True, True,
                         False, True, False, True, True, True, True, True, True, False, True, True, False, True, True,
                         True, True, True, True, True, True, True, True, True, False, True, False, False, True, True,
                         True, False, False, False, True, False, True, True, True, True, True, True, False, False, True,
                         True, True, True, True, True, True, True, True, True, True, False, True, False, True, True,
                         True, True, True, True, True, True, True, True, True, False, False, True, True, True, True,
                         True, True, False, True, True, True, True, True, True, True]

avg_time_bf = mean(brute_force_times)
print(avg_time_bf)  # 0.013539376258850098

dfs_times = [0.0010266304016113281, 0.0010020732879638672, 0.007021665573120117, 0.009046316146850586,
             0.0009992122650146484, 0.01349639892578125, 0.0019998550415039062, 0.0009942054748535156,
             0.002073049545288086, 0.000993967056274414, 0.0010006427764892578, 0.0010013580322265625,
             0.0010044574737548828, 0.0009975433349609375, 0.003000497817993164, 0.008043289184570312,
             0.0009963512420654297, 0.009936332702636719, 0.003000020980834961, 0.002000093460083008,
             0.002001047134399414, 0.0009992122650146484, 0.0009996891021728516, 0.003000497817993164,
             0.0029990673065185547, 0.0009999275207519531, 0.004999637603759766, 0.005000114440917969,
             0.0009999275207519531, 0.0039997100830078125, 0.0030007362365722656, 0.0009987354278564453,
             0.0019998550415039062, 0.0020034313201904297, 0.0020008087158203125, 0.00800013542175293,
             0.0020020008087158203, 0.002000093460083008, 0.0019998550415039062, 0.008998870849609375,
             0.00099945068359375, 0.007000446319580078, 0.008998394012451172, 0.0010006427764892578,
             0.004012107849121094, 0.0009996891021728516, 0.006015777587890625, 0.008002281188964844,
             0.009015083312988281, 0.001997232437133789, 0.008044958114624023, 0.003996372222900391,
             0.001031637191772461, 0.001001119613647461, 0.001012563705444336, 0.0029985904693603516,
             0.0010006427764892578, 0.008059263229370117, 0.008167505264282227, 0.002000570297241211,
             0.002033233642578125, 0.004034519195556641, 0.0009989738464355469, 0.0010039806365966797,
             0.0009992122650146484, 0.0020034313201904297, 0.004010438919067383, 0.0009975433349609375,
             0.0020012855529785156, 0.0010001659393310547, 0.012994766235351562, 0.0030052661895751953,
             0.008999824523925781, 0.0009999275207519531, 0.0009992122650146484, 0.0009999275207519531,
             0.0009999275207519531, 0.0009999275207519531, 0.0029997825622558594, 0.002000570297241211,
             0.002000093460083008, 0.00099945068359375, 0.002000093460083008, 0.0010001659393310547,
             0.006033420562744141, 0.006002187728881836, 0.001001596450805664, 0.0009999275207519531,
             0.0029649734497070312, 0.003999948501586914, 0.0009999275207519531, 0.0009999275207519531,
             0.009000301361083984, 0.001999378204345703, 0.0009999275207519531, 0.004000186920166016,
             0.0020003318786621094, 0.0009996891021728516, 0.0010001659393310547, 0.0029997825622558594]
dfs_decisions = [True, True, True, False, True, False, True, True, True, True, True, True, True, True, True, False,
                 True, False, True, True, True, True, True, True, False, True, True, False, True, True, True, True,
                 True, True, True, True, True, True, True, False, True, False, False, True, True, True, False, False,
                 False, True, False, True, True, True, True, True, True, False, False, True, True, True, True, True,
                 True, True, True, True, True, True, False, True, False, True, True, True, True, True, True, True, True,
                 True, True, True, False, False, True, True, True, True, True, True, False, True, True, True, True,
                 True, True, True]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.0032007503509521485

# comparing decisions
print(brute_force_decisions == dfs_decisions)  # True