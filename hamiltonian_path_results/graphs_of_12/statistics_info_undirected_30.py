from statistics import mean

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [0.3375728130340576, 3.811018943786621, 0.06461215019226074, 0.023237943649291992, 0.01699972152709961,
             1.911754846572876, 0.0051882266998291016, 0.035039424896240234, 0.03299689292907715, 0.18600010871887207,
             0.00499725341796875, 0.05052304267883301, 0.026217937469482422, 0.02218317985534668, 0.003191709518432617,
             0.012000322341918945, 0.7284231185913086, 2.171412706375122, 0.018000125885009766, 0.400249719619751,
             0.08324432373046875, 1.4258127212524414, 0.0989389419555664, 0.048181772232055664, 0.12925004959106445,
             0.013216495513916016, 0.006994724273681641, 6.25328803062439, 0.1683487892150879, 0.005163908004760742,
             0.05555295944213867, 0.3971588611602783, 0.0030384063720703125, 0.0019986629486083984, 0.838019609451294,
             0.011182069778442383, 0.0060024261474609375, 14.770867586135864, 0.02914905548095703, 0.015000104904174805,
             2.122117757797241, 0.010286331176757812, 0.008999824523925781, 0.2709500789642334, 5.425347089767456,
             0.02718973159790039, 0.002000093460083008, 0.01900172233581543, 1.956221342086792, 0.02119588851928711,
             22.730144262313843, 0.22177481651306152, 0.06019282341003418, 6.8575279712677, 0.02039813995361328,
             0.0029993057250976562, 0.008184194564819336, 0.004003286361694336, 1.0468294620513916,
             0.029250621795654297, 0.07799768447875977, 0.012000560760498047, 0.07700061798095703, 1.1060457229614258,
             0.00703740119934082, 0.09638214111328125, 0.05147099494934082, 0.3850393295288086, 0.24795103073120117,
             0.058211326599121094, 0.6357784271240234, 0.016210079193115234, 0.0020008087158203125, 0.9780728816986084,
             0.09321808815002441, 0.13054442405700684, 0.4612588882446289, 0.006254434585571289, 0.09496521949768066,
             0.11519002914428711, 0.025444984436035156, 0.03935694694519043, 6.789109945297241, 0.8382096290588379,
             0.03299903869628906, 0.04631829261779785, 0.001998424530029297, 0.665820837020874, 0.1468214988708496,
             1.1227941513061523, 0.022169113159179688, 1.5033986568450928, 0.013218402862548828, 0.26872944831848145,
             4.1236395835876465, 0.7648847103118896, 0.9921762943267822, 0.13451695442199707, 0.019217491149902344,
             2.470123052597046]
dfs_decisions = [True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                 False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True,
                 True, True, True, False, True, True, True, True, True, True, False, True, True, True, False, True,
                 False, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True,
                 True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True,
                 True, True, True, True, True, False, True, False, True, True, False, True, True, True, True, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 0.9974022197723389

# comparing decisions
# print(brute_force_decisions == dfs_decisions)
