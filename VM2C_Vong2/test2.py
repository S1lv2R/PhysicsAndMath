import gurobipy as gp
import numpy as np
from gurobipy import GRB

d = [1, 2, 2, 3]

model = gp.Model()
vars = model.addMVar(shape=(len(d)), vtype=GRB.BINARY)

objective = gp.LinExpr()
for i in range(len(d)):
    objective += d[i] * vars[i]

model.setObjective(objective, GRB.MINIMIZE)
model.addConstr(vars.sum() == 1)

model.optimize()

if model.status == GRB.OPTIMAL:
    print(vars.x.astype(int))
else:
    print("Khong co loi giai\n")