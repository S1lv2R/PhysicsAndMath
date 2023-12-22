from pathlib import Path

root_path = Path(__file__).parent.parent
data_root_path = root_path / "data"

HOURS_PER_SHIFT = 8
ALLOWED_DAYS = 22 
DAYS = 28
SHIFTS = DAYS * 3
JOBS = 3 

JOB_LIST = ["Rot", "May_dong_hop", "Pallet"]

C = 1.3
