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
            

def bmi_filter(bmi_caled_members : list) -> list[dict]:
    """
    This function separates members based on their BMI into 4 groups.
    
    :param bmi_caled_members: List of all members with their BMI calculated.
    :type bmi_caled_members: list
    :return: A list which has member's BMI group specified. Each member is represented by a dict, 
    and a key exists in that dict called bmi group which determines member's group.
    :rtype: list
    """
    bmi_gped_members = bmi_caled_members
    for member in bmi_gped_members:
        if member['bmi'] < 18.5: 
            member['bmi group'] = 'underweighted'
        elif member['bmi'] < 24.9:
            member['bmi group'] = 'normal'
        elif member['bmi'] < 29.9:
            member['bmi group'] = 'overweighted'
        else:
            member['bmi group'] = 'obese'
    
    return bmi_gped_members


def age_filter(all_members: list) -> dict[str:list]:
    """
    Age filter filters all member based on their ages between 4 group.
    
    :param all_members: List containing info of all members (Each member is a dict)
    :type all_members: list
    :return: A list which has member's age group specified. Each member is represented by a dict, 
    and a key exists in that dict called age group which determines member's age group.
    :rtype: list
    """
    age_gped_members = all_members

    for member in age_gped_members:
        if int(member['age']) < 23:
            member['age group'] = 'youth'
        elif int(member['age']) < 40:
            member['age group'] = 'adult'
        elif int(member['age']) < 60:
            member['age group'] = 'middle age'
        else:
            member['age group'] = 'old'

    return age_gped_members