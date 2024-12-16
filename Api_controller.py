from flask import Flask, request, jsonify

# Create a Flask application
app = Flask(__name__)

# Sample data to act as a database
data = [
    {"id": 1, "name": "John Doe", "department": "HR"},
    {"id": 2, "name": "Jane Smith", "department": "IT"}
]

# Route to fetch all records
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(data), 200

# Route to fetch a specific record by ID
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((emp for emp in data if emp['id'] == employee_id), None)
    if employee:
        return jsonify(employee), 200
    else:
        return jsonify({"error": "Employee not found"}), 404

# Route to add a new record
@app.route('/employees', methods=['POST'])
def add_employee():
    new_employee = request.json
    if 'id' in new_employee and 'name' in new_employee and 'department' in new_employee:
        data.append(new_employee)
        return jsonify(new_employee), 201
    else:
        return jsonify({"error": "Invalid input"}), 400

# Route to update an existing record
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = next((emp for emp in data if emp['id'] == employee_id), None)
    if employee:
        updates = request.json
        employee.update(updates)
        return jsonify(employee), 200
    else:
        return jsonify({"error": "Employee not found"}), 404

# Route to delete a record
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    global data
    data = [emp for emp in data if emp['id'] != employee_id]
    return jsonify({"message": "Employee deleted"}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)