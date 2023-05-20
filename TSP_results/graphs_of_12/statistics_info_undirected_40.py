from statistics import mean
from math import inf

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [7.280949831008911, 8.43691110610962, 6.696927309036255, 16.293789625167847, 9.549899339675903,
             2.1759445667266846, 9.161904335021973, 8.218953609466553, 2.115994691848755, 10.088860273361206,
             8.04295015335083, 11.135853052139282, 7.565924167633057, 12.600872993469238, 14.062859296798706,
             30.329660654067993, 6.50093674659729, 4.429996967315674, 9.861964464187622, 3.326932907104492,
             13.16686725616455, 8.010887145996094, 22.756736040115356, 42.33459997177124, 3.8959619998931885,
             1.845952033996582, 23.598779916763306, 2.7879698276519775, 4.273958206176758, 18.51882529258728,
             73.72234654426575, 39.598628759384155, 4.426995277404785, 34.35465216636658, 41.578595876693726,
             25.928283214569092, 4.581975221633911, 10.207945108413696, 42.95397162437439, 28.962362051010132,
             38.26572036743164, 36.32422065734863, 4.378994703292847, 5.6009485721588135, 23.75285530090332,
             9.198922634124756, 5.491952180862427, 8.257935047149658, 15.13483715057373, 24.049891471862793,
             2.437980890274048, 5.838987350463867, 5.986952781677246, 45.52415919303894, 20.07980728149414,
             15.145849227905273, 23.519851684570312, 9.425961017608643, 25.76376461982727, 5.102959632873535,
             11.142952680587769, 5.633920907974243, 16.188876390457153, 5.415961265563965, 42.56568908691406,
             6.285986423492432, 11.30091381072998, 19.45885443687439, 4.768964529037476, 4.842962980270386,
             23.019829034805298, 42.72168445587158, 12.531942367553711, 4.994932413101196, 8.44493842124939,
             5.316998481750488, 14.278900384902954, 37.61773729324341, 6.039989709854126, 4.978002071380615,
             5.456929445266724, 45.24872040748596, 8.099907159805298, 9.350967168807983, 21.004884958267212,
             31.381792545318604, 2.7849812507629395, 10.26393175125122, 19.202836513519287, 26.610823392868042,
             3.5979747772216797, 9.541933298110962, 10.049931764602661, 27.14235520362854, 4.409974575042725,
             5.09699821472168, 14.208937644958496, 17.146923780441284, 37.60671949386597, 60.215261459350586]
dfs_decisions = [(True, 89), (True, 72), (True, 108), (False, inf), (True, 90), (True, 70), (True, 105), (False, inf),
                 (True, 107), (False, inf), (True, 133), (True, 93), (True, 98), (True, 67), (True, 121), (True, 83),
                 (True, 105), (False, inf), (True, 70), (True, 95), (True, 111), (True, 102), (True, 88), (True, 122),
                 (True, 135), (True, 95), (True, 90), (False, inf), (True, 96), (False, inf), (True, 68), (True, 95),
                 (True, 89), (True, 92), (True, 93), (True, 89), (False, inf), (False, inf), (True, 65), (True, 106),
                 (True, 84), (True, 82), (True, 101), (True, 131), (True, 79), (True, 128), (True, 102), (True, 82),
                 (False, inf), (True, 80), (True, 143), (True, 138), (False, inf), (True, 74), (True, 75), (True, 112),
                 (True, 81), (True, 105), (True, 80), (True, 99), (True, 96), (True, 95), (True, 76), (False, inf),
                 (True, 100), (False, inf), (True, 114), (True, 67), (True, 111), (True, 107), (True, 77), (True, 82),
                 (True, 118), (True, 131), (True, 138), (True, 104), (True, 59), (True, 70), (True, 130), (True, 116),
                 (True, 124), (True, 80), (True, 82), (True, 127), (True, 76), (True, 84), (True, 105), (False, inf),
                 (True, 111), (True, 84), (True, 96), (True, 79), (True, 89), (False, inf), (False, inf), (False, inf),
                 (True, 112), (True, 84), (True, 99), (True, 105)]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 16.206397533416748

