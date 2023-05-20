from statistics import mean

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [1.3994934558868408, 11.062541961669922, 21.484537839889526, 2.403856039047241, 3.0649068355560303,
             0.8428316116333008, 0.05196404457092285, 10.909653425216675, 2.421250581741333, 8.325790643692017,
             1.3506956100463867, 4.026396036148071, 2.222808361053467, 5.415073394775391, 0.12696242332458496,
             0.27735066413879395, 12.14949345588684, 2.407217264175415, 23.151097536087036, 3.6978683471679688,
             2.1342148780822754, 4.893697023391724, 3.816819906234741, 0.0540003776550293, 3.095853805541992,
             0.8866355419158936, 0.1477820873260498, 0.11075663566589355, 0.004203081130981445, 1.620058536529541,
             14.509762525558472, 0.5833108425140381, 2.41123104095459, 5.121011018753052, 14.953119993209839,
             3.4481399059295654, 19.006025075912476, 45.353652477264404, 1.9105279445648193, 1.9495570659637451,
             5.6485583782196045, 10.4066321849823, 1.213531255722046, 7.654295921325684, 7.636344909667969,
             11.210333108901978, 7.487075567245483, 8.946225643157959, 18.21035885810852, 12.424928665161133,
             0.3670814037322998, 0.13528752326965332, 9.512370109558105, 0.012998819351196289, 0.1991724967956543,
             11.2214834690094, 5.308420419692993, 0.05468034744262695, 4.089433431625366, 0.4489619731903076,
             0.2625279426574707, 0.8712141513824463, 5.553581953048706, 5.329376220703125, 0.012971162796020508,
             6.910143613815308, 0.055266380310058594, 2.9198176860809326, 6.552264928817749, 1.1596972942352295,
             6.568556308746338, 4.005011320114136, 2.6782829761505127, 1.4356234073638916, 4.176398515701294,
             0.37218689918518066, 0.010159015655517578, 3.363069534301758, 12.648746252059937, 9.150885820388794,
             2.087937116622925, 6.868921995162964, 3.5468482971191406, 1.8917186260223389, 1.6243822574615479,
             0.1619277000427246, 2.7620227336883545, 16.293554306030273, 0.22713398933410645, 5.7046239376068115,
             5.808668613433838, 8.06568193435669, 3.343160390853882, 1.1053922176361084, 0.09611248970031738,
             0.27493834495544434, 3.5314412117004395, 21.71131205558777, 1.1358542442321777, 6.400267601013184]
dfs_decisions = [True, False, False, False, False, False, True, False, True, False, True, False, True, False, True,
                 True, False, True, False, False, False, False, False, True, False, True, True, True, True, True, False,
                 True, True, False, False, False, False, False, False, False, False, False, False, False, True, False,
                 False, False, False, False, True, True, False, True, True, False, False, True, False, True, True, True,
                 False, False, True, False, True, False, True, False, False, False, False, True, False, True, True,
                 False, False, False, True, False, True, False, False, True, False, False, True, False, False, False,
                 False, True, True, True, True, False, True, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 5.316680052280426

# comparing decisions
print(brute_force_decisions == dfs_decisions)