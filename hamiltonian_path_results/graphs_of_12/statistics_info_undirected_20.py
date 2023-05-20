from statistics import mean

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [0.5564076900482178, 0.8162853717803955, 0.31566548347473145, 0.20133638381958008, 0.49529457092285156,
             0.44986510276794434, 0.24612998962402344, 0.21500825881958008, 0.3818655014038086, 0.3608067035675049,
             0.24673819541931152, 0.24190115928649902, 0.40026259422302246, 0.5274596214294434, 0.27173662185668945,
             0.28699779510498047, 0.6315228939056396, 0.18831133842468262, 0.039000749588012695, 0.029999732971191406,
             0.7152450084686279, 0.4528191089630127, 0.23887920379638672, 1.3637759685516357, 0.014085054397583008,
             0.25610995292663574, 0.0683746337890625, 0.03295421600341797, 0.003998279571533203, 0.39322710037231445,
             0.06511449813842773, 0.48448967933654785, 0.8375382423400879, 0.5369017124176025, 0.021001100540161133,
             0.35623979568481445, 0.4171562194824219, 0.37886619567871094, 1.6182129383087158, 0.6841742992401123,
             0.44191622734069824, 0.003999948501586914, 0.47795772552490234, 0.30499839782714844, 0.23614072799682617,
             0.24241161346435547, 0.03899955749511719, 0.6320517063140869, 0.12108111381530762, 0.32135534286499023,
             0.15386581420898438, 0.351459264755249, 0.017128467559814453, 0.38206911087036133, 0.28815770149230957,
             0.29651856422424316, 0.2532234191894531, 0.22951626777648926, 0.05808234214782715, 0.6029918193817139,
             0.5140972137451172, 0.07140350341796875, 0.2706880569458008, 0.30736422538757324, 0.23927617073059082,
             0.37222862243652344, 0.9292595386505127, 0.11300182342529297, 0.05799603462219238, 0.2581799030303955,
             0.35016965866088867, 0.15790867805480957, 0.005965471267700195, 0.4394087791442871, 0.42649412155151367,
             0.16318941116333008, 1.2332627773284912, 0.9814243316650391, 0.1340022087097168, 0.2759287357330322,
             0.06917476654052734, 0.5653624534606934, 1.021669864654541, 0.4952387809753418, 0.03839373588562012,
             0.1568443775177002, 0.3920867443084717, 0.9548394680023193, 1.4490091800689697, 0.4946894645690918,
             0.27488279342651367, 0.3290226459503174, 0.18500018119812012, 0.09698700904846191, 0.0063343048095703125,
             0.10170149803161621, 0.537339448928833, 0.2867164611816406, 0.5452041625976562, 0.28763651847839355]
dfs_decisions = [False, False, False, False, False, False, False, False, True, False, False, False, False, False, False,
                 False, False, False, True, True, False, False, False, False, True, True, True, True, True, False,
                 False, False, False, False, True, False, False, False, False, False, True, True, False, False, False,
                 False, True, False, True, False, True, False, True, False, False, False, False, False, True, False,
                 False, True, True, False, False, False, False, False, True, False, False, True, True, False, False,
                 True, False, False, True, False, True, False, False, False, False, False, False, False, False, False,
                 True, False, False, False, True, False, False, False, False, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.36885067224502566

# comparing decisions
print(brute_force_decisions == dfs_decisions)
