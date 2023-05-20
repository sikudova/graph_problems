from statistics import mean
from math import inf

brute_force_times = [1287.4022080898285]
brute_force_decisions = [(False, inf)]

avg_time_bf = mean(brute_force_times)
print(avg_time_bf)  # 1287.4022080898285

dfs_times = [0.13696527481079102, 0.031000137329101562, 0.0709998607635498, 0.14699959754943848, 0.057000160217285156,
             0.10799980163574219, 0.07896804809570312, 0.02499985694885254, 0.08499956130981445, 0.180999755859375,
             0.1139676570892334, 0.0489964485168457, 0.09999990463256836, 0.13699984550476074, 0.14696455001831055,
             0.15399956703186035, 0.10696530342102051, 0.09300065040588379, 0.08103251457214355, 0.04396510124206543,
             0.11300134658813477, 0.09799885749816895, 0.14599895477294922, 0.07300019264221191, 0.052000999450683594,
             0.2249305248260498, 0.11399960517883301, 0.09599924087524414, 0.06300020217895508, 0.03399968147277832,
             0.15100932121276855, 0.19603276252746582, 0.04096627235412598, 0.04000496864318848, 0.15696454048156738,
             0.15096378326416016, 0.04799962043762207, 0.1250293254852295, 0.03999805450439453, 0.08899784088134766,
             0.05400204658508301, 0.29599833488464355, 0.04499983787536621, 0.029997825622558594, 0.04899740219116211,
             0.08299970626831055, 0.1080021858215332, 0.21399998664855957, 0.20999979972839355, 0.03999662399291992,
             0.0, 0.11299777030944824, 0.027001380920410156, 0.039999961853027344, 0.12700653076171875,
             0.050995826721191406, 0.016998291015625, 0.4669933319091797, 0.18699979782104492, 0.03900027275085449,
             0.03600001335144043, 0.12403535842895508, 0.09100031852722168, 0.06100344657897949, 0.07000279426574707,
             0.09900307655334473, 0.13900327682495117, 0.11896467208862305, 0.06599998474121094, 0.2689993381500244,
             0.09400081634521484, 0.022999286651611328, 0.03499937057495117, 0.03699922561645508, 0.2810361385345459,
             0.16399669647216797, 0.2819993495941162, 0.04899954795837402, 0.1040341854095459, 0.13400602340698242,
             0.04299569129943848, 0.06699967384338379, 0.035997629165649414, 0.1979963779449463, 0.06299948692321777,
             0.06700015068054199, 0.1640322208404541, 0.06799864768981934, 0.08999943733215332, 0.020999908447265625,
             0.18805956840515137, 0.08103156089782715, 0.030999183654785156, 0.0939943790435791, 0.0449979305267334,
             0.0, 0.19399738311767578, 0.037964820861816406, 0.1589961051940918, 0.000997304916381836]
dfs_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (True, 100), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (True, 105), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (True, 99), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 104), (True, 89),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (True, 106), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (True, 108), (False, inf), (True, 106),
                 (False, inf), (False, inf), (False, inf), (False, inf), (True, 96), (False, inf), (False, inf),
                 (False, inf), (False, inf), (True, 110), (False, inf), (False, inf), (False, inf), (True, 71),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                 (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 96),
                 (False, inf), (False, inf)]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.1012084698677063

dfs_cut_times = [0.047000885009765625, 0.030998706817626953, 0.0709998607635498, 0.15303516387939453,
                 0.057999610900878906, 0.11499977111816406, 0.07999610900878906, 0.026000022888183594,
                 0.08499979972839355, 0.18103480339050293, 0.12999987602233887, 0.04799985885620117,
                 0.10103416442871094, 0.1360034942626953, 0.14399981498718262, 0.15503144264221191, 0.15203404426574707,
                 0.09696769714355469, 0.07399797439575195, 0.043000221252441406, 0.12103533744812012,
                 0.09699869155883789, 0.14400076866149902, 0.07399868965148926, 0.05703592300415039,
                 0.22999978065490723, 0.11700057983398438, 0.09399938583374023, 0.06299972534179688,
                 0.034999847412109375, 0.15299034118652344, 0.19699931144714355, 0.03903365135192871,
                 0.04099440574645996, 0.1020345687866211, 0.15900301933288574, 0.04800128936767578, 0.12400197982788086,
                 0.04100203514099121, 0.09399986267089844, 0.05499839782714844, 0.2480018138885498, 0.04700112342834473,
                 0.031001806259155273, 0.055001258850097656, 0.08399844169616699, 0.10899686813354492,
                 0.21599912643432617, 0.20900273323059082, 0.04296588897705078, 0.001035928726196289,
                 0.11599993705749512, 0.026997804641723633, 0.03999924659729004, 0.12700176239013672,
                 0.05199837684631348, 0.017005205154418945, 0.45296335220336914, 0.18999934196472168,
                 0.03999972343444824, 0.03599953651428223, 0.12999892234802246, 0.09199953079223633,
                 0.05999588966369629, 0.07099676132202148, 0.09799790382385254, 0.14199542999267578,
                 0.11399960517883301, 0.06599974632263184, 0.26003432273864746, 0.09500551223754883,
                 0.025959014892578125, 0.03500032424926758, 0.03699994087219238, 0.254000186920166, 0.1809687614440918,
                 0.27903032302856445, 0.0489659309387207, 0.10999274253845215, 0.13300395011901855, 0.04196596145629883,
                 0.07100582122802734, 0.03399991989135742, 0.1849989891052246, 0.06400012969970703, 0.06900167465209961,
                 0.17500019073486328, 0.06796979904174805, 0.09099960327148438, 0.020999670028686523,
                 0.18194007873535156, 0.07500171661376953, 0.033006906509399414, 0.09799885749816895,
                 0.0429995059967041, 0.0010023117065429688, 0.19900178909301758, 0.03803539276123047,
                 0.16300296783447266, 0.0010020732879638672]
dfs_cut_decisions = [(False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (True, 100), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (True, 105), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (True, 99), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 104), (True, 89),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (True, 106), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (True, 108), (False, inf), (True, 106),
                     (False, inf), (False, inf), (False, inf), (False, inf), (True, 96), (False, inf), (False, inf),
                     (False, inf), (False, inf), (True, 110), (False, inf), (False, inf), (False, inf), (True, 71),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf),
                     (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (False, inf), (True, 96),
                     (False, inf), (False, inf)]

avg_time_dfs_cut = mean(dfs_cut_times)
print(avg_time_dfs_cut)  # 0.10038108348846436

# comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
print(dfs_decisions == dfs_cut_decisions)
# from statistics import mean
# from math import inf
#
# brute_force_times = [1287.4022080898285]
# brute_force_decisions = [(False, inf)]
#
# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)
#
# dfs_times = [0.06599950790405273]
# dfs_decisions = [(False, inf)]
#
# avg_time_dfs = mean(dfs_times)
# print(avg_time_dfs)
#
# dfs_cut_times = [0.04700183868408203]
# dfs_cut_decisions = [(False, inf)]
#
# avg_time_dfs_cut = mean(dfs_cut_times)
# print(avg_time_dfs_cut)
#
# # comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
