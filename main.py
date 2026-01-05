from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR/"athletes.csv"

from logic import read_data, bmi_calculator
<<<<<<< HEAD
from filters import sex_sep, city_sep
=======
from filters import sex_sep, city_sep, bmi_filter
>>>>>>> add-new-filters

fieldnames = read_data(INPUT_FILE)[0]
all_members = read_data(INPUT_FILE)[1]
[male_members , female_members] = sex_sep(all_members)
city_sep_members = city_sep(all_members)
bmi_caled_members = bmi_calculator(all_members)
<<<<<<< HEAD

print(bmi_caled_members[0:2])
=======
underweighted = bmi_filter(bmi_caled_members)['underweight']
normal = bmi_filter(bmi_caled_members)['normal weight']
overweight = bmi_filter(bmi_caled_members)['overweight']
obese = bmi_filter(bmi_caled_members)['obese']
>>>>>>> add-new-filters
