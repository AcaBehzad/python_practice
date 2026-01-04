import csv

def read_data(INPUT_FILE : str) -> list:
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