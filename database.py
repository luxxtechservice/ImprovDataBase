class Database:
    def __init__(self):
        self.records = []  # Initialize an empty list to store records

    def add_record(self, record):
        """Adds a new record to the database."""
        self.records.append(record)

    def search_by_id(self, record_id):
        """Search for a record by its ID."""
        for record in self.records:
            if record['id'] == record_id:
                return record
        return None

    def get_all_records(self):
        """Returns all records in the database."""
        return self.records

    def __repr__(self):
        return f"Database(records={{len(self.records)}})"  # Return a string representation of the database