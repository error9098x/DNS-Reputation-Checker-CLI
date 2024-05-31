import json

def read_domains_from_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_report(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
