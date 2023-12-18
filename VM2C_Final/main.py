from dataset import Dataset
from constants import SHIFTS, JOBS, JOB_LIST, DAYS
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

def optimize_current_shift(env):
    model = gp.Model(env=env)
    vars = model.addMVar(shape=(data.workers_count, JOBS), vtype=GRB.BINARY)
    
    for j in range(3):
        model.addConstr((data.skills[:, j] * W[:, j] * vars[:, j]).sum() >= data.pipeline_req[j])

    for i in range(data.workers_count):
        model.addConstr(vars[i, :].sum() <= 1)
   
    for i in range(data.workers_count):
        model.addConstr(vars[i, :].sum() + D[i] <= 24)

    objective = gp.LinExpr()
    objective += vars.sum()
    for i in range(data.workers_count):
        for j in range(JOBS):
            objective += A * (D[i] * vars[i, j]) + B * (N[i] * vars[i, j])

    model.setObjective(objective, sense=GRB.MINIMIZE)
    model.optimize()

    return vars.x.astype(int)

def run(env):
    workers_chosen_last_night = np.zeros((data.workers_count, JOBS), dtype=int)
    for day in range(1, len(data.shift_time)):
        for shift_idx in range(1, len(data.shift_time[day][:]) + 1):
            if data.shift_time[day][shift_idx - 1] < 1:
                continue

            global W
            
            output = ""
            if shift_idx == 1:
                W = W * np.logical_not(workers_chosen_last_night)
            elif shift_idx == 2:
                for i in range(len(workers_chosen_last_night)):
                    for j in range(JOBS):
                        if workers_chosen_last_night[i][j] == 1:
                            W[i, j] = 1

            print(day, shift_idx)
            print(W)
            print(D)
           
            night_shift = int(shift_idx == 3)
            workers_chosen = optimize_current_shift(env=env)
            indices = np.argwhere(workers_chosen == 1)

            for s in range(len(indices)):
                worker, skill = indices[s, :]
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
    
    global W
    W = np.ones((data.workers_count, JOBS), dtype=int)     # Công nhân i có được làm công việc j trong ca hay không ?

    global D
    D = np.zeros((data.workers_count), dtype=int)

    global N
    N = np.zeros((data.workers_count), dtype=int)

    run(env)
    print(D, N)

if __name__ == "__main__":
    main()
