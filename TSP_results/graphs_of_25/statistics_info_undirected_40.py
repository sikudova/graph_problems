from statistics import mean
from math import inf

brute_force_times = []
brute_force_decisions = []

# avg_time_bf = mean(brute_force_times)
# print(avg_time_bf)

dfs_times = [8.793488264083862, 10.407680034637451, 4.357997179031372, 20.6908175945282, 12.81088900566101,
             1.8349840641021729, 4.872957706451416, 2.7999439239501953, 10.37790822982788, 7.782968282699585,
             6.3039772510528564, 20.8058180809021, 11.621897459030151, 8.512922048568726, 2.337979316711426,
             5.032923221588135, 37.46170663833618, 57.565589427948, 39.424694299697876, 53.63855242729187,
             9.900896549224854, 5.179967641830444, 5.62199330329895, 33.666773319244385, 7.161987781524658,
             9.058975458145142, 30.509774923324585, 3.774977445602417, 6.906956434249878, 10.599931716918945,
             5.4579291343688965, 34.33979344367981, 3.645012855529785, 42.122756481170654, 14.238879442214966,
             12.433927774429321, 8.050915241241455, 10.099939107894897, 13.521921157836914, 7.313992977142334,
             20.954881191253662, 25.30286455154419, 9.13194990158081, 12.297932147979736, 3.1569507122039795,
             13.94592547416687, 13.871928215026855, 0.0, 6.541966199874878, 9.365915060043335, 17.58591079711914,
             27.247856855392456, 6.338937759399414, 9.213922262191772, 8.961926698684692, 4.291948556900024,
             7.476962566375732, 3.4639856815338135, 1.5599596500396729, 12.012977361679077, 0.4389975070953369,
             8.228994369506836, 6.790939807891846, 2.6650211811065674, 2.7760214805603027, 20.766904830932617,
             18.354878187179565, 12.610939741134644, 5.534942388534546, 8.336959838867188, 47.45076036453247,
             0.0010027885437011719, 0.0009968280792236328, 0.0029997825622558594, 62.076735496520996, 6.153006315231323,
             6.332941770553589, 18.070892095565796, 3.104025363922119, 14.357939958572388, 26.052900075912476,
             6.206973075866699, 5.145020246505737, 33.44190955162048, 13.743948459625244, 43.74279808998108,
             5.2799766063690186, 13.919948101043701, 1.3629953861236572, 25.415947914123535, 8.707971572875977,
             39.66186547279358, 9.907934427261353, 2.58595871925354, 17.423691987991333, 1.3949775695800781,
             27.449501991271973, 15.922708749771118, 7.169903993606567, 4.046933174133301]
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
print(avg_time_dfs)  # 13.664074635505676

dfs_cut_times = [8.678877115249634, 10.109874725341797, 4.563927888870239, 21.563841819763184, 12.787888765335083,
                 1.9039793014526367, 4.8789567947387695, 2.7380082607269287, 10.445872783660889, 7.824897527694702,
                 6.2989442348480225, 21.362810611724854, 11.692900657653809, 8.784924507141113, 2.2699787616729736,
                 5.2169506549835205, 37.59767460823059, 57.99652099609375, 39.99672865867615, 53.96365523338318,
                 9.810935735702515, 5.076965570449829, 5.721964120864868, 33.78773808479309, 7.0649168491363525,
                 9.000939846038818, 30.613823652267456, 3.8239715099334717, 6.9889843463897705, 10.746927976608276,
                 5.457996845245361, 35.29775595664978, 3.6869778633117676, 42.9077422618866, 14.345948934555054,
                 12.734927415847778, 8.002989768981934, 10.14594030380249, 13.661882400512695, 7.200957775115967,
                 21.525886058807373, 25.991863012313843, 9.591917276382446, 12.366970300674438, 3.3080148696899414,
                 14.002926111221313, 14.26992392539978, 0.00099945068359375, 6.612966537475586, 9.605945825576782,
                 17.636938095092773, 27.757858753204346, 6.559002637863159, 9.200987815856934, 8.890989780426025,
                 4.289015054702759, 7.524929523468018, 3.438016891479492, 1.603991985321045, 12.172942638397217,
                 0.45896315574645996, 8.059953927993774, 6.921970844268799, 2.6209516525268555, 2.767951488494873,
                 20.845935106277466, 18.04195284843445, 12.641938924789429, 5.70397424697876, 8.53399133682251,
                 47.23483657836914, 0.0, 0.0, 0.0019998550415039062, 62.40470504760742, 6.011974096298218,
                 6.3630051612854, 18.138920545578003, 3.1229515075683594, 14.58293890953064, 26.831900358200073,
                 6.41497540473938, 5.089940786361694, 33.53787183761597, 14.03494906425476, 43.96983313560486,
                 5.123015403747559, 13.684911727905273, 1.4259984493255615, 25.58691096305847, 8.819971084594727,
                 40.06286096572876, 10.089999198913574, 2.601024866104126, 18.25570034980774, 1.4889724254608154,
                 27.310507774353027, 15.81768274307251, 6.990871429443359, 4.114887475967407]
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
print(avg_time_dfs_cut)  # 13.788212883472443

# comparing decisions
# print(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)
print(dfs_decisions == dfs_cut_decisions)  # true
