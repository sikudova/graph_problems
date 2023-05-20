import time
from graphs_files.graphs_25_undirected_50 import graphs

FILE_NAME = "statistics_info_undirected_50.py"

with open('TSP_results/graphs_of_25/{}'.format(FILE_NAME), 'a') as f:
    print("from statistics import mean\nfrom math import inf\n", file=f)

brute_force_times = []
brute_force_decisions = []

dfs_times = []
dfs_decisions = []

dfs_cut_times = []
dfs_cut_decisions = []

count = 0
# loop through all graphs
for graph in graphs:
    count += 1
    print(f"graph no {count}")

    # brute force
    # start_time = time.time()
    # decision_bf = graph.TSP_brute_force()
    # end_time = time.time()
    #
    # execution_time_bf = end_time - start_time
    # brute_force_times.append(execution_time_bf)
    # brute_force_decisions.append(decision_bf)

    # dfs
    start_time = time.time()
    decision_dfs = graph.TSP_DFS()
    end_time = time.time()

    execution_time_dfs = end_time - start_time
    dfs_times.append(execution_time_dfs)
    dfs_decisions.append(decision_dfs)

    # dfs with cut
    start_time = time.time()
    decision_dfs_cut = graph.TSP_DFS_cut()
    end_time = time.time()

    execution_time_dfs_cut = end_time - start_time
    dfs_cut_times.append(execution_time_dfs_cut)
    dfs_cut_decisions.append(decision_dfs_cut)

with open('TSP_results/graphs_of_25/{}'.format(FILE_NAME), 'a') as f:
    # brute force
    print(f"brute_force_times = {brute_force_times}", file=f)
    print(f"brute_force_decisions = {brute_force_decisions}\n", file=f)
    print("avg_time_bf = mean(brute_force_times)", file=f)
    print("print(avg_time_bf)", file=f)

    # dfs
    print(f"\ndfs_times = {dfs_times}", file=f)
    print(f"dfs_decisions = {dfs_decisions}\n", file=f)
    print("avg_time_dfs = mean(dfs_times)", file=f)
    print("print(avg_time_dfs)", file=f)

    # dfs with cut
    print(f"\ndfs_cut_times = {dfs_cut_times}", file=f)
    print(f"dfs_cut_decisions = {dfs_cut_decisions}\n", file=f)
    print("avg_time_dfs_cut = mean(dfs_cut_times)", file=f)
    print("print(avg_time_dfs_cut)", file=f)

    # comparing decisions
    print(
        "\n# comparing decisions\nprint(brute_force_decisions == dfs_decisions and dfs_decisions == dfs_cut_decisions)",
        file=f)
