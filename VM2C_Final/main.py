from constants import SHIFTS, JOBS, JOB_LIST, DAYS, ALLOWED_DAYS
from dataset import Dataset
from gurobipy import GRB
import gurobipy as gp
import numpy as np
import sys

data, W, D, N = None, None, None, None
A, B, C = 10, 1, 5

def load_input(data_pack):
    global data
    data = Dataset(f"duLieu{data_pack}")

def write_output(text, data_pack):
    with open(f"./result/result_data_{data_pack}_part_a.txt", "a") as file:
        file.write(text)

def clear_file(data_pack):
    with open(f"./result/result_data_{data_pack}_part_a.txt", "w") as file:
        file.write("")

def optimize_current_shift(env, pipeline_idx):
    model = gp.Model(env=env)
    vars = model.addMVar(shape=(data.workers_count, JOBS), vtype=GRB.BINARY)

    for i in range(data.workers_count):
        model.addConstr(vars[i, :] <= data.skills[i, pipeline_idx, :])
        model.addConstr(vars[i, :].sum() <= 1)
        model.addConstr(vars[i, :].sum() + D[i] <= ALLOWED_DAYS)
    
    for j in range(JOBS):
        model.addConstr((W * vars[:, j]).sum() >= data.pipeline_req[pipeline_idx, j])

    objective = gp.LinExpr()
    objective += vars.sum()
    
    for i in range(data.workers_count):
        if data.skills[i, :].sum() > 1:
            objective += C * (A * D[i] + B * N[i]) * vars[i, :].sum()
        else:
            objective += (A * D[i] + B * N[i]) * vars[i, :].sum()
    
    model.setObjective(objective, sense=GRB.MINIMIZE)
    model.optimize()

    if model.status == GRB.INFEASIBLE:
        print("Solution not found")
        print(data.skills[:, pipeline_idx, :])
        exit(0)

    return vars.x.astype(int)

def run(env, data_pack):
    workers_chosen_last_night = np.zeros((data.workers_count), dtype=int)
    last_night = 0

    global W
    
    for day in range(1, len(data.shift_time)):
        magic_pointer = 0
        for shift_idx in range(1, JOBS + 1):
            for pipeline_idx in range(data.pipeline):
                if data.shift_time[day, pipeline_idx, shift_idx - 1] < 1:
                    continue

                magic_pointer += 1
                    
                print(f"[Log] day: {day}, pipeline: {pipeline_idx + 1}, shift: {shift_idx}")

                if magic_pointer == 1:
                    W *= np.logical_not(workers_chosen_last_night)
                elif magic_pointer == np.sum(data.shift_time[day, :, shift_idx - 2]) + 1 and shift_idx > 1 and day > 1:
                    W = np.logical_or(W, workers_chosen_last_night)

                night_shift = int(shift_idx == 3)
                workers_chosen = optimize_current_shift(env, pipeline_idx)
                only_workers_chosen = np.argwhere(workers_chosen == 1)

                output = ""
                for s in range(len(only_workers_chosen)):
                    worker, skill = only_workers_chosen[s, :]
                    W[worker] = 0
                    D[worker] += 1
                    N[worker] += 1 * night_shift

                    output += f"{day:02d}.06.2023 Ca_{shift_idx} V{(worker + 1):02d} Day_chuyen_{pipeline_idx + 1} {JOB_LIST[skill]}\n"

                if night_shift:
                    one_row_workers_chosen = [workers_chosen[i].sum() for i in range(data.workers_count)]
                    workers_chosen_last_night = (
                            one_row_workers_chosen
                            if last_night != day
                            else np.logical_or(workers_chosen_last_night, one_row_workers_chosen)
                    )
                    last_night = day

                write_output(output, data_pack)
        W = np.ones((data.workers_count), dtype=int)

def main():
    data_pack = sys.argv[1] or 1

    load_input(data_pack)

    env = gp.Env(empty = True)
    env.setParam('OutputFlag', 0)
    env.start()
    
    global W, D, N

    W = np.ones((data.workers_count), dtype=int)
    D = np.zeros((data.workers_count), dtype=int)
    N = np.zeros((data.workers_count), dtype=int)
    
    clear_file(data_pack)

    run(env, data_pack)
    print(D, N)

if __name__ == "__main__":
    main()
