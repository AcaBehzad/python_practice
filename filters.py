import csv

def sex_sep(rows: list) -> list[list[dict],list[dict]]:
    male_members = []
    female_members = []
    for row in rows:
        if row['sex'] == 'M':
            male_members.append(row)
        elif row['sex'] == 'F':
            female_members.append(row)
    
    return [male_members,female_members]


