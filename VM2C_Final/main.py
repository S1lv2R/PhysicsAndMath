from dataset import Dataset
from constants import SHIFTS, JOBS, JOB_LIST, DAYS, ALLOWED_DAYS
import gurobipy as gp
from gurobipy import GRB
import numpy as np

data, W, D, N = None, None, None, None
A, B = 10, 1

def load_input():
    global data
    data = Dataset("duLieu2")

def write_output(text):
    with open("./result_data_2_part_a.txt", "a") as file:
        file.write(text)

def clear_file():
    with open("./result_data_2_part_a.txt", "w") as file:
        file.write("")

def optimize_current_shift(env, pipeline_idx):
    model = gp.Model(env=env)
    vars = model.addMVar(shape=(data.workers_count, JOBS), vtype=GRB.BINARY)

    for i in range(data.workers_count):
        model.addConstr(vars[i, :] <= data.skills[i, pipeline_idx, :])
    
    for j in range(JOBS):
        model.addConstr((W[:, pipeline_idx, j] * vars[:, j]).sum() >= data.pipeline_req[pipeline_idx, j])

    for i in range(data.workers_count):
        model.addConstr(vars[i, :].sum() <= 1)
        model.addConstr(vars[i, :].sum() + D[i] <= ALLOWED_DAYS)

    objective = gp.LinExpr()
    objective += vars.sum()
    
    for i in range(data.workers_count):
        objective += (A * D[i] + B * N[i]) * vars[i, :].sum()

    model.setObjective(objective, sense=GRB.MINIMIZE)
    model.optimize()

    if model.status == GRB.INFEASIBLE:
        print("Solution not found")
        exit(0)

    return vars.x.astype(int)

def run(env):
    workers_chosen_last_night = np.zeros((data.workers_count, data.pipeline, JOBS), dtype=int)
    for day in range(1, len(data.shift_time)):
        for pipeline_idx in range(data.pipeline):
            for shift_idx in range(1, len(data.shift_time[day, pipeline_idx, :]) + 1):
                if data.shift_time[day, pipeline_idx, shift_idx - 1] < 1:
                    continue
                
                print(day, pipeline_idx, shift_idx)
                global W
            
                if shift_idx == 1:
                    W[:, pipeline_idx, :] *= np.logical_not(workers_chosen_last_night[:, pipeline_idx, :])
                elif shift_idx == 2:
                    W[:, pipeline_idx, :] = np.logical_or(W[:, pipeline_idx, :], workers_chosen_last_night[:, pipeline_idx, :])
            
                night_shift = int(shift_idx == 3)
                workers_chosen = optimize_current_shift(env, pipeline_idx)
                only_workers_chosen = np.argwhere(workers_chosen == 1)

                output = ""
                for s in range(len(only_workers_chosen)):
                    worker, skill = only_workers_chosen[s, :]
                    W[worker, pipeline_idx, skill] = 0
                    D[worker] += 1
                    N[worker] += 1 * night_shift

                    output += f"{day:02d}.06.2023 Ca_{shift_idx} V{(worker + 1):02d} Day_chuyen_{pipeline_idx + 1} {JOB_LIST[skill]}\n"
            
                if night_shift:
                    workers_chosen_last_night[:, pipeline_idx, :] = workers_chosen
                write_output(output)
        W = np.ones((data.workers_count, data.pipeline, JOBS), dtype=int)

def main():
    load_input()

    env = gp.Env(empty = True)
    env.setParam('OutputFlag', 0)
    env.start()
    
    global W, D, N

    W = np.ones((data.workers_count, data.pipeline, JOBS), dtype=int)
    D = np.zeros((data.workers_count), dtype=int)
    N = np.zeros((data.workers_count), dtype=int)
    
    clear_file()

    run(env)
    print(D, N)

if __name__ == "__main__":
    main()
