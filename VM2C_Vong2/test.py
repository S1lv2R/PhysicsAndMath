import gurobipy as gp
import numpy as np
from gurobipy import GRB

a = [1, 2, 2] # a[i] Số lượng công nhân tối thiểu cho giai đoạn i
n = 17      # Số lượng công nhân
k = len(a)

b = np.zeros((n, k))    # Công nhân i có làm công việc j hay không ?
c = np.ones((n, k))     # Công nhân i có được làm công việc j trong ca hay không ?
d = np.zeros(n)     # Số ngày làm việc của công nhân i
t = [""]

dict = ["dieu khien may rot", "dieu khien may dong hop", "pallet"]

with open("./output.txt", "w") as file:
    file.write("")

def setup_array(j, file):
    with open(file) as file:
        lines = file.readlines()

    for line in lines:
        b[int(line.rstrip()[1:]) - 1, j] = 1

def write_output(text):
    with open("./output.txt", "a", encoding="utf-8") as file:
        file.write(text)

setup_array(0, './ky_nang_Day_chuyen_1_Rot.txt')
setup_array(1, './ky_nang_Day_chuyen_1_May_dong_hop.txt')
setup_array(2, './ky_nang_Day_chuyen_1_Pallet.txt')

def calculate():
    model = gp.Model()
    vars = model.addMVar(shape=(n, k), vtype=GRB.BINARY)

    for j in range(3):
        model.addConstr((b[:, j] * c[:, j] * vars[:, j]).sum() >= a[j])

    for i in range(n):
        model.addConstr(vars[i, :].sum() <= 1)
    
    objective = gp.LinExpr()
    objective += vars.sum()
    for i in range(n):
        for j in range(k):
            if b[i][j] == 1:
                objective += d[i] * vars[i][j]

    model.setObjective(objective, sense=GRB.MINIMIZE)
    model.optimize()
    return vars.x.astype(int)

days = 28
for i in range(days * 3):
    result = calculate()
    indices = np.argwhere(result == 1)
    text = "Ca " + str(i + 1) + "\n"
    not_be_ones = []
    for j in range(len(indices)):
        h = indices[j, :]
        text += "V" + str(h[0] + 1) + " Ky nang: " + dict[h[1]] + "\n"
        d[h[0]] += 1
        c[h[0], h[1]] = 0
        not_be_ones.append([h[0], h[1]])
    
    if ((i + 1) % 3 == 0):
        c = np.ones((n, k))
        # for i in range(len(not_be_ones)):
        #     c[not_be_ones[i][0], not_be_ones[i][1]] = 0

    write_output(text + "\n")

print(d)