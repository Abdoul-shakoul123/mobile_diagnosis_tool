"""
Database Module
- Inashughulikia kusoma/kuandika data kutoka JSON au SQLite
"""

import json

class Database:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except:
            return {}

    def save_data(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
