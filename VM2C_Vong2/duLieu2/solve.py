import gurobipy as gp
import numpy as np
from gurobipy import GRB
import datetime

a = [1, 2, 2] # a[i] Số lượng công nhân tối thiểu cho giai đoạn i
n = 17      # Số lượng công nhân
k = len(a)

b = np.zeros((n, k))    # Công nhân i có làm công việc j hay không ?
c = np.ones((n, k))     # Công nhân i có được làm công việc j trong ca hay không ?
d = np.zeros(n)         # Tổng số ngày làm việc của công nhân i
t = []

dict = ["May_dong_hop", "Rot", "Pallet "]

with open("./result_data_1_part_a.txt", "w") as file:
    file.write("")

def setup_workers(j, file):
    with open(file) as file:
        lines = file.readlines()

    for line in lines:
        b[int(line.rstrip()[1:]) - 1, j] = 1

def setup_time(file):
    with open(file) as file:
        lines = file.readlines()[1:] # Bỏ qua line đầu
        for line in lines:
            item = line.strip().split('; ')
            start_time = datetime.datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S")
            end_time = datetime.datetime.strptime(item[1], "%Y-%m-%d %H:%M:%S")
            
            shifts = check_shifts(start_time, end_time)
            t.append([start_time, end_time, shifts])
            print(f"Ca lam viec trong khoang {item[0]} -> {item[1]}: {', '.join(shifts[i][0] for i in range(len(shifts)))}")

def check_shifts(start_time, end_time):
    shifts = []
    if start_time.hour >= 22 or (6 > start_time.hour >= 0):
        if 6 < end_time.hour <= 14:
            shifts.extend([['Ca_3', start_time.hour, 6], ['Ca_1', 6, end_time.hour]])
        elif end_time.hour <= 6:
            shifts.extend([['Ca_3', start_time.hour, end_time.hour]])
    elif start_time.hour >= 14:
        if 6 < end_time.hour <= 14:
            shifts.extend([['Ca_2', start_time.hour, 22], ['Ca_3', 22, 6], ['Ca_1', 6, end_time.hour]])
        elif end_time.hour <= 6:
            shifts.extend([['Ca_2', start_time.hour, 22], ['Ca_3', 22, end_time.hour]])
        elif end_time.hour <= 22:
            shifts.extend([['Ca_2', start_time.hour, end_time.hour]])
    elif start_time.hour >= 6:
        if end_time.hour <= 6:
            shifts.extend([['Ca_1', start_time.hour, 14], ['Ca_2', 14, 22], ['Ca_3', 22, end_time.hour]])
        elif 14 < end_time.hour <= 22:
            shifts.extend([['Ca_1', start_time.hour, 14], ['Ca_2', 14, end_time.hour]])
        elif end_time.hour <= 14:
            shifts.extend([['Ca_1', start_time.hour, end_time.hour]])
    return shifts

def write_output(text):
    with open("./result_data_1_part_a.txt", "a", encoding="utf-8") as file:
        file.write(text)

# Đọc dữ liệu để khởi tạo danh sách việc làm cho các công nhân
setup_workers(0, './ky_nang_Day_chuyen_1_Rot.txt')
setup_workers(1, './ky_nang_Day_chuyen_1_May_dong_hop.txt')
setup_workers(2, './ky_nang_Day_chuyen_1_Pallet.txt')

# Đọc dữ liệu để khởi tạo danh sách thời gian dây chuyền hoạt động
setup_time('./lenh_san_xuat_Day_chuyen_1.txt')

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

old_indices = np.array([])
last_shift = ""
last_date = None
for i in range(len(t)):
    start_time, end_time, shifts = t[i]
    for j in range(len(shifts)):
        # print(shifts[j])
        shift, start, end = shifts[j]
        result = calculate()
        indices = np.argwhere(result == 1) # Liệt kê danh sách các công nhân được chọn do gurobi tính toán
        start_date = start_time
        end_date = end_time
        
        if start_time < end_time and start < end and shift in "Ca_3":
            start_date = end_time
        elif start_time < end_time and start < end and shift in ["Ca_1", "Ca_2"]:
            end_date = start_time

        output = ""

        # Lặp qua danh sách indices
        for s in range(len(indices)):
            h = indices[s, :] # Thông tin: i (công nhân thứ i), j (kỹ năng thứ j)
            vid = "V" + (str(h[0] + 1) if (h[0] + 1) >= 10 else "0" + str(h[0] + 1)) # ID của công nhân
            output += f"{start_date.strftime('%d.%m.%Y')} {shift} {vid} Day_chuyen_1 {dict[h[1]]}\n"
            d[h[0]] += 1 # Tăng 1 ngày làm việc cho công nhân
            c[h[0], h[1]] = 0 # Công nhân chỉ được làm 1 ca trong ngày

        if shift in "Ca_3":
            c = np.ones((n, k))
            for i in range(len(indices)): # Các công nhân làm ca tối nay sẽ không được làm ca sáng hôm sau
                c[indices[i, 0], indices[i, 1]] = 0
            old_indices = indices
        
        if last_shift in "Ca_3" and not (shift in "Ca_1"):
            for i in range(len(old_indices)):
                c[old_indices[i, 0], old_indices[i, 1]] = 1

        if last_date != None:
            if start_time > last_date or end_time > start_time:
                for i in range(len(old_indices)):
                    c[old_indices[i, 0], old_indices[i, 1]] = 1
        
        last_date = end_time
        last_shift = shift
        write_output(output)

print(d)