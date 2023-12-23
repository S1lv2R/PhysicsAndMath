from constants import JOBS, JOB_LIST, DAYS, ALLOWED_DAYS, C
from dataset import Dataset
from gurobipy import GRB
import gurobipy as gp
import numpy as np
import sys

data, W, D, N = None, None, None, None

def load_input(data_pack):
    global data
    data = Dataset(f"duLieu{data_pack}")

def clear_file(data_pack):
    with open(f"../result/result_data_{data_pack}_part_a.txt", "w") as file:
        file.write("")

def write_the_schedule(text, data_pack):
    with open(f"../result/result_data_{data_pack}_part_a.txt", "a") as file:
        file.write(text)

def write_log(data_pack):
    with open(f"../logs/log_{data_pack}.txt", "w") as file:
        file.write(
            f"""
            ________________________________________________________________________________
            
            The standard deviation between workers' shifts:      \t{np.std(D)}
            The standard deviation between workers' night shifts:\t{np.std(N)}
            ________________________________________________________________________________
            """
        )

def optimize_current_shift(env, pipeline_idx, night_shift):
    model = gp.Model(env=env)
    vars = model.addMVar(shape=(data.workers_count, JOBS), vtype=GRB.BINARY)

    for i in range(data.workers_count):
        model.addConstr(vars[i] <= data.skills[i, pipeline_idx, :])  # Workers only do jobs that match their skills.
        model.addConstr(vars[i].sum() <= 1)                          # Workers only do one job per shift.
        model.addConstr(vars[i].sum() + D[i] <= ALLOWED_DAYS)        # Workers only work a maximum of {ALLOWED_DAYS} days.
    
    # Each shift must have a sufficient number of workers.
    for j in range(JOBS):
        model.addConstr(
                (W * vars[:, j]).sum() >= data.pipeline_req[pipeline_idx, j])

    objective = gp.LinExpr()
    objective += vars.sum()
    
    for i in range(data.workers_count):
        objective += (C if data.skills[i].sum() > 1 else 1) * (N[i] if night_shift else D[i]) * vars[i].sum()
    
    model.setObjective(objective, sense=GRB.MINIMIZE)
    model.optimize()

    if model.status == GRB.INFEASIBLE:
        print("Solution not found")
        exit(0)

    return vars.x.astype(int)

def run(env, data_pack):
    workers_chosen_last_night = np.zeros(data.workers_count, dtype=int)
    last_night = 0

    global W
   
    for day in range(1, len(data.shift_time)):
        magic_pointer = 0
        for shift_idx in range(1, JOBS + 1):
            for pipeline_idx in range(data.pipeline):
                if data.shift_time[day, pipeline_idx, shift_idx - 1] < 1:
                    continue
                
                magic_pointer += 1
                    
                print(f"[Log] day: {day}, pipeline: {pipeline_idx + 1}, shift: {shift_idx}, magic_pointer: {magic_pointer}")
                
                # 1. Workers who worked the previous night's shift did not work the next morning's shift.
                # 2. Workers who worked the night shift before can work the afternoon shift and the evening shift the next day.

                if magic_pointer == 1:
                    W &= np.logical_not(workers_chosen_last_night)
                elif magic_pointer == np.sum(data.shift_time[day, :, shift_idx - 2]) + 1 and shift_idx > 1:
                    W |= workers_chosen_last_night
               
                night_shift = int(shift_idx == 3)
                workers_chosen = optimize_current_shift(env, pipeline_idx, night_shift)

                for worker in range(len(workers_chosen)):
                    for skill in range(JOBS):
                        if workers_chosen[worker][skill] < 1:
                            continue

                        N[worker] += 1 * night_shift
                        D[worker] += 1
                        W[worker] = 0

                        write_the_schedule(
                            f"{day:02d}.06.2023 Ca_{shift_idx} V{(worker + 1):02d} Day_chuyen_{pipeline_idx + 1} {JOB_LIST[skill]}\n",
                            data_pack
                        )

                if night_shift:
                    one_row_workers_chosen = np.array([workers_chosen[i].sum() for i in range(data.workers_count)])
                    workers_chosen_last_night = (
                        one_row_workers_chosen if last_night != day
                        else workers_chosen_last_night | one_row_workers_chosen
                    )
                    last_night = day
        W = np.ones(data.workers_count, dtype=int)

def main():
    data_pack = sys.argv[1] or 1

    load_input(data_pack)

    env = gp.Env(empty = True)
    env.setParam('OutputFlag', 0)
    env.start()
    
    global W, D, N

    W = np.ones(data.workers_count, dtype=int)
    D = np.zeros(data.workers_count, dtype=int)
    N = np.zeros(data.workers_count, dtype=int)
    
    clear_file(data_pack)

    run(env, data_pack)
    write_log(data_pack)
    print(D, N)

if __name__ == "__main__":
    main()
