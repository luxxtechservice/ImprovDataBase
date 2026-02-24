class SpreadsheetData:
    def __init__(self):
        self.data = []

    def add_entry(self, name, grade, comp):
        entry = {'name': name, 'grade': grade, 'comp': comp}
        self.data.append(entry)

    def get_all_entries(self):
        return self.data

    def get_entry(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return None

    def remove_entry(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]