from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR/"athletes.csv"

from logic import read_data, bmi_calculator
from filters import sex_sep, city_sep, bmi_filter, age_filter

fieldnames = read_data(INPUT_FILE)[0]
all_members = read_data(INPUT_FILE)[1]