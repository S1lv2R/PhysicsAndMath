import gurobipy as gp
import numpy as np
from gurobipy import GRB

model = gp.Model()

a = [1, 2, 2] # a[i] Số lượng công nhân tối thiểu cho giai đoạn i
n = 17      # Số lượng công nhân
k = len(a)  #

b = np.zeros((n, k))
c = np.ones((n, k))

dict = ["điều khiển máy rót", "điều khiển máy đóng hộp", "pallet"]

with open("./output.txt", "w") as file:
    file.write("")

def setup_array(j, file):
    with open(file) as file:
        lines = file.readlines()

    for line in lines:
        b[int(line.rstrip()[1:]) - 1, j] = 1

def write_output(text):
    with open("./output.txt", "a") as file:
        file.write(text + "\n")

setup_array(0, './ky_nang_Day_chuyen_1_Rot.txt')
setup_array(1, './ky_nang_Day_chuyen_1_May_dong_hop.txt')
setup_array(2, './ky_nang_Day_chuyen_1_Pallet.txt')

vars = model.addMVar(shape=(n, k), vtype=GRB.BINARY)

for j in range(3):
    model.addConstr((b[:, j] * vars[:, j]).sum() >= a[j])

for i in range(n):
    model.addConstr(vars[i, :].sum() <= 1)

total = (c * vars).sum()
model.setObjective(total, sense=GRB.MINIMIZE)

days = 1
for k in range(days * 3):
    print(c)
    model.optimize()
    text = "Ca " + str(k + 1) + "\n"

    indices = np.argwhere(vars.x.astype(int) == 1)
    for i in range(len(indices)):
        j = indices[i, :]
        text = text + "V" + str(j[0] + 1) + " Kỹ năng: " + dict[j[1]] + "\n"
        c[j[0], j[1]] = 0
    write_output(text)
