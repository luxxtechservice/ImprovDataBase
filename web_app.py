from flask import Flask, request, jsonify

app = Flask(__name__)

class SpreadsheetDatabase:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)
        return "Record added."

    def search_by_name(self, name):
        return [record for record in self.records if record['name'] == name]

    def search_by_id(self, _id):
        for record in self.records:
            if record['id'] == _id:
                return record
        return None

    def get_all_records(self):
        return self.records

    def delete_record(self, _id):
        self.records = [record for record in self.records if record['id'] != _id]
        return "Record deleted."

db = SpreadsheetDatabase()

@app.route('/records', methods=['POST'])
def add_record():
    data = request.json
    return db.add_record(data)

@app.route('/records/name/<string:name>', methods=['GET'])
def search_by_name(name):
    return jsonify(db.search_by_name(name))

@app.route('/records/id/<int:_id>', methods=['GET'])
def search_by_id(_id):
    record = db.search_by_id(_id)
    return jsonify(record if record else {'error': 'Record not found'})

@app.route('/records', methods=['GET'])
def get_all_records():
    return jsonify(db.get_all_records())

@app.route('/records/id/<int:_id>', methods=['DELETE'])
def delete_record(_id):
    return db.delete_record(_id)

if __name__ == '__main__':
    app.run(debug=True)