import datetime

t = []

with open("./output.txt", "w") as file:
    file.write("")

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
            shifts.extend([['Ca toi', start_time.hour, 6], ['Ca sang', 6, end_time.hour]])
        elif end_time.hour <= 6:
            shifts.extend([['Ca toi', start_time.hour, end_time.hour]])
    elif start_time.hour >= 14:
        if 6 < end_time.hour <= 14:
            shifts.extend([['Ca chieu', start_time.hour, 22], ['Ca toi', 22, 6], ['Ca sang', 6, end_time.hour]])
        elif end_time.hour <= 6:
            shifts.extend([['Ca chieu', start_time.hour, 22], ['Ca toi', 22, end_time.hour]])
        elif end_time.hour <= 22:
            shifts.extend([['Ca chieu', start_time.hour, end_time.hour]])
    elif start_time.hour >= 6:
        if end_time.hour <= 6:
            shifts.extend([['Ca sang', start_time.hour, 14], ['Ca chieu', 14, 22], ['Ca toi', 22, end_time.hour]])
        elif 14 < end_time.hour <= 22:
            shifts.extend([['Ca sang', start_time.hour, 14], ['Ca chieu', 14, end_time.hour]])
        elif end_time.hour <= 14:
            shifts.extend([['Ca sang', start_time.hour, end_time.hour]])
    return shifts

def write_output(text):
    with open("./output.txt", "a", encoding="utf-8") as file:
        file.write(text)

# Đọc dữ liệu để khởi tạo danh sách thời gian dây chuyền hoạt động
setup_time('./lenh_san_xuat_Day_chuyen_1.txt')

last_shift = ""
last_date = None
for i in range(len(t)):
    start_time, end_time, shifts = t[i]
    for j in range(len(shifts)):
        shift, start, end = shifts[j]
        start_date = start_time
        end_date = end_time
        
        if start_time < end_time and start < end and shift in "Ca toi":
            start_date = end_time
        elif start_time < end_time and start < end and shift in ["Ca sang", "Ca chieu"]:
            end_date = start_time

        output = f"{shift} {start_date.strftime('%Y-%m-%d')} {start}:00:00 -> {end_date.strftime('%Y-%m-%d')} {end}:00:00 \n"
        write_output(output)