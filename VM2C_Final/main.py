from dataset import Dataset
from constants import SHIFTS, JOBS, JOB_LIST, DAYS, ALLOWED_DAYS
import gurobipy as gp
from gurobipy import GRB
import numpy as np

data, W, D, N = None, None, None, None
A, B = 10, 1

def load_input():
    global data
    data = Dataset()

def write_output(text):
    with open("./result_data_1_part_a.txt", "a") as file:
        file.write(text)

def clear_file():
    with open("./result_data_1_part_a.txt", "w") as file:
        file.write("")

def optimize_current_shift(env):
    model = gp.Model(env=env)
    vars = model.addMVar(shape=(data.workers_count, JOBS), vtype=GRB.BINARY)

    for i in range(data.workers_count):
        model.addConstr(vars[i, :] <= data.skills[i, :])
        model.addConstr(vars[i, :].sum() <= 1)
        model.addConstr(vars[i, :].sum() + D[i] <= ALLOWED_DAYS)
    
    for j in range(JOBS):
        model.addConstr((W[:, j] * vars[:, j]).sum() >= data.pipeline_req[j])

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
    workers_chosen_last_night = np.zeros((data.workers_count, JOBS), dtype=int)
    for day in range(1, len(data.shift_time)):
        for shift_idx in range(1, len(data.shift_time[day][:]) + 1):
            if data.shift_time[day][shift_idx - 1] < 1:
                continue

            global W
            
            if shift_idx == 1:
                W *= np.logical_not(workers_chosen_last_night) # W *= ~workers_chosen_last_night
            elif shift_idx == 2:
                W = np.logical_or(W, workers_chosen_last_night) # W |= workers_chosen_last_night
            
            night_shift = int(shift_idx == 3)
            workers_chosen = optimize_current_shift(env=env)
            only_workers_chosen = np.argwhere(workers_chosen == 1)

            output = ""
            for s in range(len(only_workers_chosen)):
                worker, skill = only_workers_chosen[s, :]
                W[worker, skill] = 0
                D[worker] += 1
                N[worker] += 1 * night_shift

                output += f"{day:02d}.06.2023 Ca_{shift_idx} V{(worker + 1):02d} Day_chuyen_1 {JOB_LIST[skill]}\n"
            
            if night_shift:
                workers_chosen_last_night = workers_chosen
            write_output(output)
        W = np.ones((data.workers_count, JOBS), dtype=int)

def main():
    load_input()

    env = gp.Env(empty = True)
    env.setParam('OutputFlag', 0)
    env.start()
    
    global W, D, N

    W = np.ones((data.workers_count, JOBS), dtype=int)
    D = np.zeros((data.workers_count), dtype=int)
    N = np.zeros((data.workers_count), dtype=int)
    
    clear_file()

    run(env)
    print(D, N)

if __name__ == "__main__":
    main()
