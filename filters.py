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

def city_sep(rows: list) -> dict[str:list]:
    city_sep_members = {}
    for row in rows:
        if row['city'] in city_sep_members.keys():
            city_sep_members[row['city']].append(row)
        else:
            city_sep_members[row['city']] = []
            city_sep_members[row['city']].append(row)

    return city_sep_members
            


