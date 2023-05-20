from statistics import mean

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [4.713940858840942, 1.1070201396942139, 0.6739940643310547, 0.8319888114929199, 1.9909732341766357,
             0.42099618911743164, 0.4819643497467041, 1.4860098361968994, 3.680955171585083, 0.7129571437835693,
             1.9970066547393799, 9.970871448516846, 1.5169825553894043, 2.4539666175842285, 2.7849643230438232,
             0.37599611282348633, 0.8789529800415039, 0.8540270328521729, 2.161973237991333, 0.7319521903991699,
             2.0149741172790527, 1.2490234375, 1.1729824542999268, 12.951798677444458, 10.111908435821533,
             1.168952465057373, 2.9399938583374023, 1.0674731731414795, 1.2569873332977295, 8.560924291610718,
             0.17698144912719727, 9.342982530593872, 5.905895709991455, 0.6119897365570068, 2.441965341567993,
             6.030930995941162, 12.9508695602417, 1.4240014553070068, 2.1229405403137207, 3.538956880569458,
             0.24999713897705078, 0.29999232292175293, 0.5220308303833008, 5.192934274673462, 0.36199212074279785,
             3.7549185752868652, 0.5700292587280273, 0.20699810981750488, 1.9319405555725098, 1.485978126525879,
             0.62103271484375, 2.7169599533081055, 0.838953971862793, 2.9419991970062256, 1.0779509544372559,
             0.6140258312225342, 6.433887243270874, 1.5309810638427734, 0.33502697944641113, 0.6249608993530273,
             1.5230131149291992, 4.534948110580444, 0.9939804077148438, 1.4269464015960693, 0.6250283718109131,
             1.785975456237793, 1.740980625152588, 0.35999345779418945, 2.7099666595458984, 2.8939621448516846,
             0.279998779296875, 5.374897480010986, 7.034951686859131, 0.5249922275543213, 0.4649982452392578,
             1.9859819412231445, 3.535965919494629, 23.941744804382324, 3.8789963722229004, 1.0549919605255127,
             2.8299853801727295, 0.9150230884552002, 0.6229627132415771, 0.3440279960632324, 3.2439701557159424,
             0.32596492767333984, 1.1880226135253906, 1.7909839153289795, 2.9249684810638428, 0.6959977149963379,
             7.133597135543823, 27.970494270324707, 5.928944826126099, 0.6709976196289062, 0.4309957027435303,
             1.4259867668151855, 11.494902849197388, 0.20199990272521973, 1.790980577468872, 0.2569999694824219]
dfs_decisions = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False]

avg_time_dfs = mean(dfs_times)
print(avg_time_dfs)  # 2.980427362918854

# comparing decisions
print(brute_force_decisions == dfs_decisions)