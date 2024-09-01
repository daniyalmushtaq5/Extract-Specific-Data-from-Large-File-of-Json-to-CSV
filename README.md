JSON to CSV Converter

This Python script extracts data from a JSON file and writes it into a CSV file. The script is designed to handle specific fields from the JSON file, such as UID, Title, Abstract, Author Names:Affiliation, Journal Name, Volume, Published Date, Eissn, and DOI.
Features

    Parses large JSON files using ijson for efficient memory usage.
    Extracts specific fields from nested JSON objects.
    Handles missing or malformed data gracefully.
    Outputs a well-formatted CSV file with customizable headers.

Requirements

    Python 3.x
    Required Python packages:
        ijson
        csv (part of Python's standard library)
        rich (for pretty-printing, optional)

You can install the required packages using pip:

bash

pip install ijson rich

Usage

    Prepare your JSON file:
        Place your JSON file in the same directory as the script, or provide the path to the file.

    Run the script:
        You can run the script using the command line:

        bash

    python your_script_name.py

    The script will convert the JSON data in export.json to a CSV file named data.csv.

Customize input/output:

    If you want to use a different JSON input file or output CSV file, modify the extract_data_json_to_csv function call in the __main__ section:

    python

        extract_data_json_to_csv("path/to/your/input.json", "path/to/your/output.csv")

Example

bash

python your_script_name.py

This command will convert the JSON data from export.json into a CSV file named data.csv.
Code Overview

The script defines a single function, extract_data_json_to_csv, which performs the following:

    Opens the JSON file and initializes a CSV writer.
    Iterates over JSON objects using ijson.items for efficient parsing.
    Extracts relevant fields, handling missing data with default values (N/A).
    Writes the extracted data into a CSV file with predefined headers.

Handling of Specific Fields

    UID: Unique identifier.
    Title: Extracted from the static_data.summary.titles.title field.
    Abstract: Extracted from the static_data.fullrecord_metadata.abstracts.abstract.abstract_text.p field.
    Author Names
    : Combines author names with their affiliations.
    Journal Name: Extracted from the static_data.summary.publishers.publisher.names.name.
    Volume: Extracted from the static_data.summary.pub_info.vol.
    Published Date: Extracted from the static_data.summary.pub_info.sortdate.
    Eissn: Extracted from the dynamic_data.cluster_related.identifiers.identifier.
    DOI: Extracted from the dynamic_data.cluster_related.identifiers.identifier.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

For any questions or issues, please open an issue on this repository.