dfs_cut_times = [5.507948160171509, 5.270941734313965, 5.529942035675049, 16.043864011764526, 7.973912954330444,
                 1.839012861251831, 6.9488935470581055, 8.423881530761719, 2.2279958724975586, 10.151901483535767,
                 8.015551567077637, 8.15795350074768, 5.988937854766846, 5.133946418762207, 12.211877584457397,
                 15.75987195968628, 5.743942499160767, 4.247953176498413, 5.141981363296509, 2.408010482788086,
                 10.73689079284668, 6.364970922470093, 13.779895782470703, 32.992685317993164, 3.8859615325927734,
                 1.7980153560638428, 10.345898151397705, 2.8239948749542236, 3.4309661388397217, 18.035828351974487,
                 18.37633776664734, 24.33678412437439, 3.857973337173462, 16.003895044326782, 26.1697998046875,
                 17.872808933258057, 4.604940891265869, 10.108877420425415, 12.603885650634766, 22.328771829605103,
                 15.451864957809448, 15.677834272384644, 3.8999712467193604, 5.683917760848999, 19.438725233078003,
                 8.39296817779541, 4.9889562129974365, 6.241943597793579, 15.343875169754028, 17.127845525741577,
                 2.5559792518615723, 5.545956373214722, 6.354918956756592, 13.730925559997559, 9.815953731536865,
                 13.102892875671387, 19.965808391571045, 7.801934480667114, 15.628876447677612, 3.8229665756225586,
                 8.523929357528687, 5.617962121963501, 8.488973140716553, 5.45092248916626, 27.281797885894775,
                 6.153954744338989, 8.753936529159546, 8.991903066635132, 4.404964923858643, 4.691000461578369,
                 6.614919900894165, 25.76780891418457, 11.577919006347656, 5.147964239120483, 7.711944818496704,
                 5.385930061340332, 6.156988143920898, 18.537838459014893, 6.163920640945435, 4.699966669082642,
                 5.40695858001709, 23.784832239151, 6.930955648422241, 8.45290756225586, 10.712925910949707,
                 17.91588020324707, 2.6289520263671875, 10.149966478347778, 17.283924341201782, 15.054864168167114,
                 3.12898325920105, 7.79795241355896, 6.2390007972717285, 27.208783388137817, 4.646968841552734,
                 5.286933422088623, 9.696901082992554, 11.537935733795166, 26.953866720199585, 31.80479621887207]
dfs_cut_decisions = [(True, 89), (True, 72), (True, 108), (False, inf), (True, 90), (True, 70), (True, 105),
                     (False, inf), (True, 107), (False, inf), (True, 133), (True, 93), (True, 98), (True, 67),
                     (True, 121), (True, 83), (True, 105), (False, inf), (True, 70), (True, 95), (True, 111),
                     (True, 102), (True, 88), (True, 122), (True, 135), (True, 95), (True, 90), (False, inf),
                     (True, 96), (False, inf), (True, 68), (True, 95), (True, 89), (True, 92), (True, 93), (True, 89),
                     (False, inf), (False, inf), (True, 65), (True, 106), (True, 84), (True, 82), (True, 101),
                     (True, 131), (True, 79), (True, 128), (True, 102), (True, 82), (False, inf), (True, 80),
                     (True, 143), (True, 138), (False, inf), (True, 74), (True, 75), (True, 112), (True, 81),
                     (True, 105), (True, 80), (True, 99), (True, 96), (True, 95), (True, 76), (False, inf), (True, 100),
                     (False, inf), (True, 114), (True, 67), (True, 111), (True, 107), (True, 77), (True, 82),
                     (True, 118), (True, 131), (True, 138), (True, 104), (True, 59), (True, 70), (True, 130),
                     (True, 116), (True, 124), (True, 80), (True, 82), (True, 127), (True, 76), (True, 84), (True, 105),
                     (False, inf), (True, 111), (True, 84), (True, 96), (True, 79), (True, 89), (False, inf),
                     (False, inf), (False, inf), (True, 112), (True, 84), (True, 99), (True, 105)]

avg_time_dfs_cut = mean(dfs_cut_times)
print(avg_time_dfs_cut)  # 10.525104520320893

# comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
print(dfs_decisions == dfs_cut_decisions)