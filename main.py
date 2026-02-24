def search_record_by_id(records, record_id):
    """Search for a record by ID in the records list."""
    for record in records:
        if record['id'] == record_id:
            return record
    return None

def display_all_data(records):
    """Display all records in a readable format."""
    for record in records:
        print(f"ID: {record['id']}, Data: {record['data']}")
