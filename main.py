import time
from graphs_files.graphs_5_undirected import graphs

# from statistics import mean

with open('hamiltonian_path_results/graphs_of_5/{}'.format("statistics_info.py"), 'a') as f:
    print("from statistics import mean\n", file=f)

brute_force_times = []
brute_force_decisions = []

dfs_times = []
dfs_decisions = []

# loop through all graphs
for graph in graphs:
    # brute force
    start_time = time.time()
    decision_bf = graph.hamiltonian_path_brute_force_decision()
    end_time = time.time()

    execution_time_bf = end_time - start_time
    brute_force_times.append(execution_time_bf)
    brute_force_decisions.append(decision_bf)

    # dfs
    start_time = time.time()
    decision_dfs = graph.hamiltonian_path_DFS_decision()
    end_time = time.time()

    execution_time_dfs = end_time - start_time
    dfs_times.append(execution_time_dfs)
    dfs_decisions.append(decision_dfs)

    # print(f"Execution time: {execution_time_bf} seconds, decision: {decision_bf}")

with open('hamiltonian_path_results/graphs_of_5/{}'.format("statistics_info.py"), 'a') as f:
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
