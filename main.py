from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR/"athletes.csv"

from logic import read_data
from filters import sex_sep

fieldnames = read_data(INPUT_FILE)[0]
rows = read_data(INPUT_FILE)[1]

[male_members , female_members] = sex_sep(rows)

print(female_members[0:3])


