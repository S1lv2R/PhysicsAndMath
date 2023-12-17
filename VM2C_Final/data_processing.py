import numpy as np

HOURS_PER_SHIFT = 8
shift_time = np.zeros((29, 3), dtype=int)

def convert_to_start_time(_time):
    return 6 if 6 <= _time < 14 else 14 if 14 <= _time < 22 else 22

def convert_to_end_time(_time):
    return 14 if 6 < _time <= 14 else 22 if 14 < _time <= 22 else 30

with open(f"lenh_san_xuat_Day_chuyen_1.txt", "r") as f:
    f.readline()  # Comment line
    _time = [line.strip().split() for line in f.readlines()]

    shift_start_time = [6, 14, 22]

    for i in range(len(_time)):
        start_day = int(_time[i][0][8:10])
        start_hour = int(_time[i][1][0:2])

        end_day = int(_time[i][2][8:10])
        end_hour = int(_time[i][3][0:2])

        if (start_hour >= 0 and start_hour < shift_start_time[0]):
            shift_time[start_day - 1, 2] = 1
            continue
        
        new_start_hour = convert_to_start_time(start_hour)
        new_end_hour = convert_to_end_time(end_hour)
        active_shifts = (new_end_hour - new_start_hour) // HOURS_PER_SHIFT
        
        shifts = [1] * active_shifts
        if (new_start_hour == shift_start_time[0]):
            shift_time[start_day, :active_shifts] = shifts
        elif (new_start_hour == shift_start_time[1]):
            shift_time[start_day, 1:(active_shifts + 1)] = shifts
            if active_shifts > 2:
                shift_time[start_day + 1, 0] = 1
        elif (new_start_hour == shift_start_time[2]):
            shift_time[start_day, 2] = 1
            if active_shifts > 1:
                shift_time[start_day + 1, :active_shifts] = shifts

print(shift_time)
