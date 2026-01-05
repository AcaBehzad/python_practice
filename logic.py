import csv

def read_data(INPUT_FILE : str) -> list:
    """
    This function reads the csv (input file) and returns a list of the data of all members.
    
    :param INPUT_FILE: CSV path
    :type INPUT_FILE: str
    :return: list containing two lists 
    1- A list of field names
    2- A list of the data of all members (Each member as a dictionary.)
    :rtype: list
    """
    try:
        with open(INPUT_FILE,'r',encoding='utf-8') as f:

            reader = csv.DictReader(f)
            rows = list(reader)
            fieldname = reader.fieldnames

            if reader.fieldnames == None:
                raise('File has no header')
            
    except FileNotFoundError:
        print(f"There is no file found in the {INPUT_FILE}")

    return [fieldname, rows]

def bmi_calculator(all_members: list) -> list:
    """
    This fucntions calculates BMI of our members. 
    
    :param all_members: List of all members
    :type all_members: list
<<<<<<< HEAD
    :return: it adds BMI to each member data,and returns new list of all members with BMI values added.
=======
    :return: It adds BMI to each member data,and returns new list of all members with BMI values added.
>>>>>>> add-new-filters
    :rtype: list
    """
    for member in all_members:
        bmi = float(member['weight'])/(float(member['height'])/100)**2
        member['bmi'] = bmi
    
    return all_members


    