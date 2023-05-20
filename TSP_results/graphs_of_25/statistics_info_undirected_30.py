from statistics import mean
from math import inf

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [0.6782631874084473, 0.8799600601196289, 0.0, 0.4309968948364258, 0.199998140335083, 0.45403170585632324,
             0.3049924373626709, 0.1849994659423828, 0.05900144577026367, 0.05000042915344238, 0.12388801574707031,
             0.44899606704711914, 0.0, 0.4109964370727539, 0.1060025691986084, 0.4230318069458008, 0.418994665145874,
             1.1209566593170166, 0.0, 0.32703208923339844, 0.17200088500976562, 0.19796299934387207,
             0.19800186157226562, 0.15099835395812988, 0.16199922561645508, 0.029999732971191406, 0.08699893951416016,
             0.47899508476257324, 0.049001216888427734, 0.2519972324371338, 0.4179959297180176, 0.0010001659393310547,
             0.3969919681549072, 0.40503358840942383, 0.12799406051635742, 0.02099776268005371, 0.5219957828521729,
             0.3049967288970947, 0.0010001659393310547, 0.31003355979919434, 0.0010004043579101562, 0.35996127128601074,
             0.32799649238586426, 0.24202775955200195, 0.019002914428710938, 0.5639553070068359, 0.7029929161071777,
             0.5839941501617432, 1.4459826946258545, 0.17699813842773438, 0.7879598140716553, 0.25199437141418457,
             0.5059604644775391, 0.0009999275207519531, 0.0009996891021728516, 0.4040334224700928, 0.9279553890228271,
             0.1289985179901123, 0.45899343490600586, 0.14699864387512207, 0.5079984664916992, 0.292996883392334,
             0.1550004482269287, 0.6590316295623779, 0.16296148300170898, 0.4049994945526123, 0.7749919891357422,
             0.18400049209594727, 0.9719893932342529, 0.33699488639831543, 0.2129659652709961, 0.0009992122650146484,
             0.9859921932220459, 0.03599953651428223, 0.18799662590026855, 0.6120281219482422, 0.21799612045288086,
             0.36599254608154297, 0.8109924793243408, 0.0010001659393310547, 0.13899946212768555, 0.14899849891662598,
             0.45299863815307617, 0.10199975967407227, 0.0, 0.0, 0.3450348377227783, 1.1149885654449463,
             0.03499960899353027, 0.0009684562683105469, 0.0630335807800293, 0.21999764442443848, 0.8349916934967041,
             0.10499858856201172, 0.5320203304290771, 1.5929841995239258, 0.4079620838165283, 0.45403027534484863,
             0.07696318626403809, 0.922992467880249]
dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf)]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.34378833055496216

dfs_cut_times = [0.5710251331329346, 0.8139886856079102, 0.0009999275207519531, 0.3509950637817383, 0.25500059127807617,
                 0.415996789932251, 0.29599571228027344, 0.19199728965759277, 0.0599980354309082, 0.05207681655883789,
                 0.12999868392944336, 0.4410269260406494, 0.0010013580322265625, 0.4109928607940674,
                 0.10796141624450684, 0.4499950408935547, 0.39899706840515137, 1.157984972000122, 0.0009999275207519531,
                 0.32199692726135254, 0.17499494552612305, 0.1999979019165039, 0.18799448013305664, 0.15500140190124512,
                 0.15799856185913086, 0.03199934959411621, 0.08799600601196289, 0.48099493980407715,
                 0.051001548767089844, 0.24899721145629883, 0.4199957847595215, 0.0, 0.38599634170532227,
                 0.40199947357177734, 0.12999892234802246, 0.02100086212158203, 0.5309581756591797, 0.30699706077575684,
                 0.0, 0.29099488258361816, 0.0, 0.3959999084472656, 0.32399702072143555, 0.2330000400543213,
                 0.017999649047851562, 0.5579977035522461, 0.6479935646057129, 0.5379927158355713, 1.5410215854644775,
                 0.17999935150146484, 0.812990665435791, 0.2310318946838379, 0.5259950160980225, 0.0010001659393310547,
                 0.0, 0.39899730682373047, 0.9819867610931396, 0.14100217819213867, 0.4719972610473633,
                 0.14299511909484863, 0.5159947872161865, 0.28102803230285645, 0.1649620532989502, 0.6879918575286865,
                 0.16699838638305664, 0.40202951431274414, 0.788989782333374, 0.19699764251708984, 0.9249916076660156,
                 0.358997106552124, 0.21002984046936035, 0.0, 0.9429538249969482, 0.03800082206726074,
                 0.18900036811828613, 0.5589966773986816, 0.23496508598327637, 0.38199901580810547, 0.8069882392883301,
                 0.0, 0.14499735832214355, 0.15199875831604004, 0.43802905082702637, 0.10396122932434082,
                 0.001003265380859375, 0.0010001659393310547, 0.3779571056365967, 1.0569860935211182,
                 0.035035133361816406, 0.0009982585906982422, 0.06396317481994629, 0.20699787139892578,
                 0.8009955883026123, 0.10500574111938477, 0.5319943428039551, 1.7589845657348633, 0.43499207496643066,
                 0.4289970397949219, 0.07900094985961914, 1.0109901428222656]
dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf)]

avg_time_dfs_cut = mean(dfs_cut_times)
print(avg_time_dfs_cut)  # 0.34423747539520266

# comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
print(dfs_decisions == dfs_cut_decisions)  # true
