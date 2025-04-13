import csv
import json

def get_countries_for_tables():
    result = {}
    
    with open('./data/countries.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        
        for row in reader:
            continent = row['continent']
            country_data = {
                'country': row['country'],
                'capital': row['capital']
            }
            
            if continent not in result:
                result[continent] = []
            result[continent].append(country_data)
    
    return result

def get_all_countries():
    countries = []
    with open('./data/countries.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            countries.append(row)

    result = json.dumps(countries, ensure_ascii=False)

    return result