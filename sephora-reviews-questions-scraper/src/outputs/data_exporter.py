thonimport json

class DataExporter:
    def export_data(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)