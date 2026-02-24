import json

class SpreadsheetDatabase:
    def __init__(self):
        self.records = []
        self.id_counter = 1

    def add_record(self, name, grade, comp):
        record = {
            'id': self.id_counter,
            'name': name,
            'grade': grade,
            'comp': comp
        }
        self.records.append(record)
        self.id_counter += 1
        print(f"Record added: {record}")

    def search_by_name(self, name):
        found_records = [record for record in self.records if record['name'] == name]
        return found_records

    def search_by_id(self, record_id):
        for record in self.records:
            if record['id'] == record_id:
                return record
        return None

    def display_records(self):
        for record in self.records:
            print(record)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.records, f)
        print("Records saved to file.")

if __name__ == "__main__":
    db = SpreadsheetDatabase()
    
    # Example usage:
    db.add_record("Alice", "A", "Math")
    db.add_record("Bob", "B", "Science")
    
    print("Search for Alice:", db.search_by_name("Alice"))
    print("Search for ID 1:", db.search_by_id(1))
    
    db.display_records()
    db.save_to_file("records.json")
