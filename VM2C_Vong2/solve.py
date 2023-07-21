import gurobipy as gp
import numpy as np
from gurobipy import GRB

a = [1, 2, 2] # a[i] Số lượng công nhân tối thiểu cho giai đoạn i
n = 17      # Số lượng công nhân
k = len(a)

b = np.zeros((n, k))    # Công nhân i có làm công việc j hay không ?
c = np.ones((n, k))     # Công nhân i có được làm công việc j trong ca hay không ?
d = np.zeros(n)         # Tổng số ngày làm việc của công nhân i

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

# Đọc dữ liệu
setup_array(0, './ky_nang_Day_chuyen_1_Rot.txt')
setup_array(1, './ky_nang_Day_chuyen_1_May_dong_hop.txt')
setup_array(2, './ky_nang_Day_chuyen_1_Pallet.txt')

def calculate():
    model = gp.Model()

    # Đây là quy hoạch tuyến tính nhị phân
    vars = model.addMVar(shape=(n, k), vtype=GRB.BINARY)

    for j in range(3):
        # Ràng buộc 1: Số lượng công nhân được chọn để làm trong giai đoạn j tối thiểu là a[j]
        model.addConstr((b[:, j] * c[:, j] * vars[:, j]).sum() >= a[j])

    for i in range(n):
        # Ràng buộc 2: Công nhân chỉ được làm 1 công việc duy nhất trong một ca
        model.addConstr(vars[i, :].sum() <= 1)
    
    objective = gp.LinExpr()
    objective += vars.sum() # Hàm mục tiêu 1: Số lượng công nhân được chọn là nhỏ nhất
    for i in range(n):
        for j in range(k):
            if b[i][j] == 1:
                # Hàm mục tiêu 2: Ưu tiên chọn các công nhân có tổng số ngày làm việc ít (công bằng)
                objective += d[i] * vars[i][j]

    model.setObjective(objective, sense=GRB.MINIMIZE)
    model.optimize()

    return vars.x.astype(int)

days = 28
old_indices = np.array([])
for i in range(days * 3):
    result = calculate()
    indices = np.argwhere(result == 1) # Liệt kê danh sách (i, j) được chọn do gurobi tính toán
    output = "Ca " + str(i + 1) + "\n"
    for j in range(len(indices)): # Lặp qua danh sách indices
        h = indices[j, :] # Thông tin: i (công nhân thứ i), j (kỹ năng thứ j)
        vid = "V" + (str(h[0] + 1) if (h[0] + 1) >= 10 else "0" + str(h[0] + 1)) # ID của công nhân
        output += vid + " Ky nang: " + dict[h[1]] + "\n"
        d[h[0]] += 1 # Tăng số ngày làm việc đối với công nhân được chọn
        c[h[0], h[1]] = 0 # Công nhân được chọn trong ca hôm nay sẽ không được làm các ca khác trong ngày
    
    if ((i + 1) % 3 == 0): # Nếu hết một ngày
        # Sang hôm sau các công nhân đều có thể làm việc (RESET), trừ các công nhân làm ca tối hôm qua
        c = np.ones((n, k))
        for i in range(len(indices)):
            c[indices[i, 0], indices[i, 1]] = 0
        old_indices = indices
    elif ((i + 1) % 2 == 0):
        # Sang ngày thứ hai thì những công nhân làm ca đêm hôm trước sẽ bắt đầu đi làm
        for i in range(len(old_indices)):
            c[old_indices[i, 0], old_indices[i, 1]] = 1

    write_output(output)

print(d)