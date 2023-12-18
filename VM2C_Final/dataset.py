import numpy as np
from constants import JOBS, JOB_LIST, SHIFTS, HOURS_PER_SHIFT

class Dataset:
    def __init__(self):
        self.data_path = "./data/duLieu1/" 
        self.workers_count = 0
        self.skills = []
        self.shift_time = np.zeros((29, 3), dtype=int)
        self.pipeline_req = (1, 2, 2)
        self.names = {}

        self.load_input()
    def load_input(self):
        with open(self.data_path + "01_nhan_su.txt", "r") as f:
            f.readline()  # Comment line
            _names = [line.strip().split() for line in f.readlines()]

            self.names = dict([worker[1], int(worker[0]) - 1]
                              for worker in _names)

            self.workers_count = len(self.names)
            self.skills = np.array([[0] * JOBS for _ in range(self.workers_count)])
        
        for job_idx in range(JOBS):
            job = JOB_LIST[job_idx]
            with open(self.data_path + f"ky_nang_Day_chuyen_1_{job}.txt", "r") as f:
                worker_list = [line.strip() for line in f.readlines()]
                for worker_name in worker_list:
                    worker = self.names[worker_name]
                    self.skills[worker][job_idx] = 1

        convert_to_start_time = lambda _time: 6 if 6 <= _time < 14 else 14 if 14 <= _time < 22 else 22
        convert_to_end_time = lambda _time: 14 if 6 < _time <= 14 else 22 if 14 < _time <= 22 else 30

        with open(self.data_path + "lenh_san_xuat_Day_chuyen_1.txt", "r") as f:
            f.readline()  # Comment line
            _time = [line.strip().split() for line in f.readlines()]
            shift_start_time = [6, 14, 22]

            for i in range(len(_time)):
                start_day = int(_time[i][0][8:10])
                start_hour = int(_time[i][1][0:2])

                end_day = int(_time[i][2][8:10])
                end_hour = int(_time[i][3][0:2])

                if (start_hour >= 0 and start_hour < shift_start_time[0]):
                    self.shift_time[start_day - 1, 2] = 1
                    continue
        
                new_start_hour = convert_to_start_time(start_hour)
                new_end_hour = convert_to_end_time(end_hour)
                active_shifts = (new_end_hour - new_start_hour) // HOURS_PER_SHIFT
        
                shifts = [1] * active_shifts
                if (new_start_hour == shift_start_time[0]):
                    self.shift_time[start_day, :active_shifts] = shifts
                elif (new_start_hour == shift_start_time[1]):
                    self.shift_time[start_day, 1:(active_shifts + 1)] = shifts
                    if active_shifts > 2:
                        self.shift_time[start_day + 1, 0] = 1
                elif (new_start_hour == shift_start_time[2]):
                    self.shift_time[start_day, 2] = 1
                    if active_shifts > 1:
                        self.shift_time[start_day + 1, :active_shifts] = shifts
