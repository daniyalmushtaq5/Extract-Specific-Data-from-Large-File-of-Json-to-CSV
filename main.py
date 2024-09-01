import ijson
import csv
from rich import print

def extract_data_json_to_csv(json_file_path : str, csv_file_path : str):
    with open(json_file_path, 'r') as file:
        with open(csv_file_path, 'w', newline='') as csv_file:

            header_names = ['UID', 'Title', 'Abstract', 'Author Names:Affiliation', 'Journal Name', 'Volume', 'Published Date', 'Eissn', 'DOI']
            writer = csv.DictWriter(csv_file, fieldnames=header_names)
            
            writer.writeheader()
    
            objects = ijson.items(file, 'Records.records.REC.item')
            for obj in objects:
                try:
                    uid = obj['UID']
                except(KeyError,TypeError):
                    uid = "N/A"

                try:
                    for title_type in obj['static_data']['summary']['titles']['title']:
                        if title_type['type'] == 'item':
                            title = title_type['content']
                except(KeyError,TypeError):
                    title = "N/A"

                try:
                    abstract = obj['static_data']['fullrecord_metadata']['abstracts']['abstract']['abstract_text']['p']
                except(KeyError,TypeError):
                    abstract = "N/A"

                try:
                    authers_name_and_affiliations = ""
                    items = obj['static_data']['fullrecord_metadata']['addresses']['address_name']
                    if isinstance(items, dict):
                        items = [items]

                    for item in items:
                        names = item['names']['name']
                        if isinstance(names, dict):
                            names = [names] 

                        affiliation = item['address_spec']['organizations']['organization'][0]['content']                        
                        authers_name_and_affiliations += " | ".join(
                            f"{name['full_name']} : {affiliation}" for name in names
                        ) + " | "

                    # Strip the last trailing ' | ' and print the final result
                    authers_name_and_affiliations = authers_name_and_affiliations.rstrip(' | ')
                except(TypeError,KeyError):
                    authers_name_and_affiliations = "N/A"

                try:
                    journal_name = obj['static_data']['summary']['publishers']['publisher']['names']['name']['unified_name']
                except(TypeError,KeyError):
                    journal_name = obj['static_data']['summary']['publishers']['publisher']['names']['name']['full_name']

                try:
                    pub_date = obj['static_data']['summary']['pub_info']['sortdate']
                except(TypeError,KeyError):
                    pub_date = "N/A"

                try:
                    volume = obj['static_data']['summary']['pub_info']['vol']
                except(TypeError,KeyError):
                    volume = "N/A"

                try:
                    eissn = ""
                    doi = ""
                    items = obj['dynamic_data']['cluster_related']['identifiers']['identifier']
                    if isinstance(items,dict):
                        items = [items]
                    for item in items:
                        if item['type'] == "eissn" or item['type'] == "issn":
                            eissn = item['value']
                        if item['type'] == 'doi':
                            doi = item['value']
                except(TypeError,KeyError):
                    eissn = "N/A"
                    doi = "N/A"

                row = {
                    'UID' : uid,
                    'Title' : title,
                    'Abstract': abstract,
                    'Author Names:Affiliation' : authers_name_and_affiliations,
                    'Journal Name': journal_name,
                    'Volume' : volume,
                    'Published Date' : pub_date, 
                    'Eissn' : eissn, 
                    'DOI' : doi
                }

                writer.writerow(row)

if __name__ == "__main__":
    extract_data_json_to_csv("./export.json", "./data.csv")



