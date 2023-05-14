from statistics import mean

brute_force_times = [0.1290590763092041, 0.029048442840576172, 0.005001544952392578, 0.027060508728027344,
                     0.0301969051361084, 0.029259443283081055, 0.02282547950744629, 0.0050432682037353516,
                     0.002998828887939453, 0.015134096145629883, 0.013086557388305664, 0.02316904067993164,
                     0.006043910980224609, 0.025917768478393555, 0.030138015747070312, 0.022050142288208008,
                     0.03009033203125, 0.002998828887939453, 0.02514505386352539, 0.013962984085083008,
                     0.0039997100830078125, 0.009000062942504883, 0.01699995994567871, 0.0280001163482666,
                     0.026999950408935547, 0.03000044822692871, 0.018999814987182617, 0.00800013542175293,
                     0.025999784469604492, 0.029033899307250977, 0.020997285842895508, 0.010999917984008789,
                     0.03213620185852051, 0.01601266860961914, 0.011936664581298828, 0.02696537971496582,
                     0.025957345962524414, 0.015004634857177734, 0.019998550415039062, 0.023043394088745117,
                     0.029081344604492188, 0.002999544143676758, 0.02611231803894043, 0.007052898406982422,
                     0.0020008087158203125, 0.024097681045532227, 0.020131826400756836, 0.027028799057006836,
                     0.003000974655151367, 0.025000810623168945, 0.008000612258911133, 0.027002334594726562,
                     0.010999679565429688, 0.015999317169189453, 0.023999691009521484, 0.018984317779541016,
                     0.0029981136322021484, 0.023966312408447266, 0.027059078216552734, 0.023036718368530273,
                     0.027045726776123047, 0.010996580123901367, 0.02803182601928711, 0.028127670288085938,
                     0.022971391677856445, 0.02991795539855957, 0.02695155143737793, 0.030013322830200195,
                     0.0039997100830078125, 0.0010006427764892578, 0.027024269104003906, 0.004999876022338867,
                     0.03302502632141113, 0.004000425338745117, 0.016091108322143555, 0.030985355377197266,
                     0.01603078842163086, 0.028106212615966797, 0.0270693302154541, 0.027150869369506836,
                     0.028096914291381836, 0.03010082244873047, 0.028027057647705078, 0.02442622184753418,
                     0.001047372817993164, 0.028105735778808594, 0.017078876495361328, 0.026123046875,
                     0.02505326271057129, 0.025009870529174805, 0.0020127296447753906, 0.020010709762573242,
                     0.025995731353759766, 0.025959253311157227, 0.008998632431030273, 0.029972314834594727,
                     0.028971433639526367, 0.0020003318786621094, 0.028007030487060547, 0.024983644485473633]
brute_force_decisions = [True, False, True, False, False, False, False, True, True, True, True, False, True, False,
                         False, True, False, True, False, True, True, True, True, False, False, False, True, True,
                         False, False, True, True, False, True, True, False, False, True, True, True, False, True,
                         False, True, True, False, False, False, True, False, True, False, True, True, False, True,
                         True, False, False, True, False, True, False, False, True, False, True, False, True, True,
                         True, True, False, True, True, False, True, False, False, False, False, False, False, False,
                         True, False, True, False, False, False, True, True, False, True, True, False, False, True,
                         False, True]

avg_time_bf = mean(brute_force_times)
print(avg_time_bf)  # 0.020903899669647216

dfs_times = [0.005047321319580078, 0.003998517990112305, 0.0010123252868652344, 0.005047798156738281,
             0.0049991607666015625, 0.0046880245208740234, 0.0030052661895751953, 0.0009992122650146484,
             0.002002239227294922, 0.0030019283294677734, 0.0039844512939453125, 0.0020003318786621094,
             0.0009686946868896484, 0.003996849060058594, 0.005047798156738281, 0.00500035285949707,
             0.004002094268798828, 0.0009992122650146484, 0.0039958953857421875, 0.0029997825622558594,
             0.0010001659393310547, 0.002000093460083008, 0.0039997100830078125, 0.0039997100830078125,
             0.0039997100830078125, 0.003999948501586914, 0.003999948501586914, 0.0010001659393310547,
             0.0030002593994140625, 0.00400233268737793, 0.0040013790130615234, 0.001998424530029297,
             0.005998849868774414, 0.0020020008087158203, 0.002000093460083008, 0.0040130615234375,
             0.004012346267700195, 0.0030028820037841797, 0.0040400028228759766, 0.004000663757324219,
             0.003055095672607422, 0.001004934310913086, 0.0030317306518554688, 0.0010004043579101562,
             0.0010037422180175781, 0.004055023193359375, 0.002000093460083008, 0.004000425338745117,
             0.0010116100311279297, 0.002996683120727539, 0.0019996166229248047, 0.0030007362365722656,
             0.0029981136322021484, 0.004002809524536133, 0.00400543212890625, 0.004001617431640625,
             0.0009999275207519531, 0.003034353256225586, 0.00400090217590332, 0.004001140594482422,
             0.004046916961669922, 0.003001689910888672, 0.002997875213623047, 0.003958940505981445,
             0.0039997100830078125, 0.0029926300048828125, 0.005000114440917969, 0.004999876022338867,
             0.0010004043579101562, 0.00099945068359375, 0.004000663757324219, 0.0009996891021728516,
             0.005000114440917969, 0.0009999275207519531, 0.0019998550415039062, 0.006017446517944336,
             0.0020051002502441406, 0.004007816314697266, 0.003015279769897461, 0.005028963088989258,
             0.004031181335449219, 0.004999637603759766, 0.004004001617431641, 0.0029659271240234375,
             0.0010492801666259766, 0.004041194915771484, 0.004032135009765625, 0.0029981136322021484,
             0.003046274185180664, 0.0030028820037841797, 0.0010328292846679688, 0.004004001617431641,
             0.002999544143676758, 0.005034923553466797, 0.002001523971557617, 0.004999876022338867,
             0.0029997825622558594, 0.0009999275207519531, 0.0029997825622558594, 0.004999876022338867]
dfs_decisions = [True, False, True, False, False, False, False, True, True, True, True, False, True, False, False, True,
                 False, True, False, True, True, True, True, False, False, False, True, True, False, False, True, True,
                 False, True, True, False, False, True, True, True, False, True, False, True, True, False, False, False,
                 True, False, True, False, True, True, False, True, True, False, False, True, False, True, False, False,
                 True, False, True, False, True, True, True, True, False, True, True, False, True, False, False, False,
                 False, False, False, False, True, False, True, False, False, False, True, True, False, True, True,
                 False, False, True, False, True]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.003203885555267334

# comparing decisions
print(brute_force_decisions == dfs_decisions)  # True