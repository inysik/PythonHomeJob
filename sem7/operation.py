import csv
import json
import pickle


def load_data(file_name, file_type):
    with open(file_name, 'rb') as f:
        if file_type == 'pickle':
            return pickle.load(f)
        elif file_type == 'json':
            return json.load(f)
        elif file_type == 'csv':
            reader = csv.reader(f)
            return [{'name': row[0], 'phone': row[1]} for row in reader]
        else:
            raise ValueError('Invalid file type')


def save_data(file_name, file_type, data):
    with open(file_name, 'wb') as f:
        if file_type == 'pickle':
            pickle.dump(data, f)
        elif file_type == 'json':
            json.dump(data, f)
        elif file_type == 'csv':
            writer = csv.writer(f)
            for entry in data:
                writer.writerow([entry['name'], entry['phone']])
        else:
            raise ValueError('Invalid file type')