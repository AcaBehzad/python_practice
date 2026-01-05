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
            


