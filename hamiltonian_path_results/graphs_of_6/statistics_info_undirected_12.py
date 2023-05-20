from statistics import mean

brute_force_times = [0.11403632164001465, 0.006972312927246094, 0.06815171241760254, 0.24364399909973145,
                     0.008999347686767578, 0.009002923965454102, 0.051001787185668945, 0.06821155548095703,
                     0.27605700492858887, 0.08062434196472168, 0.24174284934997559, 0.026000022888183594,
                     0.021000146865844727, 0.08703446388244629, 0.011000633239746094, 0.017002105712890625,
                     0.0059702396392822266, 0.006045103073120117, 0.014945745468139648, 0.03795576095581055,
                     0.06898665428161621, 0.04998660087585449, 0.009011983871459961, 0.0019998550415039062,
                     0.00800013542175293, 0.28452396392822266, 0.01699972152709961, 0.009999990463256836,
                     0.0029997825622558594, 0.04199957847595215, 0.0010001659393310547, 0.00500035285949707,
                     0.0010004043579101562, 0.0235135555267334, 0.010999679565429688, 0.02299952507019043,
                     0.2685425281524658, 0.09901142120361328, 0.013013362884521484, 0.06500911712646484,
                     0.00800013542175293, 0.0010001659393310547, 0.009999990463256836, 0.003999471664428711,
                     0.0069997310638427734, 0.017000198364257812, 0.018000125885009766, 0.1361243724822998,
                     0.012215852737426758, 0.1714615821838379, 0.1943345069885254, 0.0030012130737304688,
                     0.25166773796081543, 0.006045341491699219, 0.025089263916015625, 0.003000020980834961,
                     0.02714061737060547, 0.05321907997131348, 0.003998517990112305, 0.16591143608093262,
                     0.011070966720581055, 0.006999969482421875, 0.014046907424926758, 0.0009992122650146484,
                     0.17498373985290527, 0.02013397216796875, 0.2756822109222412, 0.00599980354309082,
                     0.1300821304321289, 0.00604557991027832, 0.026044368743896484, 0.049976348876953125,
                     0.006000041961669922, 0.00599980354309082, 0.0010004043579101562, 0.002000093460083008,
                     0.166046142578125, 0.039093732833862305, 0.008027791976928711, 0.0009989738464355469,
                     0.12221503257751465, 0.2110750675201416, 0.20589804649353027, 0.08700370788574219,
                     0.013998270034790039, 0.011985063552856445, 0.034014225006103516, 0.03500008583068848,
                     0.026879072189331055, 0.010000944137573242, 0.2438826560974121, 0.213212251663208,
                     0.018990039825439453, 0.2200002670288086, 0.24012207984924316, 0.009563684463500977,
                     0.023141860961914062, 0.23490262031555176, 0.005044460296630859, 0.0050067901611328125]
brute_force_decisions = [True, True, True, False, True, True, True, True, False, True, False, True, True, True, True,
                         True, True, True, True, True, True, True, True, True, True, False, True, True, True, True,
                         True, True, True, True, True, True, False, True, True, True, True, True, True, True, True,
                         True, True, True, True, False, False, True, False, True, True, True, True, True, True, False,
                         True, True, True, True, False, True, False, True, True, True, True, True, True, True, True,
                         True, True, True, True, True, True, False, False, True, True, True, True, True, True, True,
                         False, False, True, False, False, True, True, False, True, True]

avg_time_bf = mean(brute_force_times)
print(avg_time_bf) # 0.0644137454032898

dfs_times = [0.0009989738464355469, 0.00302886962890625, 0.0059986114501953125, 0.012998819351196289,
             0.002999544143676758, 0.0020034313201904297, 0.0059964656829833984, 0.003971099853515625,
             0.029999971389770508, 0.0050013065338134766, 0.018000364303588867, 0.002000093460083008,
             0.003999233245849609, 0.008002758026123047, 0.000997781753540039, 0.0019989013671875, 0.002000570297241211,
             0.0010001659393310547, 0.003010988235473633, 0.003013134002685547, 0.003983259201049805,
             0.0019996166229248047, 0.0010001659393310547, 0.0020122528076171875, 0.0020139217376708984,
             0.028011322021484375, 0.002000093460083008, 0.0010001659393310547, 0.0010001659393310547,
             0.003999948501586914, 0.0039997100830078125, 0.0009999275207519531, 0.0020003318786621094,
             0.002000570297241211, 0.0010004043579101562, 0.001001119613647461, 0.026049137115478516,
             0.012999773025512695, 0.00099945068359375, 0.004999876022338867, 0.0019998550415039062,
             0.0009999275207519531, 0.0020003318786621094, 0.003000020980834961, 0.002000093460083008,
             0.0019998550415039062, 0.0019998550415039062, 0.01602029800415039, 0.0019996166229248047,
             0.005079746246337891, 0.009047985076904297, 0.001961231231689453, 0.008002042770385742,
             0.000997781753540039, 0.0009992122650146484, 0.002000093460083008, 0.0019996166229248047,
             0.0053195953369140625, 0.002013683319091797, 0.004019498825073242, 0.0010004043579101562,
             0.0010001659393310547, 0.0019981861114501953, 0.0009999275207519531, 0.006000041961669922,
             0.002045869827270508, 0.031000137329101562, 0.0010001659393310547, 0.01104736328125, 0.000997781753540039,
             0.002000093460083008, 0.00599980354309082, 0.0009999275207519531, 0.002000093460083008,
             0.004999637603759766, 0.004000186920166016, 0.016031265258789062, 0.0009982585906982422,
             0.00099945068359375, 0.003000974655151367, 0.00799870491027832, 0.011079072952270508, 0.010000228881835938,
             0.006014585494995117, 0.0009996891021728516, 0.0009996891021728516, 0.002000093460083008,
             0.004999876022338867, 0.0010008811950683594, 0.002998828887939453, 0.020018815994262695,
             0.011987924575805664, 0.0020003318786621094, 0.013086318969726562, 0.02036142349243164,
             0.0006351470947265625, 0.001001119613647461, 0.019110441207885742, 0.0009999275207519531,
             0.002053499221801758]
dfs_decisions = [True, True, True, False, True, True, True, True, False, True, False, True, True, True, True, True,
                 True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True,
                 True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, False,
                 False, True, False, True, True, True, True, True, True, False, True, True, True, True, False, True,
                 False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False,
                 False, True, True, True, True, True, True, True, False, False, True, False, False, True, True, False,
                 True, True]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs) # 0.005310189723968506

# comparing decisions
print(brute_force_decisions == dfs_decisions) # True