from statistics import mean
from math import inf

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [64.52285695075989, 17.60108757019043, 37.34415149688721, 34.960461139678955, 13.80306339263916,
             22.85663080215454, 50.20828032493591, 14.114762306213379, 17.04602599143982, 17.70869755744934,
             15.54318356513977, 7.911305665969849, 21.09320378303528, 12.419069051742554, 16.729209423065186,
             6.617024898529053, 10.218626499176025, 36.08318209648132, 10.368233680725098, 4.522981643676758,
             74.05006337165833, 27.488839149475098, 25.92202854156494, 27.77646255493164, 90.59197211265564,
             27.513270378112793, 10.309787034988403, 25.299839735031128, 92.45200204849243, 55.42105007171631,
             41.92452883720398, 59.991005420684814, 21.468746662139893, 15.139769077301025, 5.482778310775757,
             46.378865480422974, 18.09686040878296, 19.80805468559265, 23.31459069252014, 52.02870750427246,
             18.719996213912964, 62.823962926864624, 30.365925550460815, 22.060985565185547, 29.84760046005249,
             34.91477346420288, 17.45267915725708, 42.50434851646423, 8.936850786209106, 102.42783093452454,
             15.7878897190094, 212.11817288398743, 57.43581438064575, 2.8710546493530273, 41.13109469413757,
             48.59286570549011, 17.833276748657227, 22.08656668663025, 53.322057485580444, 18.786813974380493,
             95.96724343299866, 18.916141271591187, 63.96392107009888, 18.03710389137268, 22.464472770690918,
             21.206931591033936, 5.340784788131714, 10.66530966758728, 2.6841373443603516, 18.002745866775513,
             40.00096893310547, 14.279086112976074, 2.2664239406585693, 11.85679292678833, 21.423479080200195,
             27.024920225143433, 14.55545949935913, 20.263399362564087, 41.799373388290405, 25.711182355880737,
             3.008127212524414, 25.250365495681763, 28.55133891105652, 47.25681924819946, 4.094263315200806,
             5.588467121124268, 35.50360178947449, 24.088186264038086, 28.727437496185303, 28.47810411453247,
             20.823527574539185, 39.46990990638733, 40.338165521621704, 76.0909423828125, 36.70693254470825,
             8.792473554611206, 7.691776990890503, 26.804133653640747, 70.7186233997345, 107.404860496521]
dfs_decisions = [(True, 163), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 180),
                 (True, 142), (True, 192), (False, inf), (True, 130), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (True, 150), (True, 173), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (True, 155), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (True, 142), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (True, 182), (False, inf), (True, 121), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (True, 142), (False, inf), (True, 138), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf)]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 32.13969754934311

dfs_cut_times = [55.84287166595459, 18.130980014801025, 37.56361246109009, 34.978336334228516, 14.148293256759644,
                 22.683414697647095, 51.370596170425415, 12.88221526145935, 17.373042583465576, 18.033931493759155,
                 15.925163269042969, 7.975214242935181, 20.20989727973938, 12.287745714187622, 16.824368238449097,
                 6.716385841369629, 10.220042705535889, 37.030829429626465, 10.388603210449219, 4.736525297164917,
                 84.18947649002075, 26.72298240661621, 26.803837060928345, 27.476988315582275, 96.59212350845337,
                 26.267279386520386, 10.07533884048462, 25.199135541915894, 91.18947458267212, 58.290791273117065,
                 39.52940630912781, 52.37644672393799, 21.620986700057983, 14.485053300857544, 5.998008966445923,
                 44.214110136032104, 19.35755443572998, 19.956687688827515, 23.709546327590942, 47.46715068817139,
                 18.683096647262573, 66.48561072349548, 28.65071129798889, 22.909936904907227, 28.665985107421875,
                 35.223432540893555, 17.939709186553955, 42.87327265739441, 8.890892267227173, 105.24318027496338,
                 16.277849912643433, 164.40850806236267, 68.07093667984009, 3.5374956130981445, 38.4496431350708,
                 45.097752809524536, 17.683882236480713, 25.763097524642944, 43.742279291152954, 19.50308847427368,
                 99.86139178276062, 19.66935420036316, 63.62082552909851, 18.628308057785034, 23.66764807701111,
                 21.937129020690918, 5.547426462173462, 9.751454591751099, 2.715259552001953, 18.151176929473877,
                 41.986600160598755, 14.79966688156128, 2.3333964347839355, 11.88326644897461, 22.063397645950317,
                 25.56268572807312, 15.331768274307251, 20.490345001220703, 40.29733395576477, 24.096205949783325,
                 3.7244224548339844, 23.374147415161133, 28.76129388809204, 50.51021385192871, 4.122405290603638,
                 5.448525667190552, 35.1232430934906, 24.856266260147095, 29.81364870071411, 28.747469425201416,
                 21.810155630111694, 39.28691363334656, 40.46087384223938, 77.69871211051941, 37.37239909172058,
                 9.136693954467773, 7.49371337890625, 27.406080722808838, 71.74304294586182, 107.4664990901947]
dfs_cut_decisions = [(True, 163), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 180),
                     (True, 142), (True, 192), (False, inf), (True, 130), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (True, 150), (True, 173), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (True, 155), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (True, 142), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (True, 182), (False, inf), (True, 121), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (True, 142), (False, inf), (True, 138), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf)]

avg_time_dfs_cut = mean(dfs_cut_times)
print(avg_time_dfs_cut)  # 31.816961703300475

# comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
print(dfs_decisions == dfs_cut_decisions)  # true