import csv

def sex_sep(all_members: list) -> list[list[dict],list[dict]]:
    """
    This function receives the list of all members in our data base and seperate them
    into two lists based on their gender.
    
    :param rows: it takes all members
    :type rows: list
    :return: it returns two lists:
    1 - Male members
    2 - Female members
    :rtype: list[list[dict]]
    """
    male_members = []
    female_members = []
    for row in all_members:
        if row['sex'] == 'M':
            male_members.append(row)
        elif row['sex'] == 'F':
            female_members.append(row)
    
    return [male_members,female_members]

def city_sep(all_members: list) -> dict[str:list]:
    """
    This function receives the list of all members in our data base and seperate them
    based on their hometown.
    
    :param rows: All members
    :type rows: list
    :return: a dictionary with keys set as cities, and values are the list of those members living 
    in that city
    :rtype: dict
    """
    city_sep_members = {}
    for row in all_members:
        if row['city'] in city_sep_members.keys():
            city_sep_members[row['city']].append(row)
        else:
            city_sep_members[row['city']] = []
            city_sep_members[row['city']].append(row)

    return city_sep_members
            

def bmi_filter(bmi_caled_members : list) -> dict[str:list]:
    """
    This function separates members based on their BMI into 4 groups.
    
    :param bmi_caled_members: List of all members with their BMI calculated.
    :type bmi_caled_members: list
    :return: A dictionary with 4 keys and under each key there is a list containing all members in that group.
    :rtype: dict
    """
    bmi_group = {'underweight':[],
                 'normal weight':[],
                 'overweight':[],
                 'obese': []}
    for member in bmi_caled_members:
        if member['bmi'] < 18.5: 
            bmi_group['underweight'].append(member)
        elif member['bmi'] < 24.9:
            bmi_group['normal weight'].append(member)
        elif member['bmi'] < 29.9:
            bmi_group['overweight'].append(member)
        else:
            bmi_group['obese'].append(member)
    
    return bmi_group
