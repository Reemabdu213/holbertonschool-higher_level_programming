#!/usr/bin/python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and write to data.json.

    Args:
        csv_filename (str): The CSV filename to read from.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
